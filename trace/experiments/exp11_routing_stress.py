"""Frozen routing stress: descriptive pseudocode, not an executed clinical experiment."""

EXPERIMENT = {"title": "Frozen routing stress", "source": "Table 8, p.15",
              "reported_results": "results/paper_reported/routing_stress.csv"}

PSEUDOCODE = r'''
FOR selector IN [learned_TRACE, random, low_transfer]:
    LOAD the declared strategy pool and selector policy for this stress condition
    REQUIRE the stress construction is fixed before evaluating outcomes
    EVALUATE matched samples with no strategy acquisition or utility updates
    RECORD selector identity, pool hash, random seed, verified outcomes and rounds
COMPARE the three VSRs
MISSING INTERFACE: exact low-transfer pool/selector construction is not specified;
do not choose it by searching the evaluation set for low scores
'''

if __name__ == "__main__":
    print(PSEUDOCODE)

