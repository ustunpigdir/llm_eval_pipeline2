# BERTScore Structured All-32 Phase-1-Hardened Report

## Scope

- Run name: `structured_prompt_all32_phase1_hardened_v1`
- Source: saved structured-prompt V2-V5 outputs only
- Rows scored: CLEAN rows only
- Reference source: worked_solutions_batch1.md through worked_solutions_batch7.md
- Rescale with baseline: True
- BERTScore model hash: unknown

## Validation

- CLEAN rows scored: 252
- REVIEW rows scored: 0
- Scenarios represented: 32
- Batches represented: V2, V3, V4, V5
- Deterministic PASS/FAIL: PASS=117, FAIL=135
- learning.db modified: false
- raw outputs modified: false
- model/LLM API calls made: false

## Overall

- Mean F1: 0.503559
- Median F1: 0.632473
- Min F1: -0.381666
- Max F1: 0.774753

## By Deterministic Grade

| grade | n_rows | mean_f1 | median_f1 | min_f1 | max_f1 |
| --- | ---: | ---: | ---: | ---: | ---: |
| FAIL | 135 | 0.489969 | 0.614170 | -0.381666 | 0.774753 |
| PASS | 117 | 0.519239 | 0.652349 | -0.194096 | 0.768946 |

## By Batch

| batch | n_rows | PASS | FAIL | mean_f1 | median_f1 |
| --- | ---: | ---: | ---: | ---: | ---: |
| V2 | 64 | 37 | 27 | 0.490934 | 0.639926 |
| V3 | 61 | 24 | 37 | 0.501700 | 0.604600 |
| V4 | 63 | 19 | 44 | 0.483810 | 0.653061 |
| V5 | 64 | 37 | 27 | 0.537395 | 0.703205 |

## Lowest Scenario Mean F1

| scenario_id | n_rows | mean_f1 |
| --- | ---: | ---: |
| COS_DESITTER_001 | 8 | 0.219557 |
| GR_GPS_001 | 8 | 0.344388 |
| GR_ISCO_001 | 8 | 0.357902 |
| QFT_G2_001 | 8 | 0.392601 |
| GR_PERI_001 | 8 | 0.418488 |

## Highest Scenario Mean F1

| scenario_id | n_rows | mean_f1 |
| --- | ---: | ---: |
| QFT_YUKAWA_001 | 8 | 0.611776 |
| QM_BERRY_001 | 8 | 0.598842 |
| QI_TELEPORT_001 | 8 | 0.595567 |
| SR_TWIN_001 | 8 | 0.588029 |
| QM_AB_001 | 8 | 0.581669 |

## Baseline Context

- Previous baseline rows: 617
- Previous baseline mean F1: -0.163535
- Structured mean F1 minus previous baseline mean F1: 0.667093
- Comparison is aggregate only; no unsafe row-level alignment was performed.

## Outputs

- `bertscore_structured_all32_phase1_hardened.csv`
- `bertscore_structured_all32_phase1_hardened.json`
- `bertscore_structured_all32_phase1_hardened_by_batch.csv`
- `bertscore_structured_all32_phase1_hardened_by_scenario.csv`
- `bertscore_structured_all32_phase1_hardened_by_model.csv`
- `bertscore_structured_all32_phase1_hardened_by_grade.csv`
- `bertscore_structured_vs_original_baseline_summary.csv`
- `manifest.json`
