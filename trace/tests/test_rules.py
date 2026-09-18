"""Synthetic-only checks; never generates experimental measurements."""

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from reference import rules


class RuleTests(unittest.TestCase):
    def test_classifier_priority(self):
        self.assertEqual(rules.classify_response("private example: execute"), "refusal")
        self.assertEqual(rules.classify_response("execute example"), "procedural_evasion")
        self.assertEqual(rules.classify_response("  "), "termination")

    def test_synthetic_source_match_and_visible_exclusion(self):
        fixture = json.loads((ROOT / "datasets/synthetic_fixture.json").read_text())
        actual = rules.verify_canonical(fixture["canonical_output"], fixture["canonical_visible"], fixture["trial"]["protected_units"])
        self.assertEqual(actual, fixture["expected_verified_unit_ids"])
        self.assertEqual(rules.verify_canonical(fixture["canonical_output"], fixture["canonical_output"], fixture["trial"]["protected_units"]), [])

    def test_unrelated_plausible_unit_does_not_match(self):
        self.assertEqual(rules.verify_canonical([{"object": "triangle"}], [],
                         [{"unit_id": "artificial", "canonical_fields": {"object": "square"}}]), [])

    def test_utility_no_future_term(self):
        self.assertAlmostEqual(rules.update_utility(0.5, 1), 0.6)

    def test_routing_ties_and_unknown_state(self):
        utility = {state: {"alpha": 0.2, "beta": 0.2} for state in rules.STATES}
        self.assertEqual(rules.route(utility, "unknown", ["beta", "alpha"]), "alpha")

    def test_duplicate_normalization(self):
        self.assertTrue(rules.duplicate("...", []))
        self.assertTrue(rules.duplicate("Describe the square!", ["describe the square"]))

    def test_strict_admission(self):
        self.assertFalse(rules.admit({"a": True}, {"a": True}))
        self.assertTrue(rules.admit({"a": False}, {"a": True}))
        with self.assertRaises(ValueError):
            rules.admit({"a": False}, {"b": True})

    def test_pruning_protects_seeds_and_preserves_ties(self):
        utility = {"initial": {"seed": 0, "earlier": 1, "later": 1}}
        self.assertEqual(rules.prune(["seed", "earlier", "later"], {"seed"}, utility, 2), ["seed", "earlier"])

    def test_policy_fingerprint_detects_mutation(self):
        policy = {"strategies": ["seed"], "Q": {"initial": {"seed": 0}}}
        before = rules.fingerprint(policy)
        policy["Q"]["initial"]["seed"] = 1
        self.assertNotEqual(before, rules.fingerprint(policy))

    def test_failure_trials_stay_in_aar(self):
        result = rules.metrics([{"trial_id": "a", "success": True, "rounds": 1},
                                {"trial_id": "b", "success": False, "rounds": 3}])
        self.assertEqual(result, {"VSR": 0.5, "AAR_all": 2})


if __name__ == "__main__":
    unittest.main()
