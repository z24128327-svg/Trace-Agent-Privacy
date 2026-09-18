# Data Interfaces

This review artifact includes schemas and artificial examples only. No original clinical record, patient-linked memory, private tool trace, credentials, or institution-specific paths are distributed.

| Dataset | Role | Reported trial scope | Raw records in this artifact |
| --- | --- | --- | --- |
| MIMIC-III | Acquisition and held-out evaluation | 100 evolution / 100 admission / 100 shadow trajectories | No |
| MIMIC-IV | Frozen dataset shift | 150 | No |
| eICU | Frozen dataset shift | 150 | No |
| MIMIC-CXR | Frozen dataset shift | 150 | No |
| Visible-only benign suite | Output-control utility | Count not specified | No |

Obtain clinical datasets through their official providers under the applicable access requirements. A prepared question subset is not equivalent to the complete database or the exact final experiment split. A separate historical RAP task is not part of these paper clinical dataset-shift experiments.

`trial.schema.json` describes the minimum trial manifest. `synthetic_fixture.json` illustrates source matching and visible-query exclusion using colored-object identifiers. Its values are invented solely for deterministic software checks; they are not generated patients or experimental measurements. Canonical unit fields are only a serialization contract, not a clinical ontology or implemented normalizer.

Required provenance for real reproduction includes immutable dataset version and split IDs, protected-source-unit annotations, visible query history, retrieval/context configuration, model/decoding revisions, and the frozen repertoire/router hashes. This companion does not fabricate missing provenance.
