from types import SimpleNamespace
import unittest

from classify_remaining_layer1b_flags import extract_field_value
from extract_final_answers import field_pairs
from normalizer import normalize_answer
from symbolic_eval import eval_value


def extraction_status(helper_status, values, gold_rows):
    extracted_field_names = set(values)
    gold_field_names = {row.field_name for row in gold_rows}
    if helper_status == "OK" and len(values) == len(gold_rows) and extracted_field_names == gold_field_names:
        return "OK"
    if helper_status == "OK":
        return "FIELD_SET_MISMATCH"
    return helper_status


class Phase1ExtractorFixTests(unittest.TestCase):
    def assertFloatValue(self, raw, expected, tol=1e-12):
        value, note = eval_value(raw)
        self.assertIn(note, {"numeric", "symbolic"})
        self.assertAlmostEqual(value, expected, delta=max(abs(expected) * tol, tol))

    def test_unit_exponent_stripping_preserves_numeric_magnitude(self):
        self.assertFloatValue(r"3.9 \times 10^{-5} \text{ μJ/m}^2", 3.9e-5)
        self.assertFloatValue(r"5.1 \times 10^{6} \text{ m}^{2}", 5.1e6)
        self.assertFloatValue(r"1.56 \times 10^{-4} \text{ Pa}", 1.56e-4)
        self.assertFloatValue(r"10^{-5}", 1e-5)


    def test_orphan_exponent_is_not_silently_evaluated(self):
        value, note = eval_value(r"^2")
        self.assertIsNone(value)
        self.assertEqual(note, "orphan-exponent-operator")


    def test_operator_prefixes_are_stripped_longest_first(self):
        self.assertEqual(extract_field_value(r"\simeq 3.2"), "3.2")
        self.assertEqual(extract_field_value(r"\approxeq 5.2"), "5.2")
        self.assertEqual(extract_field_value(r"\approx 4.1"), "4.1")
        self.assertEqual(extract_field_value(r"= 7.0"), "7.0")


    def test_field_pairs_accept_operator_variants(self):
        block = r"""
        \begin{aligned}
        \mathrm{x} &\simeq 3.2 \\
        \mathrm{y} &\approxeq 5.2 \\
        \mathrm{z} &\approx 4.1 \\
        \mathrm{w} &= 7.0 \\
        \end{aligned}
        """
        pairs = list(field_pairs(block))
        self.assertEqual(
            [(name, value) for _, name, value in pairs],
            [
                ("x", "3.2"),
                ("y", "5.2"),
                ("z", "4.1"),
                ("w", "7.0"),
            ],
        )


    def test_normalize_answer_none_empty_whitespace(self):
        self.assertEqual(normalize_answer(None), "")
        self.assertEqual(normalize_answer(""), "")
        self.assertEqual(normalize_answer("  a\n b "), "a b")


    def test_field_set_mismatch_status_for_ok_helper(self):
        gold = [SimpleNamespace(field_name=name) for name in ("a", "b", "c")]
        self.assertEqual(extraction_status("OK", {"a": "1", "b": "2"}, gold), "FIELD_SET_MISMATCH")
        self.assertEqual(extraction_status("OK", {"a": "1", "b": "2", "c": "3"}, gold), "OK")
        self.assertEqual(extraction_status("NO_VALID_BLOCK", {}, gold), "NO_VALID_BLOCK")


if __name__ == "__main__":
    unittest.main()
