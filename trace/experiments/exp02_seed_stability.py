"""Five-seed held-out stability: descriptive pseudocode, not an executed clinical experiment."""

EXPERIMENT = {"title": "Five-seed held-out stability", "source": "Table 4, p.14",
              "reported_results": "results/paper_reported/rq1_seeds.csv"}

PSEUDOCODE = r'''
FOR seed IN [7, 13, 21, 42, 66]:
    FOR core_method IN [fixed, Q_only, unguided, TRACE]:
        RUN independently seeded acquisition with matched initial conditions
        FREEZE then SCORE the same declared 100-trial shadow split
        STORE method, seed, successes, trial_count, VSR, AAR
REQUIRE one complete cell for every method-seed combination
REPORT each seed separately and average seed statistics with equal weights
DO NOT select the best seed by its shadow result
'''

if __name__ == "__main__":
    print(PSEUDOCODE)

