# Soft Numeric Fail Layer v1 Report

## 1. Purpose

Create a post-autograde secondary label that separates strict PASS rows, near-tolerance numeric FAIL rows, and harder FAIL rows. Original deterministic PASS/FAIL labels are unchanged.

## 2. Input Artifacts

- V2: outputs/structured_prompt_pilot_v2/autograde_no_bert_v1/structured_prompt_v2_clean_autograde.csv
- V3: outputs/structured_prompt_pilot_v3/autograde_no_bert_v1/structured_prompt_v3_clean_autograde.csv
- V4: outputs/structured_prompt_pilot_v4/autograde_no_bert_v1/structured_prompt_v4_clean_autograde.csv
- V5: outputs/structured_prompt_pilot_v5/autograde_no_bert_v1/structured_prompt_v5_clean_autograde.csv
- gold_fields: learning.db opened read-only
- metric context: existing BERTScore, ROUGE-L, chrF, ROSCOE row-score CSVs

## 3. Original Deterministic Baseline

- total clean graded rows: 252
- PASS: 117
- FAIL: 135
- REVIEW rows: excluded upstream from the source clean autograde files

## 4. Tolerance Increase Definition

- tolerance_multiplier: 1.25
- relative and absolute tolerances are multiplied by 1.25; this is not a flat 25% error allowance.

## 5. Eligibility Rules

- PASS rows are labeled PASS_ORIGINAL and never reclassified.
- FAIL rows become SOFT_NUMERIC_FAIL only when every originally failed numeric mismatch passes under 1.25x tolerance.
- Missing, unparseable, extraction, format, conceptual, symbolic, or ambiguous failures remain HARD_FAIL.

## 6. Row Coverage

- scenarios represented: 32
- models represented: 8
- protected inputs unchanged: yes

## 7. Overall Results

- HARD_FAIL: 135
- PASS_ORIGINAL: 117
- soft_numeric_share_of_original_fails: 0.000000

## 8. Results by Batch

| batch | total | original PASS | original FAIL | soft numeric | hard fail | soft share of fails |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| V2 | 64 | 37 | 27 | 0 | 27 | 0.0 |
| V3 | 61 | 24 | 37 | 0 | 37 | 0.0 |
| V4 | 63 | 19 | 44 | 0 | 44 | 0.0 |
| V5 | 64 | 37 | 27 | 0 | 27 | 0.0 |

## 9. Results by Scenario

| scenario | total | original PASS | original FAIL | soft numeric | hard fail | soft share of fails |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| CM_APSIDAL_001 | 8 | 3 | 5 | 0 | 5 | 0.0 |
| CM_FOUCAULT_001 | 8 | 7 | 1 | 0 | 1 | 0.0 |
| CM_KAPITZA_001 | 8 | 1 | 7 | 0 | 7 | 0.0 |
| CM_TOP_001 | 8 | 6 | 2 | 0 | 2 | 0.0 |
| COS_AGE_001 | 8 | 1 | 7 | 0 | 7 | 0.0 |
| COS_CMB_001 | 8 | 5 | 3 | 0 | 3 | 0.0 |
| COS_DESITTER_001 | 8 | 1 | 7 | 0 | 7 | 0.0 |
| COS_DL_001 | 8 | 5 | 3 | 0 | 3 | 0.0 |
| GR_CHIRP_001 | 8 | 0 | 8 | 0 | 8 | 0.0 |
| GR_GPS_001 | 8 | 0 | 8 | 0 | 8 | 0.0 |
| GR_ISCO_001 | 8 | 0 | 8 | 0 | 8 | 0.0 |
| GR_PERI_001 | 8 | 1 | 7 | 0 | 7 | 0.0 |
| QFT_CASIMIR_001 | 8 | 1 | 7 | 0 | 7 | 0.0 |
| QFT_G2_001 | 8 | 3 | 5 | 0 | 5 | 0.0 |
| QFT_UNRUH_001 | 7 | 2 | 5 | 0 | 5 | 0.0 |
| QFT_YUKAWA_001 | 8 | 7 | 1 | 0 | 1 | 0.0 |
| QI_CLONE_001 | 8 | 8 | 0 | 0 | 0 | 0 |
| QI_HOLEVO_001 | 8 | 2 | 6 | 0 | 6 | 0.0 |
| QI_TELEPORT_001 | 8 | 6 | 2 | 0 | 2 | 0.0 |
| QI_WERNER_001 | 8 | 6 | 2 | 0 | 2 | 0.0 |
| QM_AB_001 | 8 | 4 | 4 | 0 | 4 | 0.0 |
| QM_BERRY_001 | 8 | 8 | 0 | 0 | 0 | 0 |
| QM_RT_001 | 8 | 1 | 7 | 0 | 7 | 0.0 |
| QM_TUNNEL_001 | 7 | 1 | 6 | 0 | 6 | 0.0 |
| SR_BELL_001 | 8 | 8 | 0 | 0 | 0 | 0 |
| SR_FIZEAU_001 | 8 | 8 | 0 | 0 | 0 | 0 |
| SR_ROCKET_001 | 8 | 1 | 7 | 0 | 7 | 0.0 |
| SR_TWIN_001 | 8 | 6 | 2 | 0 | 2 | 0.0 |
| STAT_BEC_001 | 6 | 0 | 6 | 0 | 6 | 0.0 |
| STAT_ISING_001 | 8 | 7 | 1 | 0 | 1 | 0.0 |
| STAT_LANDAUER_001 | 8 | 2 | 6 | 0 | 6 | 0.0 |
| STAT_NEGT_001 | 8 | 6 | 2 | 0 | 2 | 0.0 |

