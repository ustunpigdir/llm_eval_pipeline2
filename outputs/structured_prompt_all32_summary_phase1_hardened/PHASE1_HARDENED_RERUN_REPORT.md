# Phase 1 Hardened Structured Prompt Rerun Report

- created_at: 2026-07-05T21:39:31+00:00
- source: saved outputs only
- external_api_calls: false
- model_runners_executed: false
- BERTScore_status: not run
- learning_db_modified: false
- raw_outputs_modified: false

## Combined Post-Phase-1 Summary

- total_structured_runs: 264
- total_CLEAN_rows: 252
- total_REVIEW_rows: 12
- PASS: 117
- FAIL: 135
- overall_pass_rate_across_clean_rows: 0.464286
- extraction_status_distribution: {"OK": 252}
- stability_decision: STABLE_NO_METRIC_CHANGE

## Comparison To Pre-Phase-1 Known Summary

- pre_total_structured_runs: 264
- pre_total_CLEAN_rows: 252
- pre_total_REVIEW_rows: 12
- pre_PASS: 117
- pre_FAIL: 135
- pre_overall_pass_rate: 0.464286
- metric_changed: false
- changed_rows_count: 0

## Batch Summary

| batch | total_runs | CLEAN | REVIEW | PASS | FAIL | pass_rate | extraction_status_distribution | changed_rows_count |
|---|---:|---:|---:|---:|---:|---:|---|---:|
| V2 | 72 | 64 | 8 | 37 | 27 | 0.578125 | `{"OK": 64}` | 0 |
| V3 | 64 | 61 | 3 | 24 | 37 | 0.393443 | `{"OK": 61}` | 0 |
| V4 | 64 | 63 | 1 | 19 | 44 | 0.301587 | `{"OK": 63}` | 0 |
| V5 | 64 | 64 | 0 | 37 | 27 | 0.578125 | `{"OK": 64}` | 0 |

## Scenario Extremes

- scenarios_with_0_percent_pass: GR_CHIRP_001, GR_GPS_001, GR_ISCO_001, STAT_BEC_001
- scenarios_with_100_percent_pass: QI_CLONE_001, QM_BERRY_001, SR_BELL_001, SR_FIZEAU_001

## Model Ranking By Pass Rate

- Mistral NeMo 12B: 0.125 (4/32)
- Llama 3.1 8B Instruct: 0.322581 (10/31)
- Ministral 3 8B: 0.375 (12/32)
- Mistral Small 3.2 24B Instruct: 0.4375 (14/32)
- Gemma 3 12B IT: 0.46875 (15/32)
- Gemma 3 27B IT: 0.5 (16/32)
- Granite 4.1 8B: 0.655172 (19/29)
- Gemma 4 31B IT: 0.84375 (27/32)

## Changed Rows

- none

## Safety Validation

- no external API calls made
- no model runner executed
- no raw model output files modified
- learning.db not modified
- BERTScore not run
- Phase 2 semantics not implemented
- NOT_GRADEABLE not added
- LLM judge not used
