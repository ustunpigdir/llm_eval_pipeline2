# Structured Prompt v4 Autograde No BERT Report

## Inputs

- raw_runs: /Users/upigdir/Desktop/Pipeline SQL proj/outputs/structured_prompt_pilot_v4/structured_prompt_pilot_v4_runs.json
- review_layer_csv: /Users/upigdir/Desktop/Pipeline SQL proj/outputs/structured_prompt_pilot_v4/review_layer_v1/review_layer_v1.csv
- review_layer_json: /Users/upigdir/Desktop/Pipeline SQL proj/outputs/structured_prompt_pilot_v4/review_layer_v1/review_layer_v1.json

## Safety

- learning_db_modified: no
- db_backup_created: no
- BERTScore was not run.

## Counts

- CLEAN rows autograded: 63
- REVIEW rows excluded: 1

## Extraction Status Distribution

- OK: 63

## Deterministic Grade Distribution

- FAIL: 44
- PASS: 19
- overall_pass_rate: 0.301587

## Summary By Scenario

| scenario_id | clean_rows | pass_count | fail_count | pass_rate | most_common_failure_mode |
|---|---:|---:|---:|---:|---|
| CM_KAPITZA_001 | 8 | 1 | 7 | 0.125 | numeric_mismatch |
| COS_DESITTER_001 | 8 | 1 | 7 | 0.125 | numeric_mismatch |
| GR_PERI_001 | 8 | 1 | 7 | 0.125 | numeric_mismatch |
| QFT_UNRUH_001 | 7 | 2 | 5 | 0.285714 | numeric_mismatch |
| QI_HOLEVO_001 | 8 | 2 | 6 | 0.25 | numeric_mismatch |
| QM_AB_001 | 8 | 4 | 4 | 0.5 | numeric_mismatch |
| SR_TWIN_001 | 8 | 6 | 2 | 0.75 | numeric_mismatch |
| STAT_LANDAUER_001 | 8 | 2 | 6 | 0.25 | numeric_mismatch |

## Summary By Model

| model_name | clean_rows | pass_count | fail_count | pass_rate | most_common_failure_mode |
|---|---:|---:|---:|---:|---|
| Gemma 3 12B IT | 8 | 3 | 5 | 0.375 | numeric_mismatch |
| Gemma 3 27B IT | 8 | 2 | 6 | 0.25 | numeric_mismatch |
| Gemma 4 31B IT | 8 | 8 | 0 | 1.0 | none |
| Granite 4.1 8B | 7 | 3 | 4 | 0.428571 | numeric_mismatch |
| Llama 3.1 8B Instruct | 8 | 1 | 7 | 0.125 | numeric_mismatch |
| Ministral 3 8B | 8 | 1 | 7 | 0.125 | numeric_mismatch |
| Mistral NeMo 12B | 8 | 0 | 8 | 0.0 | numeric_mismatch |
| Mistral Small 3.2 24B Instruct | 8 | 1 | 7 | 0.125 | numeric_mismatch |

## Failed Fields And Failure Tags

