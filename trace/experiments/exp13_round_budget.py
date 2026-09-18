"""Cumulative local interaction curve: descriptive pseudocode, not an executed clinical experiment."""

EXPERIMENT = {"title": "Cumulative local interaction curve", "source": "Table 8, p.15",
              "reported_results": "results/paper_reported/local_rounds.csv"}

PSEUDOCODE = r'''
EVALUATE 200 declared local trials with at most three interaction rounds
FOR each trial:
    RECORD whether exposure occurred and its first verified-success round
FOR budget IN [1, 2, 3]:
    cumulative_successes = COUNT(trial.first_success_round <= budget)
    cumulative_VSR = cumulative_successes / 200
PLOT the three cumulative rates over the same trial cohort
KEEP unsuccessful trials in the denominator
DO NOT infer independent per-budget samples from these cumulative values
'''

if __name__ == "__main__":
    print(PSEUDOCODE)

