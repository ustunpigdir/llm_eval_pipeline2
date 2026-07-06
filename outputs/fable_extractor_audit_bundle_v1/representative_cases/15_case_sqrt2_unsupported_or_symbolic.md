# STAT_ISING sqrt2 shorthand / symbolic expression boundary

- case_id: `case_sqrt2_unsupported_or_symbolic`
- scenario_id: `STAT_ISING_001`
- model_name: `Gemma/Llama examples`
- source_batch: `official_baseline`
- helper_status: `OK`
- deterministic_grade: `MATCH or UNSUPPORTED depending layer`
- why_included: Covers unsupported-expression versus parser-bug boundary and symbolic equivalence risk.
- source_paths: final_answer_values_review.csv, grade_results_sample.csv

## Raw Final-Answer / Evidence Excerpt

```text
final_answer_values_review.csv classified expressions like 2/\ln(1+\sqrt2) as UNSUPPORTED; later grade_results_sample shows symbolic handling can match when safely evaluated.
```

## Extracted Fields

```json
[
  {
    "field": "tc_exact",
    "raw_value": "2/\\ln(1+\\sqrt2)"
  },
  {
    "field": "ratio_exact_mf",
    "raw_value": "\\frac{1}{2\\ln(1+\\sqrt2)}"
  }
]
```

## Expected / Gold Fields

```json
[
  {
    "field_index": 0,
    "field_name": "ratio_exact_mf",
    "expected_value_raw": "0.567296"
  },
  {
    "field_index": 1,
    "field_name": "tc_exact",
    "expected_value_raw": "2.269185"
  },
  {
    "field_index": 2,
    "field_name": "tc_meanfield",
    "expected_value_raw": "4.0"
  }
]
```
