# Degree notation/unit-wrapper accepted in official grade sample

- case_id: `case_degree_notation_units`
- scenario_id: `CM_APSIDAL_001`
- model_name: `Gemma 4 31B IT`
- source_batch: `official_baseline`
- helper_status: `OK`
- deterministic_grade: `MATCH`
- why_included: Covers degree notation / unit-wrapper normalization risk.
- source_paths: official_grade.csv

## Raw Final-Answer / Evidence Excerpt

```text
official_grade.csv rows show values like 90^\circ, 127.28^\circ matched numerically.
```

## Extracted Fields

```json
[
  {
    "field": "apsidal_harmonic_deg",
    "raw_value": "90^\\circ"
  },
  {
    "field": "apsidal_n_minus1_deg",
    "raw_value": "127.28^\\circ"
  }
]
```

## Expected / Gold Fields

```json
[
  {
    "field_index": 0,
    "field_name": "apsidal_harmonic_deg",
    "expected_value_raw": "90.0"
  },
  {
    "field_index": 1,
    "field_name": "apsidal_kepler_deg",
    "expected_value_raw": "180.0"
  },
  {
    "field_index": 2,
    "field_name": "apsidal_n_minus1_deg",
    "expected_value_raw": "127.279221"
  },
  {
    "field_index": 3,
    "field_name": "precession_per_period_deg",
    "expected_value_raw": "-105.441559"
  }
]
```
