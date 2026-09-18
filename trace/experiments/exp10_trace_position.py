"""Trace-placement sensitivity: descriptive pseudocode, not an executed clinical experiment."""

EXPERIMENT = {"title": "Trace-placement sensitivity", "source": "Appendix F, p.15",
              "reported_results": "results/paper_reported/trace_position.csv"}

PSEUDOCODE = r'''
FOR placement IN [head, middle, tail]:
    PLACE the same retained memory block at the selected prompt position
    KEEP queries, retrieval, context budget, target model and frozen policy matched
    ENSURE truncation does not silently change the intended protected-memory condition
    EVALUATE the same trial IDs with no strategy or utility updates
    RECORD placement, exact prompt/context metadata, VSR and AAR
COMPARE matched placement conditions; do not retrain the router
'''

if __name__ == "__main__":
    print(PSEUDOCODE)

