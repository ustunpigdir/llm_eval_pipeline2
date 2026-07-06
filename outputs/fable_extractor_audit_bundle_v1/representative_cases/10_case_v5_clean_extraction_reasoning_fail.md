# Clean extraction but genuine reasoning/calculation failure

- case_id: `case_v5_clean_extraction_reasoning_fail`
- scenario_id: `GR_CHIRP_001`
- model_name: `Gemma 3 12B IT`
- source_batch: `structured_prompt_pilot_v5`
- helper_status: `OK`
- deterministic_grade: `FAIL`
- why_included: Demonstrates CLEAN extraction does not imply correctness; autograder catches numeric mismatch.
- source_paths: outputs/structured_prompt_pilot_v5/autograde_no_bert_v1/structured_prompt_v5_clean_autograde.json

## Raw Final-Answer / Evidence Excerpt

```text
the combination 𝓜; the individual masses / mass ratio enter only at higher post-Newtonian order. So a leading-order chirp measures **𝓜**, not the total mass.

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{chirp\_mass\_msun} &= 53.8 \\
\mathrm{each\_mass\_msun}  &= 61.7 \\
\mathrm{total\_mass\_msun} &= 123.4 \\
\end{aligned}
\]
```

## Extracted Fields

```json
[
  {
    "field": "chirp_mass_msun",
    "raw_value": "53.8"
  },
  {
    "field": "each_mass_msun",
    "raw_value": "61.7"
  },
  {
    "field": "total_mass_msun",
    "raw_value": "123.4"
  }
]
```

## Expected / Gold Fields

```json
[
  {
    "field_index": 0,
    "field_name": "chirp_mass_msun",
    "expected_value_raw": "28.0"
  },
  {
    "field_index": 1,
    "field_name": "each_mass_msun",
    "expected_value_raw": "32.163554"
  },
  {
    "field_index": 2,
    "field_name": "total_mass_msun",
    "expected_value_raw": "64.327108"
  }
]
```
