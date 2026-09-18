"""Candidate lifecycle accounting: descriptive pseudocode, not an executed clinical experiment."""

EXPERIMENT = {"title": "Candidate lifecycle accounting", "source": "Appendix C, p.13",
              "reported_results": "results/paper_reported/candidates.csv"}

PSEUDOCODE = r'''
READ candidate events for five seeds and five acquisition generations
REQUIRE each candidate ID is unique within its acquisition run
COUNT generated candidates, lexical duplicates, and evaluated candidates
COUNT strict parent-relative admissions and rejected evaluated candidates
COUNT later pruning events only for previously admitted candidates
REQUIRE generated = duplicates + evaluated
REQUIRE evaluated = admitted + rejected
REPORT aggregate counts, not an invented candidate-by-candidate history
MANUSCRIPT TOTALS: 75 generated; 9 duplicates; 66 evaluated; 24 admitted;
                   42 rejected; 4 later pruned
'''

if __name__ == "__main__":
    print(PSEUDOCODE)

