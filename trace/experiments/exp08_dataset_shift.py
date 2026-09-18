"""Frozen clinical dataset shift: descriptive pseudocode, not an executed clinical experiment."""

EXPERIMENT = {"title": "Frozen clinical dataset shift", "source": "Table 8, p.15",
              "reported_results": "results/paper_reported/dataset_shift.csv"}

PSEUDOCODE = r'''
LOAD the same frozen repertoire and corresponding router used for transfer
FOR dataset IN [MIMIC-IV, eICU, MIMIC-CXR]:
    LOAD 150 authorized trial manifests and fixed protected source units
    REQUIRE no records from this dataset were used for generation or admission
    EVALUATE without utility updates or repertoire changes
    RECORD VSR, executed-round diagnostics, data manifest and frozen hashes
REPORT each dataset separately
DO NOT replace missing restricted records with a different dataset or generated patients
'''

if __name__ == "__main__":
    print(PSEUDOCODE)

