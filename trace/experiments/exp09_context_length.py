"""Context-length sensitivity: descriptive pseudocode, not an executed clinical experiment."""

EXPERIMENT = {"title": "Context-length sensitivity", "source": "Appendix F, p.15",
              "reported_results": "results/paper_reported/context_length.csv"}

PSEUDOCODE = r'''
FOR token_budget IN [4000, 16000, 25000, 64000]:
    CONSTRUCT context under the declared tokenizer and truncation policy
    KEEP matched queries, protected ground truth, target decoding and frozen policy
    COUNT the actual prompt tokens; do not substitute a character approximation
    EVALUATE without acquisition or utility updates
    RECORD token budget, actual token counts, VSR and AAR
PLOT VSR at the actual numerical context lengths
NOTE the full context-construction procedure is an external protocol input
'''

if __name__ == "__main__":
    print(PSEUDOCODE)

