# Structured Prompt All32 Summary

- total_structured_runs: 264
- total_CLEAN_rows: 252
- total_REVIEW_rows: 12
- pass_count: 117
- fail_count: 135
- overall_pass_rate_across_clean_rows: 0.464286
- BERTScore_status: not run

## Pass Rate By Batch

| batch | total_runs | clean_rows | review_rows | pass_count | fail_count | pass_rate |
|---|---:|---:|---:|---:|---:|---:|
| V2 | 72 | 64 | 8 | 37 | 27 | 0.578125 |
| V3 | 64 | 61 | 3 | 24 | 37 | 0.393443 |
| V4 | 64 | 63 | 1 | 19 | 44 | 0.301587 |
| V5 | 64 | 64 | 0 | 37 | 27 | 0.578125 |

## Scenario Extremes

- scenarios_with_0_percent_pass: GR_CHIRP_001, GR_GPS_001, GR_ISCO_001, STAT_BEC_001
- scenarios_with_100_percent_pass: QI_CLONE_001, QM_BERRY_001, SR_BELL_001, SR_FIZEAU_001

## Model Extremes

- lowest_pass_rate_models: Mistral NeMo 12B (0.125); Llama 3.1 8B Instruct (0.322581); Ministral 3 8B (0.375)
- highest_pass_rate_models: Gemma 4 31B IT (0.84375); Granite 4.1 8B (0.655172); Gemma 3 27B IT (0.5)

## Pass Rate By Scenario

- CM_APSIDAL_001: 0.375 (3/8)
- CM_FOUCAULT_001: 0.875 (7/8)
- CM_KAPITZA_001: 0.125 (1/8)
- CM_TOP_001: 0.75 (6/8)
- COS_AGE_001: 0.125 (1/8)
- COS_CMB_001: 0.625 (5/8)
- COS_DESITTER_001: 0.125 (1/8)
- COS_DL_001: 0.625 (5/8)
- GR_CHIRP_001: 0.0 (0/8)
- GR_GPS_001: 0.0 (0/8)
- GR_ISCO_001: 0.0 (0/8)
- GR_PERI_001: 0.125 (1/8)
- QFT_CASIMIR_001: 0.125 (1/8)
- QFT_G2_001: 0.375 (3/8)
- QFT_UNRUH_001: 0.285714 (2/7)
- QFT_YUKAWA_001: 0.875 (7/8)
- QI_CLONE_001: 1.0 (8/8)
- QI_HOLEVO_001: 0.25 (2/8)
- QI_TELEPORT_001: 0.75 (6/8)
- QI_WERNER_001: 0.75 (6/8)
- QM_AB_001: 0.5 (4/8)
- QM_BERRY_001: 1.0 (8/8)
- QM_RT_001: 0.125 (1/8)
- QM_TUNNEL_001: 0.142857 (1/7)
- SR_BELL_001: 1.0 (8/8)
- SR_FIZEAU_001: 1.0 (8/8)
- SR_ROCKET_001: 0.125 (1/8)
- SR_TWIN_001: 0.75 (6/8)
- STAT_BEC_001: 0.0 (0/6)
- STAT_ISING_001: 0.875 (7/8)
- STAT_LANDAUER_001: 0.25 (2/8)
- STAT_NEGT_001: 0.75 (6/8)

## Pass Rate By Model

- Gemma 3 12B IT: 0.46875 (15/32)
- Gemma 3 27B IT: 0.5 (16/32)
- Gemma 4 31B IT: 0.84375 (27/32)
- Granite 4.1 8B: 0.655172 (19/29)
- Llama 3.1 8B Instruct: 0.322581 (10/31)
- Ministral 3 8B: 0.375 (12/32)
- Mistral NeMo 12B: 0.125 (4/32)
- Mistral Small 3.2 24B Instruct: 0.4375 (14/32)
