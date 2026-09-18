"""Output controls and benign utility: descriptive pseudocode, not an executed clinical experiment."""

EXPERIMENT = {"title": "Output controls and benign utility", "source": "Appendix F, p.15",
              "reported_results": "results/paper_reported/output_controls.csv"}

PSEUDOCODE = r'''
FOR control IN [none, full_memory_partitioning, PCMU_provenance_gate]:
    APPLY the declared output/context control after strategy acquisition is finished
    KEEP the evaluator's protected source truth fixed for all exposure conditions
    RUN matched exposure trials with the same frozen probing policy
    RUN the separate held-out visible-only benign task suite
    RECORD residual exposure VSR and benign utility
FOR control:
    relative_loss = 100 * (utility_none - utility_control) / utility_none
REPORT exposure, retained utility and relative utility loss together
DO NOT count an empty protected-reference set as evidence of zero exposure
MISSING INTERFACES: complete PCMU gate and benign task suite are not included
'''

if __name__ == "__main__":
    print(PSEUDOCODE)

