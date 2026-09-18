"""Bounded-online comparison: descriptive pseudocode, not an executed clinical experiment."""

EXPERIMENT = {"title": "Bounded-online comparison", "source": "Table 7, p.15",
              "reported_results": "results/paper_reported/bounded_online.csv"}

PSEUDOCODE = r'''
FOR method IN [static_one_shot, static_matched_budget, MEXTRA_style,
               iterative_multi_query, random_router, domain_no_feedback, TRACE]:
    budget = 1 IF method == static_one_shot ELSE 3
    RUN the declared method with matched samples and target settings
    ALLOW within-trial reference-method adaptation only as predeclared
    REQUIRE no TRACE repertoire acquisition or Q updates on evaluation targets
    REQUIRE 1 <= actual_executed_rounds <= budget
    SCORE using the same source-grounded verifier and visible-history exclusion
REPORT method-level VSR and all-trial AAR
NOTE operational reference prompts and complete method definitions are not supplied
'''

if __name__ == "__main__":
    print(PSEUDOCODE)

