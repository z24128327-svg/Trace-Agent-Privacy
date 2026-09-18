"""Frozen acquisition outputs and a bounded, response-conditioned downstream loop."""

PSEUDOCODE = r'''
PROCEDURE FREEZE_AND_HASH(library, Q):
    RETURN IMMUTABLE_SNAPSHOT(library, Q, library_hash=SHA256(library),
                              router_hash=SHA256(Q), acquisition_manifest)

PROCEDURE FROZEN_TRIAL(snapshot, trial, target_agent, verifier, round_budget):
    before = HASH(snapshot)
    state = initial
    visible_history = []
    verified_units = []
    executed_rounds = 0
    FOR turn IN 1..round_budget:
        strategy = SELECT_STRATEGY(snapshot.Q, state, snapshot.library)
        query = INSTANTIATE(strategy, trial.visible_task, observed_response_history)
        visible_history.APPEND(query)
        response = target_agent.INTERACT(query, trial.target_accessible_context)
        outcome = VERIFY_RESPONSE(response, visible_history, trial.protected_units, verifier)
        executed_rounds += 1
        RECORD(turn, strategy.id, response, outcome, actual_token_counts, errors)
        verified_units.EXTEND(outcome.verified_units)
        IF outcome.success: BREAK
        state = CLASSIFY(response)
    REQUIRE HASH(snapshot) == before
    REQUIRE strategy_generation_count == library_update_count == q_update_count == 0
    RETURN {success: LENGTH(verified_units) > 0, rounds: executed_rounds,
            first_success_round, trial_id, library_hash, router_hash}

EVALUATION BOUNDARY:
    Classification and choosing an existing strategy remain allowed.
    Generation, admission, pruning, utility updates and target-feedback selection are forbidden.
    Use the same frozen hashes across backbones and dataset-shift conditions.
    Run-level selection must not use downstream or shadow feedback.
'''

if __name__ == "__main__":
    print(PSEUDOCODE)
