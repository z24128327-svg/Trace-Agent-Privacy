# Experiment Index

Each file contains a method-level procedure, the controlled comparison, required inputs, and the matching manuscript aggregate CSV. Invoking a file prints pseudocode only. No clinical execution is implied.

| Python file | Experiment | Result CSV |
| --- | --- | --- |
| [exp01_mechanism_comparison.py](exp01_mechanism_comparison.py) | Mechanism comparison | `rq1_methods.csv` |
| [exp02_seed_stability.py](exp02_seed_stability.py) | Five-seed held-out stability | `rq1_seeds.csv` |
| [exp03_evolution_dynamics.py](exp03_evolution_dynamics.py) | Representative acquisition trajectory | `evolution.csv` |
| [exp04_candidate_accounting.py](exp04_candidate_accounting.py) | Candidate lifecycle accounting | `candidates.csv` |
| [exp05_cross_backbone.py](exp05_cross_backbone.py) | Frozen cross-backbone transfer | `transfer.csv` |
| [exp06_controller_ablation.py](exp06_controller_ablation.py) | Frozen-controller ablation | `controller_ablation.csv` |
| [exp07_bounded_online.py](exp07_bounded_online.py) | Bounded-online comparison | `bounded_online.csv` |
| [exp08_dataset_shift.py](exp08_dataset_shift.py) | Frozen clinical dataset shift | `dataset_shift.csv` |
| [exp09_context_length.py](exp09_context_length.py) | Context-length sensitivity | `context_length.csv` |
| [exp10_trace_position.py](exp10_trace_position.py) | Trace-placement sensitivity | `trace_position.csv` |
| [exp11_routing_stress.py](exp11_routing_stress.py) | Frozen routing stress | `routing_stress.csv` |
| [exp12_low_transfer_stability.py](exp12_low_transfer_stability.py) | Low-transfer repeat stability | `low_transfer_runs.csv` |
| [exp13_round_budget.py](exp13_round_budget.py) | Cumulative local interaction curve | `local_rounds.csv` |
| [exp14_output_controls.py](exp14_output_controls.py) | Output controls and benign utility | `output_controls.csv` |

All CSV files are in `../results/paper_reported/`. Exact raw trial datasets, final frozen checkpoints, clinical verification, and some control implementations remain external requirements. Aggregate tables cannot recover them.
