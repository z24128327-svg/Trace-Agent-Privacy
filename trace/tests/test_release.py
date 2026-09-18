"""Checks for release-scanner regressions and generated-output isolation."""

import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools import check_release


class ReleaseTests(unittest.TestCase):
    def test_scanner_does_not_flag_its_own_patterns(self):
        path = ROOT / "tools/check_release.py"
        self.assertEqual(check_release.check_source_files([path]), 1)

    def test_local_path_patterns_detect_constructed_examples(self):
        pattern = check_release.PATTERNS["local_absolute_path"]
        examples = ["C:" + "/Users/example/file", "/" + "root/autodl/file", "/" + "home/example/file"]
        for example in examples:
            with self.subTest(example=example):
                self.assertIsNotNone(pattern.search(example))

    def test_generated_outputs_are_not_release_inputs(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_text("Public description", encoding="utf-8")
            generated = root / "generated_figures"
            generated.mkdir()
            (generated / "manifest.json").write_text("[]", encoding="utf-8")
            with patch.object(check_release, "ROOT", root):
                self.assertEqual(check_release.release_files(), [root / "README.md"])


if __name__ == "__main__":
    unittest.main()
