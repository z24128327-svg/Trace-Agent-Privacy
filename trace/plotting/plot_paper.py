"""Render manuscript-reported aggregates only; never import experiment runners."""

import csv
import json
import math
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if (ROOT / ".tools").is_dir():
    sys.path.insert(0, str(ROOT / ".tools"))
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".cache/matplotlib"))

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

DATA = ROOT / "results/paper_reported"
OUTPUT = ROOT / "generated_figures"
COLORS = ["#4472C4", "#ED7D31", "#389B55", "#8064A2", "#C49A25", "#666666"]


def configure_style():
    plt.rcParams.update({
        "font.family": "serif", "font.serif": ["Times New Roman", "DejaVu Serif"],
        "font.size": 9, "axes.labelsize": 9, "axes.labelweight": "bold",
        "axes.linewidth": 0.7, "xtick.labelsize": 8, "ytick.labelsize": 8,
        "xtick.direction": "in", "ytick.direction": "in", "lines.linewidth": 1.2,
        "lines.markersize": 4, "legend.fontsize": 8, "legend.frameon": True,
        "legend.fancybox": False, "legend.edgecolor": "0.75", "legend.framealpha": 0.95,
        "figure.facecolor": "white", "axes.facecolor": "white",
        "pdf.fonttype": 42, "ps.fonttype": 42, "svg.fonttype": "none",
        "savefig.dpi": 600,
    })


def load_rows(name):
    with (DATA / f"{name}.csv").open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if not rows or any(not row.get("source_page") for row in rows):
        raise ValueError(f"Missing rows or source pages: {name}")
    return rows


def numbers(rows, key):
    values = [float(row[key]) for row in rows]
    if any(not math.isfinite(value) or value < 0 for value in values):
        raise ValueError(f"Invalid numerical column: {key}")
    return values


def style_axes(axis, ylabel=None):
    for spine in axis.spines.values():
        spine.set_visible(True)
        spine.set_linewidth(0.7)
    axis.grid(axis="both", color="#D0D0D0", linewidth=0.5)
    axis.set_axisbelow(True)
    if ylabel:
        axis.set_ylabel(ylabel)


def finish(figure, name, source, bundle, manifest, title=""):
    figure.tight_layout(pad=0.7)
    for extension in ("png", "pdf", "svg"):
        figure.savefig(OUTPUT / f"{name}.{extension}", dpi=600, facecolor="white")
    bundle.savefig(figure, facecolor="white")
    manifest.append({"figure": name, "title": title, "source": source,
                     "data_origin": "Manuscript-reported aggregates; no experiments rerun",
                     "formats": ["png", "pdf", "svg"], "png_dpi": 600})
    plt.close(figure)


def horizontal(name, label, title, source, bundle, manifest):
    rows = load_rows(name)
    values = numbers(rows, "vsr_percent")
    figure, axis = plt.subplots(figsize=(5.4, max(2.4, len(rows) * 0.32 + 0.7)))
    bars = axis.barh([row[label] for row in rows], values, color=COLORS[0], height=0.58,
                     edgecolor="black", linewidth=0.4)
    for bar, row in zip(bars, rows):
        if row.get("aggregation") == "single_reference_run":
            bar.set_hatch("///")
            bar.set_facecolor("#D9E2F3")
    axis.bar_label(bars, labels=[f"{value:.1f}%" for value in values], padding=3, fontsize=8)
    axis.invert_yaxis()
    axis.set_xlim(0, 110)
    axis.set_xticks(range(0, 101, 20))
    axis.set_xlabel("Verified Success Rate (%)")
    style_axes(axis)
    axis.grid(False, axis="y")
    finish(figure, name, source, bundle, manifest, title)


def cross_backbone(bundle, manifest):
    rows = load_rows("transfer")
    values = numbers(rows, "vsr_percent")
    positions = list(range(len(rows)))
    mean_vsr = sum(values) / len(values)
    figure, axis = plt.subplots(figsize=(4.0, 2.8))
    axis.plot(positions, values, "o-", color=COLORS[0], label="TRACE (frozen)", zorder=3)
    axis.axhline(mean_vsr, color=COLORS[1], linestyle="--", linewidth=1.0,
                 label=f"Mean ({mean_vsr:.1f}%)", zorder=2)
    for position, value, row in zip(positions, values, rows):
        axis.annotate(f"{value:.1f}% ({row['successes']}/{row['trials']})", (position, value),
                      xytext=(0, -16), textcoords="offset points", ha="center", fontsize=8)
    axis.set(xlabel="Target backbone", xticks=positions,
             xticklabels=[row["backbone"] for row in rows], xlim=(-0.35, len(rows) - 0.65),
             ylim=(0, 103), yticks=range(0, 101, 20))
    axis.legend(loc="lower left")
    style_axes(axis, "Verified Success Rate (%)")
    finish(figure, "transfer", "Tables 2 / 6, pp.8,14; 50 trials per backbone", bundle, manifest,
           "Frozen cross-backbone evaluation; line joins categorical models, not a temporal trajectory")


def acquisition_seeds(bundle, manifest):
    rows = load_rows("rq1_seeds")
    figure, axis = plt.subplots(figsize=(4.8, 3.1))
    for index, key in enumerate(("fixed", "q_only", "unguided", "trace")):
        axis.plot([row["seed"] for row in rows], numbers(rows, key), "o-", color=COLORS[index],
                  linewidth=1.2, label=key.replace("_", " ").title())
    axis.set_ylim(0, 100)
    axis.set_xlabel("Acquisition seed")
    axis.legend(ncol=2, loc="lower right")
    style_axes(axis, "Verified Success Rate (%)")
    finish(figure, "rq1_seeds", "Table 4, p.14", bundle, manifest, "Held-out acquisition results across five seeds")


