"""Per-turn experience with correct attribution to the strategy actually executed."""

PSEUDOCODE = r'''
PROCEDURE RECORD_VERIFIED_EXPERIENCE(completed_evolution_trajectories):
    REQUIRE every trajectory originates from D_evo
    records = []
    FOR trajectory IN completed_evolution_trajectories:
        input_state = initial
        FOR turn IN trajectory.turns IN EXECUTION_ORDER:
            records.APPEND({
                experience_id: STABLE_ID(trajectory.id, turn.index),
                input_state: input_state,
                response_state: CLASSIFY(turn.response),
                executed_strategy_id: turn.strategy_id,
                verifier_reward: turn.verification.reward,
                verified_unit_count: LENGTH(turn.verification.verified_units),
                diagnostic: OBSERVED_DIAGNOSTIC(turn),
                context: {turn.index, trace_position, context_budget},
                response_evidence: STRUCTURAL_WHITELIST(turn.response)
            })
            input_state = CLASSIFY(turn.response)
    RETURN records

PROPOSER VIEW:
    Sample bounded evidence from successes and failures across states and strategies.
    Use source-verifier labels and observable structural diagnostics.
    Do not include private source answers in candidate instructions.
    A generated explanation remains an unverified hypothesis until candidate evaluation.
    Never attribute an entire trajectory's reward to its last strategy by default.
'''

if __name__ == "__main__":
    print(PSEUDOCODE)
