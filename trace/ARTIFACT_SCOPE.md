# Artifact Scope and Evidence

| Component | Included | Status |
| --- | --- | --- |
| Overall acquisition and freeze mechanism | Eight pseudocode modules and a flow diagram | Method-level description |
| Fourteen experiment designs | One Python pseudocode file per experiment | Protocol description, not executed trials |
| Verifier decision rule | Pseudocode and a canonical-unit reference helper | Clinical entity extraction and synonym normalization are abstract inputs |
| State classifier, utility update, deduplication, admission, pruning | Small model-free reference functions with synthetic tests | Deterministic rule checks |
| Data schemas and examples | JSON Schema, dataset catalog, artificial fixture | No restricted source records |
| Aggregate results | Fourteen CSV files with manuscript source references | Transcribed reported values |
| Figures | Plotting source and PNG/PDF/SVG exports | Reconstructed from aggregates |
| Final clinical experiment code, trajectories and frozen artifacts | Not included | Required for full independent reproduction |

## Explicit Boundaries

- Five acquisition seeds are 7, 13, 21, 42 and 66. Low-transfer repeat seed IDs are not specified; their reported order is not a seed mapping.
- The paper specifies 100/100/100 disjoint trajectories. No claim of patient-level, template-level, or pretraining independence follows from trajectory disjointness.
- Five generations and a capacity of ten strategies are reported. Three proposals per generation are inferred from 75 proposals over five seeds and five generations and supported by the local development configuration; the inference is marked in the protocol.
- The initial surrogate and generator checkpoints, exact acquisition schedule, initial calibration, and complete decoding/model manifests are not specified sufficiently to reconstruct the original execution.
- Deduplication is lexical, not semantic. Composition can use several experience records but still records one designated parent.
- The main mechanism table combines four five-run means with two single-run reference methods. It is not a paired six-method significance test.
- The five displayed low-transfer percentages average to 24.66%; the manuscript reports 24.67%. The companion preserves the displayed measurements and documents the rounding discrepancy.
- Output controls are separate from strategy acquisition. Removing target-accessible memory must not remove protected ground truth from the evaluator.

This companion makes the methodological mechanism inspectable without claiming that pseudocode or synthetic checks reproduce the clinical results. Any manuscript code-availability statement should describe this artifact as pseudocode, aggregate data and plotting support while that remains its scope.
