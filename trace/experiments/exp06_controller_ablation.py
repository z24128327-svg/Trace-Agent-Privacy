"""Frozen-controller ablation: descriptive pseudocode, not an executed clinical experiment."""

EXPERIMENT = {"title": "Frozen-controller ablation", "source": "Appendix E, p.14",
              "reported_results": "results/paper_reported/controller_ablation.csv"}

PSEUDOCODE = r'''
LOAD the learned repertoire and declared frozen controller
FOR condition IN [full, without_response_diagnosis, without_calibrated_reweighting,
                  random_router, without_positional_guidance, single_turn]:
    APPLY the exact predeclared controller alteration for that condition
    EVALUATE matched sample IDs without acquiring new strategies or updating Q
    USE one interaction turn in the single-turn condition
    RECORD verified exposure and actual executed rounds
COMPARE descriptive VSR values against the unchanged controller
MISSING INTERFACE: exact reweighting and positional-guidance implementations
remain protocol inputs; changing a condition label is not an implementation
'''

if __name__ == "__main__":
    print(PSEUDOCODE)