## 10. Results by Model

| model | total | original PASS | original FAIL | soft numeric | hard fail | soft share of fails |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Gemma 3 12B IT | 32 | 15 | 17 | 0 | 17 | 0.0 |
| Gemma 3 27B IT | 32 | 16 | 16 | 0 | 16 | 0.0 |
| Gemma 4 31B IT | 32 | 27 | 5 | 0 | 5 | 0.0 |
| Granite 4.1 8B | 29 | 19 | 10 | 0 | 10 | 0.0 |
| Llama 3.1 8B Instruct | 31 | 10 | 21 | 0 | 21 | 0.0 |
| Ministral 3 8B | 32 | 12 | 20 | 0 | 20 | 0.0 |
| Mistral NeMo 12B | 32 | 4 | 28 | 0 | 28 | 0.0 |
| Mistral Small 3.2 24B Instruct | 32 | 14 | 18 | 0 | 18 | 0.0 |

## 11. Rows Reclassified as SOFT_NUMERIC_FAIL

- none

## 12. Examples of HARD_FAIL Rows That Remained Hard

- V2 / CM_FOUCAULT_001 / Mistral NeMo 12B: numeric_mismatch_exceeds_1_25x_tolerance; tags=period_hours:MISMATCH;rate_deg_per_day:MISMATCH;rate_deg_per_hour:MISMATCH
- V2 / COS_CMB_001 / Llama 3.1 8B Instruct: numeric_mismatch_exceeds_1_25x_tolerance; tags=T_rec_K:MISMATCH;log10_energy_ratio:MISMATCH;log10_number_ratio:MISMATCH
- V2 / COS_CMB_001 / Mistral NeMo 12B: numeric_mismatch_exceeds_1_25x_tolerance; tags=log10_energy_ratio:MISMATCH;log10_number_ratio:MISMATCH
- V2 / COS_CMB_001 / Mistral Small 3.2 24B Instruct: numeric_mismatch_exceeds_1_25x_tolerance; tags=log10_energy_ratio:MISMATCH;log10_number_ratio:MISMATCH
- V2 / GR_ISCO_001 / Gemma 3 12B IT: numeric_mismatch_exceeds_1_25x_tolerance; tags=f_gw_hz:MISMATCH;f_orbital_hz:MISMATCH;r_isco_km:MISMATCH
- V2 / GR_ISCO_001 / Gemma 3 27B IT: numeric_mismatch_exceeds_1_25x_tolerance; tags=f_gw_hz:MISMATCH;f_orbital_hz:MISMATCH
- V2 / GR_ISCO_001 / Gemma 4 31B IT: numeric_mismatch_exceeds_1_25x_tolerance; tags=f_gw_hz:MISMATCH;f_orbital_hz:MISMATCH
- V2 / GR_ISCO_001 / Granite 4.1 8B: numeric_mismatch_exceeds_1_25x_tolerance; tags=f_gw_hz:MISMATCH;f_orbital_hz:MISMATCH
- V2 / GR_ISCO_001 / Llama 3.1 8B Instruct: numeric_mismatch_exceeds_1_25x_tolerance; tags=f_gw_hz:MISMATCH;f_orbital_hz:MISMATCH;r_isco_km:MISMATCH
- V2 / GR_ISCO_001 / Ministral 3 8B: numeric_mismatch_exceeds_1_25x_tolerance; tags=f_gw_hz:MISMATCH;f_orbital_hz:MISMATCH;r_isco_km:MISMATCH

## 13. Interaction With Metric Scores

| category | rows | mean BERTScore F1 | mean ROUGE-L F1 | mean chrF | mean ROSCOE reasoning_alignment |
| --- | ---: | ---: | ---: | ---: | ---: |
| PASS_ORIGINAL | 117 | 0.660854 | 0.807369 | 0.83639 | 0.93994 |
| SOFT_NUMERIC_FAIL | 0 |  |  |  |  |
| HARD_FAIL | 135 | 0.590251 | 0.763017 | 0.771122 | 0.918146 |

## 14. Interpretation

SOFT_NUMERIC_FAIL is not a pass. It means the answer failed the strict numeric comparison but all failed numeric fields pass when the original tolerance is multiplied by 1.25.

## 15. Limitations

- This layer only uses existing extracted final-answer fields and gold numeric metadata.
- It does not evaluate conceptual reasoning or implement Phase 2 semantics.
- Ambiguous or non-numeric failures are conservatively labeled HARD_FAIL.

## 16. Recommended Next Categorization Layer

Add a separate non-grade-changing taxonomy for missing/unparseable/format failures versus wrong-but-extractable numeric answers.

## Field-Level Failure Summary

- numeric_mismatch: 303
- unparseable_value: 6
