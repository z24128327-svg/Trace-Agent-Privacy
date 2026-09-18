"""Mechanism comparison: descriptive pseudocode, not an executed clinical experiment."""

EXPERIMENT = {"title": "Mechanism comparison", "source": "Table 1, p.6",
              "reported_results": "results/paper_reported/rq1_methods.csv"}

PSEUDOCODE = r'''
FOR method IN [fixed, Q_only, unguided, TRACE]:
    FOR seed IN [7, 13, 21, 42, 66]:
        RESET identical seed repertoire and declared initial utility
        ACQUIRE with the selected mechanism using only D_evo and D_admit
        FREEZE acquired objects before evaluating the 100 D_shadow trials
        RECORD per-seed VSR and all-trial AAR
    REPORT arithmetic mean of five seed-level VSRs
EVALUATE one separately identified Reflexion-style reference run
EVALUATE one separately identified Self-Harness-style reference run
DO NOT pool multiple reference runs while labeling the result a single run
DO NOT treat this mixed table as a paired six-method significance test
CONTROL OBJECTS:
    fixed: unchanged seed repertoire and prescribed fixed selection
    Q_only: learn router while holding seed strategies fixed
    unguided: candidate generation without structured verified experience
    TRACE: verified-experience-guided generation plus router
    Reflexion: bounded reflection memory, with no new probing repertoire
    Self-Harness: one propose-validate-accept interaction harness
'''

if __name__ == "__main__":
    print(PSEUDOCODE)