- numeric_mismatch: 43
- unparseable_value: 1
- CM_KAPITZA_001 / Gemma 3 12B IT: failed_fields=f_min_hz;omega_min_rad_s error_tags=f_min_hz:MISMATCH;omega_min_rad_s:MISMATCH
- CM_KAPITZA_001 / Gemma 3 27B IT: failed_fields=f_min_hz;omega_min_rad_s error_tags=f_min_hz:MISMATCH;omega_min_rad_s:MISMATCH
- CM_KAPITZA_001 / Granite 4.1 8B: failed_fields=f_min_hz;omega_min_rad_s error_tags=f_min_hz:MISMATCH;omega_min_rad_s:MISMATCH
- CM_KAPITZA_001 / Llama 3.1 8B Instruct: failed_fields=f_min_hz error_tags=f_min_hz:MISMATCH
- CM_KAPITZA_001 / Ministral 3 8B: failed_fields=f_min_hz;omega_min_rad_s error_tags=f_min_hz:MISMATCH;omega_min_rad_s:MISMATCH
- CM_KAPITZA_001 / Mistral NeMo 12B: failed_fields=f_min_hz;omega_min_rad_s error_tags=f_min_hz:MISMATCH;omega_min_rad_s:MISMATCH
- CM_KAPITZA_001 / Mistral Small 3.2 24B Instruct: failed_fields=f_min_hz;omega_min_rad_s error_tags=f_min_hz:MISMATCH;omega_min_rad_s:MISMATCH
- COS_DESITTER_001 / Gemma 3 12B IT: failed_fields=efolds_to_gh;gh_temp_e30_K;horizon_gpc error_tags=efolds_to_gh:MISMATCH;gh_temp_e30_K:MISMATCH;horizon_gpc:MISMATCH
- COS_DESITTER_001 / Gemma 3 27B IT: failed_fields=efolds_to_gh;gh_temp_e30_K;horizon_gpc error_tags=efolds_to_gh:MISMATCH;gh_temp_e30_K:MISMATCH;horizon_gpc:MISMATCH
- COS_DESITTER_001 / Granite 4.1 8B: failed_fields=efolds_to_gh error_tags=efolds_to_gh:MISMATCH
- COS_DESITTER_001 / Llama 3.1 8B Instruct: failed_fields=efolds_to_gh;gh_temp_e30_K;horizon_gpc error_tags=efolds_to_gh:MISMATCH;gh_temp_e30_K:MISMATCH;horizon_gpc:MISMATCH
- COS_DESITTER_001 / Ministral 3 8B: failed_fields=gh_temp_e30_K;horizon_gpc error_tags=gh_temp_e30_K:MISMATCH;horizon_gpc:MISMATCH
- COS_DESITTER_001 / Mistral NeMo 12B: failed_fields=efolds_to_gh;gh_temp_e30_K error_tags=efolds_to_gh:MISMATCH;gh_temp_e30_K:MISMATCH
- COS_DESITTER_001 / Mistral Small 3.2 24B Instruct: failed_fields=efolds_to_gh;gh_temp_e30_K;horizon_gpc error_tags=efolds_to_gh:MISMATCH;gh_temp_e30_K:MISMATCH;horizon_gpc:MISMATCH
- GR_PERI_001 / Gemma 3 12B IT: failed_fields=advance_arcsec_orbit error_tags=advance_arcsec_orbit:MISMATCH
- GR_PERI_001 / Gemma 3 27B IT: failed_fields=advance_arcsec_century;advance_arcsec_orbit error_tags=advance_arcsec_century:MISMATCH;advance_arcsec_orbit:MISMATCH
- GR_PERI_001 / Granite 4.1 8B: failed_fields=advance_arcsec_orbit error_tags=advance_arcsec_orbit:MISMATCH
- GR_PERI_001 / Llama 3.1 8B Instruct: failed_fields=advance_arcsec_century;advance_arcsec_orbit error_tags=advance_arcsec_century:MISMATCH;advance_arcsec_orbit:MISMATCH
- GR_PERI_001 / Ministral 3 8B: failed_fields=advance_arcsec_orbit error_tags=advance_arcsec_orbit:MISMATCH
- GR_PERI_001 / Mistral NeMo 12B: failed_fields=advance_arcsec_century;advance_arcsec_orbit error_tags=advance_arcsec_century:MISMATCH;advance_arcsec_orbit:MISMATCH
- GR_PERI_001 / Mistral Small 3.2 24B Instruct: failed_fields=advance_arcsec_orbit error_tags=advance_arcsec_orbit:MISMATCH
- QFT_UNRUH_001 / Gemma 3 12B IT: failed_fields=accel_for_1K_e20;unruh_temp_K error_tags=accel_for_1K_e20:MISMATCH;unruh_temp_K:MISMATCH
- QFT_UNRUH_001 / Llama 3.1 8B Instruct: failed_fields=accel_for_1K_e20;unruh_temp_K error_tags=accel_for_1K_e20:MISMATCH;unruh_temp_K:MISMATCH
- QFT_UNRUH_001 / Ministral 3 8B: failed_fields=accel_for_1K_e20;unruh_temp_K error_tags=accel_for_1K_e20:MISMATCH;unruh_temp_K:MISMATCH
- QFT_UNRUH_001 / Mistral NeMo 12B: failed_fields=accel_for_1K_e20;unruh_temp_K error_tags=accel_for_1K_e20:MISMATCH;unruh_temp_K:MISMATCH
- QFT_UNRUH_001 / Mistral Small 3.2 24B Instruct: failed_fields=accel_for_1K_e20;unruh_temp_K error_tags=accel_for_1K_e20:MISMATCH;unruh_temp_K:MISMATCH
- QI_HOLEVO_001 / Gemma 3 27B IT: failed_fields=avg_state_purity;eigenvalue_large;holevo_chi_bits error_tags=avg_state_purity:MISMATCH;eigenvalue_large:MISMATCH;holevo_chi_bits:MISMATCH
- QI_HOLEVO_001 / Granite 4.1 8B: failed_fields=avg_state_purity;eigenvalue_large;holevo_chi_bits error_tags=avg_state_purity:MISMATCH;eigenvalue_large:MISMATCH;holevo_chi_bits:MISMATCH
- QI_HOLEVO_001 / Llama 3.1 8B Instruct: failed_fields=avg_state_purity;eigenvalue_large;holevo_chi_bits error_tags=avg_state_purity:MISMATCH;eigenvalue_large:MISMATCH;holevo_chi_bits:MISMATCH
- QI_HOLEVO_001 / Ministral 3 8B: failed_fields=avg_state_purity;eigenvalue_large;holevo_chi_bits error_tags=avg_state_purity:MISMATCH;eigenvalue_large:MISMATCH;holevo_chi_bits:UNPARSEABLE:parse-fail:TokenError
- QI_HOLEVO_001 / Mistral NeMo 12B: failed_fields=avg_state_purity;eigenvalue_large;holevo_chi_bits error_tags=avg_state_purity:MISMATCH;eigenvalue_large:MISMATCH;holevo_chi_bits:MISMATCH
- QI_HOLEVO_001 / Mistral Small 3.2 24B Instruct: failed_fields=avg_state_purity;holevo_chi_bits error_tags=avg_state_purity:MISMATCH;holevo_chi_bits:MISMATCH
- QM_AB_001 / Llama 3.1 8B Instruct: failed_fields=flux_quanta;fringe_shift;total_phase_rad error_tags=flux_quanta:MISMATCH;fringe_shift:MISMATCH;total_phase_rad:MISMATCH
- QM_AB_001 / Ministral 3 8B: failed_fields=flux_quanta;fringe_shift;total_phase_rad error_tags=flux_quanta:MISMATCH;fringe_shift:MISMATCH;total_phase_rad:MISMATCH
- QM_AB_001 / Mistral NeMo 12B: failed_fields=flux_quanta;fringe_shift;total_phase_rad error_tags=flux_quanta:MISMATCH;fringe_shift:MISMATCH;total_phase_rad:MISMATCH
- QM_AB_001 / Mistral Small 3.2 24B Instruct: failed_fields=flux_quanta;fringe_shift;total_phase_rad error_tags=flux_quanta:MISMATCH;fringe_shift:MISMATCH;total_phase_rad:MISMATCH
- SR_TWIN_001 / Gemma 3 27B IT: failed_fields=earth_time_yr;traveler_time_yr error_tags=earth_time_yr:MISMATCH;traveler_time_yr:MISMATCH
- SR_TWIN_001 / Mistral NeMo 12B: failed_fields=traveler_time_yr error_tags=traveler_time_yr:MISMATCH
- STAT_LANDAUER_001 / Gemma 3 12B IT: failed_fields=landauer_meV;landauer_zJ error_tags=landauer_meV:MISMATCH;landauer_zJ:MISMATCH
- STAT_LANDAUER_001 / Gemma 3 27B IT: failed_fields=landauer_meV error_tags=landauer_meV:MISMATCH
- STAT_LANDAUER_001 / Llama 3.1 8B Instruct: failed_fields=landauer_meV;landauer_zJ error_tags=landauer_meV:MISMATCH;landauer_zJ:MISMATCH
- STAT_LANDAUER_001 / Ministral 3 8B: failed_fields=landauer_meV error_tags=landauer_meV:MISMATCH
- STAT_LANDAUER_001 / Mistral NeMo 12B: failed_fields=landauer_meV;landauer_zJ error_tags=landauer_meV:MISMATCH;landauer_zJ:MISMATCH
- STAT_LANDAUER_001 / Mistral Small 3.2 24B Instruct: failed_fields=landauer_meV;landauer_zJ error_tags=landauer_meV:MISMATCH;landauer_zJ:MISMATCH
