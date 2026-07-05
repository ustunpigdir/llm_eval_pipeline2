# Usable-Only Analysis Views Report

## Purpose

This change adds read-only SQLite views for analyzing the official benchmark after excluding runs marked structurally unusable in `run_quality_status`. The original benchmark and grading tables remain preserved for all-results analysis.

## Views Added

- `official_usable_gradeable_runs`: official gradeable runs with `usability_status = 'USABLE'`.
- `usable_grading_results`: grading rows for runs with `usability_status = 'USABLE'`.
- `usable_grading_summary_overall`: usable-only verdict counts and match rates.
- `usable_grading_summary_by_model`: usable-only verdict counts and match rates by model.
- `usable_grading_summary_by_scenario`: usable-only verdict counts and match rates by scenario, including scenario title when available.
- `unusable_official_runs`: official gradeable runs marked unusable, with quality status and review rationale.

## Verification Counts

- `official_gradeable_runs`: 624
- `official_usable_gradeable_runs`: 617
- `unusable_official_runs`: 7
- `grading_results`: 1,861
- `usable_grading_results`: 1,839

Consistency check: `624 = 617 + 7`.

## All-Results Verdict Distribution

- `MATCH`: 1,012
- `MISMATCH`: 742
- `NOT_FOUND`: 63
- `REVIEW`: 44

## Usable-Only Verdict Distribution

- `MATCH`: 1,012
- `MISMATCH`: 742
- `NOT_FOUND`: 41
- `REVIEW`: 44

## Unusable Official Runs

| run_id | model_name | scenario_id | quality_status | source_artifact |
| --- | --- | --- | --- | --- |
| 185 | Llama 3.1 8B Instruct | GR_CHIRP_001 | UNUSABLE | remaining_layer1b_flag_classification_v3.csv |
| 187 | Ministral 3 8B | GR_CHIRP_001 | UNUSABLE | remaining_layer1b_flag_classification_v3.csv |
| 188 | Ministral 3 8B | GR_CHIRP_001 | UNUSABLE | remaining_layer1b_flag_classification_v3.csv |
| 256 | NVIDIA Nemotron 3 Nano 30B-A3B | GR_PERI_001 | UNUSABLE | remaining_layer1b_flag_classification_v3.csv |
| 286 | Llama 3.1 8B Instruct | QFT_CASIMIR_001 | UNUSABLE | remaining_layer1b_flag_classification_v3.csv |
| 380 | Ministral 3 8B | QI_CLONE_001 | UNUSABLE | remaining_layer1b_flag_classification_v3.csv |
| 514 | Gemma 3 12B IT | QM_TUNNEL_001 | UNUSABLE | remaining_layer1b_flag_classification_v3.csv |

## Preservation

The source tables `grading_results`, `official_gradeable_runs`, and `run_quality_status` are preserved unchanged. The new objects are read-only views layered on top of existing data.

## Remaining Limitation

These views exclude structurally unusable runs, but they do not yet apply human review overrides because `review_overrides` is intentionally empty.
