"""Low-transfer repeat stability: descriptive pseudocode, not an executed clinical experiment."""

EXPERIMENT = {"title": "Low-transfer repeat stability", "source": "Table 8, p.15",
              "reported_results": "results/paper_reported/low_transfer_runs.csv"}

PSEUDOCODE = r'''
FOR reported_repeat IN [1, 2, 3, 4, 5]:
    LOAD the exact predeclared low-transfer condition and original run metadata
    EVALUATE without acquisition and record trial-level outcomes
    COMPUTE repeat-level VSR
REPORT the five percentages and their arithmetic mean
DO NOT assign acquisition seed IDs to these repeats without source metadata
ROUNDING NOTE: displayed percentages average to 24.66%; the text reports 24.67%
'''

if __name__ == "__main__":
    print(PSEUDOCODE)

