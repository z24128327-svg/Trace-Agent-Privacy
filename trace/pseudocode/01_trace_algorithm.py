"""Method-level pseudocode. Running this file prints it; no experiments execute."""

PSEUDOCODE = r'''
ALGORITHM TRACE_ACQUIRE(seed_repertoire, initial_Q, D_evo, D_admit, D_shadow,
                        proposer, verifier, acquisition_protocol):
    REQUIRE disjoint trial IDs in D_evo, D_admit, D_shadow
    REQUIRE the same five-strategy initial repertoire across acquisition seeds
    REQUIRE no D_shadow or downstream-target feedback enters acquisition
    library = COPY(seed_repertoire)
    seed_ids = IDS(seed_repertoire)
    Q = COPY(initial_Q)
    history = []

    FOR generation IN 1..5:
        # Phase grouping follows Algorithm 1; hidden scheduling details are inputs.
        trajectories = EXECUTE_ACQUISITION(library, Q, D_evo,
                                           acquisition_protocol, verifier)
        experience = RECORD_VERIFIED_EXPERIENCE(trajectories)
        candidates = PROPOSE(library, experience, proposer, max_new_tokens=512)
        batch_seen = []
        accepted = []
        FOR candidate IN candidates:
            parent = CYCLIC_PARENT(library, generation, candidate.index,
                                    acquisition_protocol.proposal_budget)
            BIND_LINEAGE(candidate, exactly_one_parent=parent.id,
                         supporting_experience_ids, generator_call_id, text_hash)
            duplicate = LEXICAL_DUPLICATE(candidate, library + history + batch_seen, 0.92)
            batch_seen.APPEND(candidate)
            IF duplicate:
                RECORD(candidate, decision="duplicate")
                CONTINUE
            ENSURE_Q_ENTRIES(Q, candidate.id, acquisition_protocol.new_strategy_utility)
            # Same development trials, decoding and interaction budget on both arms.
            parent_trials = EVALUATE_FIXED_PROBE(parent, D_admit, verifier)
            child_trials = EVALUATE_FIXED_PROBE(candidate, D_admit, verifier)
            IF VSR(child_trials) > VSR(parent_trials):
                accepted.APPEND(candidate)
                RECORD(candidate, decision="admitted", paired_trial_ids)
            ELSE:
                RECORD(candidate, decision="rejected", paired_trial_ids)

        history.EXTEND(candidates)  # Include rejected and duplicate proposals.
        library = PRUNE(library + accepted, Q, protected_ids=seed_ids, capacity=10)
        Q = UPDATE_EMPIRICAL_UTILITY(Q, experience, alpha=0.2, gamma=0)
        SAVE_GENERATION_CHECKPOINT(library, Q, candidate_events, protocol_manifest)

    frozen = FREEZE_AND_HASH(library, Q)
    RETURN frozen  # Shadow and downstream evaluations happen after this boundary.

INVARIANTS:
    Verifier outcomes, not response labels, determine success and reward.
    All seed strategies remain protected; no strategy-complexity score is assumed.
    D_admit gains are development statistics, not independent test results.
    Target model weights are unchanged throughout acquisition and evaluation.
    Final generation/canonical run selection is predeclared, never based on shadow scores.
    New-action utility initialization is an explicit input; local development uses zero.
'''

if __name__ == "__main__":
    print(PSEUDOCODE)