def evolution(bundle, manifest):
    rows = load_rows("evolution")
    figure, axes = plt.subplots(1, 3, figsize=(7.2, 2.5))
    generation = numbers(rows, "generation")
    panels = [("vsr_percent", "VSR (%)", (0, 110)), ("aar", "Average Agentic Rounds", (0, 3)),
              ("repertoire_size", "Retained strategies", (0, 12))]
    for index, (key, label, limits) in enumerate(panels):
        values = numbers(rows, key)
        axes[index].plot(generation, values, "o-", color=COLORS[index], linewidth=1.2)
        axes[index].set(xlabel="Generation", xticks=generation, ylim=limits,
                        xlim=(min(generation) - 0.45, max(generation) + 0.45))
        style_axes(axes[index], label)
        for position, value in zip(generation, values):
            axes[index].annotate(f"{value:g}", (position, value), xytext=(0, 8),
                                 textcoords="offset points", ha="center", fontsize=7)
    axes[2].axhline(10, linestyle="--", color="#888888", linewidth=0.8)
    axes[0].set_yticks(range(0, 101, 20))
    finish(figure, "evolution", "Figure 3 / Table 5, pp.7,14; development split", bundle, manifest,
           "Representative seed-21 development trajectory")


def candidate_accounting(bundle, manifest):
    rows = load_rows("candidates")
    figure, axis = plt.subplots(figsize=(5.4, 2.8))
    bars = axis.bar([row["stage"].replace(" ", "\n") for row in rows], numbers(rows, "count"), color=COLORS,
                    edgecolor="black", linewidth=0.4)
    axis.bar_label(bars, padding=4)
    axis.set_ylim(0, 85)
    style_axes(axis, "Candidate count")
    finish(figure, "candidates", "Appendix C, p.13; stages overlap, pruning follows admission", bundle, manifest,
           "Candidate accounting across five seeds and five generations")


def line_plot(name, key, value_key, xlabel, title, source, bundle, manifest):
    rows = load_rows(name)
    positions = numbers(rows, key)
    values = numbers(rows, value_key)
    figure, axis = plt.subplots(figsize=(4.0, 2.8))
    axis.plot(positions, values, "o-", color=COLORS[0], linewidth=1.2)
    axis.set(xlabel=xlabel, ylim=(0, 103), xticks=positions)
    for position, value in zip(positions, values):
        axis.annotate(f"{value:.1f}%", (position, value), xytext=(0, 9),
                      textcoords="offset points", ha="center", fontsize=8)
    style_axes(axis, "Verified Success Rate (%)")
    finish(figure, name, source, bundle, manifest, title)


def output_controls(bundle, manifest):
    rows = load_rows("output_controls")
    figure, axis = plt.subplots(figsize=(5.4, 3.1))
    for offset, key, label, color in [(-0.2, "residual_exposure_percent", "Residual exposure", COLORS[2]),
                                      (0.2, "utility_percent", "Benign utility", COLORS[0])]:
        bars = axis.bar([index + offset for index in range(len(rows))], numbers(rows, key),
                        width=0.36, label=label, color=color, edgecolor="black", linewidth=0.4)
        axis.bar_label(bars, labels=[f"{value:.1f}%" for value in numbers(rows, key)], padding=3, fontsize=8)
    labels = [f"{row['control']}\nRelative utility loss: {row['relative_utility_loss_percent']}%" for row in rows]
    axis.set(xticks=range(len(rows)), xticklabels=labels, ylim=(0, 114))
    axis.legend(loc="upper right", ncol=2)
    style_axes(axis, "Percent")
    finish(figure, "output_controls", "Appendix F, p.15; rounded manuscript values retained", bundle, manifest,
           "Output controls: residual exposure and benign utility")


def main():
    OUTPUT.mkdir(parents=True, exist_ok=True)
    configure_style()
    manifest = []
    charts = [
        ("rq1_methods", "method", "RQ1: mechanism comparison (hatched bars: single reference runs)", "Table 1, p.6"),
        ("controller_ablation", "condition", "Frozen-controller ablations", "Appendix E, p.14"),
        ("bounded_online", "method", "Bounded-online comparison", "Table 7, p.15"),
        ("dataset_shift", "dataset", "Frozen dataset-shift evaluation (150 trials each)", "Table 8, p.15"),
        ("trace_position", "position", "Trace-placement sensitivity", "Appendix F, p.15"),
        ("routing_stress", "router", "Frozen routing stress", "Table 8, p.15"),
        ("low_transfer_runs", "reported_run_index", "Low-transfer runs (seed identifiers not reported)", "Table 8, p.15"),
    ]
    with PdfPages(OUTPUT / "TRACE_all_figures.pdf") as bundle:
        for chart in charts:
            horizontal(*chart, bundle, manifest)
        for plot in (cross_backbone, acquisition_seeds, evolution, candidate_accounting, output_controls):
            plot(bundle, manifest)
        line_plot("context_length", "context_tokens", "vsr_percent", "Context length (tokens)",
                  "Frozen context-length sensitivity", "Appendix F, p.15", bundle, manifest)
        line_plot("local_rounds", "round", "cumulative_vsr_percent", "Interaction round",
                  "Local 200-trial cumulative curve", "Table 8, p.15", bundle, manifest)
    (OUTPUT / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"Rendered {len(manifest)} figures in PNG/PDF/SVG and a combined PDF.")


if __name__ == "__main__":
    main()
