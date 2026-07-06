# +1 Percentage-Point Numeric Tolerance Layer v1 Report

## 1. Purpose

Create a read-only post-autograde secondary label that tests whether strict numeric FAIL rows are rescued by adding one percentage point to each original relative tolerance.

## 2. Input Artifacts

- structured_prompt_pilot_v2..v5 clean autograde CSVs
- gold_fields from learning.db opened read-only
- existing metric row-score CSVs for context

## 3. Original Deterministic Baseline

- total clean graded rows: 252
- PASS: 117
- FAIL: 135
- REVIEW rows: excluded upstream

## 4. Difference from +25% Tolerance Multiplier Layer

- previous +25% rescued rows: 0
- +25% changed 1% to 1.25%; this layer changes 1% to 2% and 2% to 3%.

## 5. +1 Percentage-Point Tolerance Definition

- effective_rel_tolerance = original_rel_tolerance + 0.01
- absolute-only tolerances are preserved.

## 6. Eligibility Rules

- PASS rows are preserved as PASS_ORIGINAL.
- FAIL rows are rescued only when all originally failed numeric mismatches pass under +1 percentage-point relative tolerance.
- Missing, unparseable, extraction, format, conceptual, symbolic, formula, or ambiguous failures remain HARD_FAIL.

## 7. Row Coverage

- scenarios represented: 32
- models represented: 8
- protected inputs unchanged: yes

## 8. Overall Results

- HARD_FAIL: 134
- PASS_ORIGINAL: 117
- PLUS_ONE_PP_NUMERIC_RESCUE: 1
- rescue_share_of_original_fails: 0.007407

## 9. Results by Batch

| batch | total | original PASS | original FAIL | rescued | hard fail | rescue share |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| V2 | 64 | 37 | 27 | 1 | 26 | 0.037037 |
| V3 | 61 | 24 | 37 | 0 | 37 | 0.0 |
| V4 | 63 | 19 | 44 | 0 | 44 | 0.0 |
| V5 | 64 | 37 | 27 | 0 | 27 | 0.0 |

## 10. Results by Scenario

| scenario | total | original PASS | original FAIL | rescued | hard fail | rescue share |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| CM_APSIDAL_001 | 8 | 3 | 5 | 0 | 5 | 0.0 |
| CM_FOUCAULT_001 | 8 | 7 | 1 | 1 | 0 | 1.0 |
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

## 11. Results by Model

| model | total | original PASS | original FAIL | rescued | hard fail | rescue share |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Gemma 3 12B IT | 32 | 15 | 17 | 0 | 17 | 0.0 |
| Gemma 3 27B IT | 32 | 16 | 16 | 0 | 16 | 0.0 |
| Gemma 4 31B IT | 32 | 27 | 5 | 0 | 5 | 0.0 |
| Granite 4.1 8B | 29 | 19 | 10 | 0 | 10 | 0.0 |
| Llama 3.1 8B Instruct | 31 | 10 | 21 | 0 | 21 | 0.0 |
| Ministral 3 8B | 32 | 12 | 20 | 0 | 20 | 0.0 |
| Mistral NeMo 12B | 32 | 4 | 28 | 1 | 27 | 0.035714 |
| Mistral Small 3.2 24B Instruct | 32 | 14 | 18 | 0 | 18 | 0.0 |

## 12. Rows Reclassified as PLUS_ONE_PP_NUMERIC_RESCUE

- V2 / CM_FOUCAULT_001 / Mistral NeMo 12B: all_original_numeric_mismatches_pass_under_plus_one_percentage_point_tolerance

## 13. Examples of HARD_FAIL Rows That Remained Hard

- V2 / COS_CMB_001 / Llama 3.1 8B Instruct: numeric_mismatch_exceeds_plus_one_percentage_point_tolerance; tags=T_rec_K:MISMATCH;log10_energy_ratio:MISMATCH;log10_number_ratio:MISMATCH
- V2 / COS_CMB_001 / Mistral NeMo 12B: numeric_mismatch_exceeds_plus_one_percentage_point_tolerance; tags=log10_energy_ratio:MISMATCH;log10_number_ratio:MISMATCH
- V2 / COS_CMB_001 / Mistral Small 3.2 24B Instruct: numeric_mismatch_exceeds_plus_one_percentage_point_tolerance; tags=log10_energy_ratio:MISMATCH;log10_number_ratio:MISMATCH
- V2 / GR_ISCO_001 / Gemma 3 12B IT: numeric_mismatch_exceeds_plus_one_percentage_point_tolerance; tags=f_gw_hz:MISMATCH;f_orbital_hz:MISMATCH;r_isco_km:MISMATCH
- V2 / GR_ISCO_001 / Gemma 3 27B IT: numeric_mismatch_exceeds_plus_one_percentage_point_tolerance; tags=f_gw_hz:MISMATCH;f_orbital_hz:MISMATCH
- V2 / GR_ISCO_001 / Gemma 4 31B IT: numeric_mismatch_exceeds_plus_one_percentage_point_tolerance; tags=f_gw_hz:MISMATCH;f_orbital_hz:MISMATCH
- V2 / GR_ISCO_001 / Granite 4.1 8B: numeric_mismatch_exceeds_plus_one_percentage_point_tolerance; tags=f_gw_hz:MISMATCH;f_orbital_hz:MISMATCH
- V2 / GR_ISCO_001 / Llama 3.1 8B Instruct: numeric_mismatch_exceeds_plus_one_percentage_point_tolerance; tags=f_gw_hz:MISMATCH;f_orbital_hz:MISMATCH;r_isco_km:MISMATCH
- V2 / GR_ISCO_001 / Ministral 3 8B: numeric_mismatch_exceeds_plus_one_percentage_point_tolerance; tags=f_gw_hz:MISMATCH;f_orbital_hz:MISMATCH;r_isco_km:MISMATCH
- V2 / GR_ISCO_001 / Mistral NeMo 12B: numeric_mismatch_exceeds_plus_one_percentage_point_tolerance; tags=f_gw_hz:MISMATCH;f_orbital_hz:MISMATCH;r_isco_km:MISMATCH

## 14. Comparison with +25% Layer

- previous SOFT_NUMERIC_FAIL count: 0
- new PLUS_ONE_PP_NUMERIC_RESCUE count: 1
- rows newly rescued by +1 percentage-point tolerance: 1

## 15. Interaction With Metric Scores

| category | rows | mean BERTScore F1 | mean ROUGE-L F1 | mean chrF | mean ROSCOE reasoning_alignment |
| --- | ---: | ---: | ---: | ---: | ---: |
| PASS_ORIGINAL | 117 | 0.660854 | 0.807369 | 0.83639 | 0.93994 |
| PLUS_ONE_PP_NUMERIC_RESCUE | 1 | 0.814434 | 0.929134 | 0.925182 | 0.946443 |
| HARD_FAIL | 134 | 0.588578 | 0.761777 | 0.769972 | 0.917935 |

## 16. Interpretation

PLUS_ONE_PP_NUMERIC_RESCUE is not a pass. It means the row failed strict numeric grading but every numeric failure passes after adding one percentage point to the original relative tolerance, with no independent hard-fail reason.

## 17. Limitations

- Uses existing normalized final-answer fields only.
- Does not revisit raw outputs or evaluate conceptual reasoning.
- Absolute-only tolerance fields are left unchanged.

## 18. Recommended Next Categorization Layer

Separate HARD_FAIL into numeric-too-far, unparseable, missing-field, and structurally invalid extraction categories.

## Field-Level Failure Summary

- numeric_mismatch: 303
- unparseable_value: 6
