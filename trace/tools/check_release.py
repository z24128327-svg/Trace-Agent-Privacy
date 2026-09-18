"""Offline release checks. No network, model, credentials, or clinical input required."""

import ast
import csv
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP = {"__pycache__", ".cache", ".tools", "generated_figures"}
TEXT = {".py", ".json", ".md", ".csv", ".txt", ".svg"}
PATTERNS = {
    "credential": re.compile(r"\bsk-[A-Za-z0-9_-]{12,}\b"),
    "private_key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "local_absolute_path": re.compile(r"[A-Za-z]:[\\/](?:Users|code)[\\/]|/[r]oot/autodl|/[h]ome/[^/\s]+/"),
    "email": re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
}


def release_files():
    return sorted(path for path in ROOT.rglob("*") if path.is_file()
                  and not SKIP.intersection(path.relative_to(ROOT).parts) and path.suffix != ".pyc")


def check_source_files(files):
    parsed = 0
    for path in files:
        if path.suffix not in TEXT:
            continue
        text = path.read_text(encoding="utf-8-sig")
        for label, pattern in PATTERNS.items():
            if pattern.search(text):
                raise ValueError(f"Release scan: {label} in {path.relative_to(ROOT)}")
        if path.suffix == ".py":
            ast.parse(text, filename=path.relative_to(ROOT).as_posix())
            parsed += 1
        if path.suffix == ".json":
            json.loads(text)
    return parsed


def check_pseudocode():
    algorithms = list((ROOT / "pseudocode").glob("*.py"))
    experiments = list((ROOT / "experiments").glob("exp*.py"))
    if len(algorithms) != 8 or len(experiments) != 14:
        raise ValueError("Expected eight algorithm and fourteen experiment pseudocode files")
    for path in algorithms + experiments:
        tree = ast.parse(path.read_text())
        assignments = [node for node in tree.body if isinstance(node, ast.Assign)]
        names = {target.id for node in assignments for target in node.targets if isinstance(target, ast.Name)}
        if "PSEUDOCODE" not in names:
            raise ValueError(f"Missing pseudocode body: {path.name}")
    return {"algorithm_modules": 8, "experiment_modules": 14}


def read_csv(name):
    with (ROOT / "results/paper_reported" / f"{name}.csv").open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def check_results():
    expected = {"fixed": 62.0, "q_only": 74.0, "unguided": 80.0, "trace": 93.6}
    seed_rows = read_csv("rq1_seeds")
    if len(seed_rows) != 5:
        raise ValueError("Expected five reported acquisition seeds")
    for method, value in expected.items():
        if abs(sum(float(row[method]) for row in seed_rows) / 5 - value) > 1e-9:
            raise ValueError("Reported seed mean mismatch")
    transfer = read_csv("transfer")
    if sum(int(row["successes"]) for row in transfer) != 140 or sum(int(row["trials"]) for row in transfer) != 150:
        raise ValueError("Reported transfer count mismatch")
    return {"reported_result_csvs": len(list((ROOT / "results/paper_reported").glob("*.csv"))), "independently_reproduced": False}


def check_manifest(files):
    manifest = json.loads((ROOT / "MANIFEST.json").read_text())
    expected = {entry["path"]: entry["sha256"] for entry in manifest["files"]}
    actual = {path.relative_to(ROOT).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
              for path in files if path.name != "MANIFEST.json"}
    if expected != actual:
        raise ValueError("Release files differ from the recorded manifest")
    return len(actual)


def main():
    files = release_files()
    report = {"source_files_parsed": check_source_files(files), **check_pseudocode(), **check_results(),
              "manifest_files_checked": check_manifest(files),
              "scan_scope": "Known path/email/key patterns plus explicit content review; not proof of absolute anonymity"}
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
