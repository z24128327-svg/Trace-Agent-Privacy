"""Lexical novelty, strict development admission, and bounded seed-protected storage."""

PSEUDOCODE = r'''
NORMALIZE_STRATEGY(text) = LOWERCASE(REGEX_REMOVE(r"\W+", text))

PROCEDURE LEXICAL_DUPLICATE(candidate, comparison_pool, threshold=0.92):
    normalized = NORMALIZE_STRATEGY(candidate.text)
    IF normalized IS EMPTY: RETURN True
    FOR previous IN comparison_pool:
        other = NORMALIZE_STRATEGY(previous.text)
        IF normalized == other OR SEQUENCE_MATCHER(normalized, other) >= threshold:
            RETURN True
    RETURN False

PROCEDURE ADMIT(parent_trials, child_trials):
    REQUIRE identical nonempty trial-ID sets and matched interaction conditions
    RETURN VSR(child_trials) > VSR(parent_trials)  # Strict inequality, no AAR term.

PROCEDURE PRUNE(library, Q, protected_ids, capacity=10):
    REQUIRE capacity >= SIZE(protected_ids)
    REQUIRE Q entries exist for every state and strategy, including new candidates
    seeds = [strategy FOR strategy IN library IF strategy.id IN protected_ids]
    nonseeds = [strategy FOR strategy IN library IF strategy.id NOT IN protected_ids]
    ranked = STABLE_SORT(nonseeds, descending=MAX_OVER_STATES(Q[state, strategy.id]))
    keep = IDS(seeds) UNION IDS(ranked[:capacity - LENGTH(seeds)])
    RECORD_PRUNE_EVENTS(IDS(library) - keep)
    RETURN [strategy FOR strategy IN library IF strategy.id IN keep]

TIES:
    Pruning preserves existing library order; routing uses ascending strategy IDs.
    There is no separately evaluated semantic-equivalence or complexity threshold.
'''

if __name__ == "__main__":
    print(PSEUDOCODE)
