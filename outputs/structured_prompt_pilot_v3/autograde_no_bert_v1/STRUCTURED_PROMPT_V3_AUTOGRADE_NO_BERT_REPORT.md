# Structured Prompt v3 Autograde No BERT Report

## Inputs

- raw_runs: /Users/upigdir/Desktop/Pipeline SQL proj/outputs/structured_prompt_pilot_v3/structured_prompt_pilot_v3_runs.json
- review_layer_csv: /Users/upigdir/Desktop/Pipeline SQL proj/outputs/structured_prompt_pilot_v3/review_layer_v1/review_layer_v1.csv
- review_layer_json: /Users/upigdir/Desktop/Pipeline SQL proj/outputs/structured_prompt_pilot_v3/review_layer_v1/review_layer_v1.json

## Safety

- learning_db_modified: no
- db_backup_created: no
- BERTScore was not run.

## Counts

- CLEAN rows autograded: 61
- REVIEW rows excluded: 3

## Extraction Status Distribution

- OK: 61

## Deterministic Grade Distribution

- FAIL: 37
- PASS: 24
- overall_pass_rate: 0.393443

## Summary By Scenario

| scenario_id | clean_rows | pass_count | fail_count | pass_rate | most_common_failure_mode |
|---|---:|---:|---:|---:|---|
| CM_APSIDAL_001 | 8 | 3 | 5 | 0.375 | numeric_mismatch |
| COS_DL_001 | 8 | 5 | 3 | 0.625 | numeric_mismatch |
| GR_GPS_001 | 8 | 0 | 8 | 0.0 | numeric_mismatch |
| QFT_CASIMIR_001 | 8 | 1 | 7 | 0.125 | numeric_mismatch |
| QI_WERNER_001 | 8 | 6 | 2 | 0.75 | numeric_mismatch |
| QM_TUNNEL_001 | 7 | 1 | 6 | 0.142857 | numeric_mismatch |
| SR_BELL_001 | 8 | 8 | 0 | 1.0 | none |
| STAT_BEC_001 | 6 | 0 | 6 | 0.0 | numeric_mismatch |

## Summary By Model

| model_name | clean_rows | pass_count | fail_count | pass_rate | most_common_failure_mode |
|---|---:|---:|---:|---:|---|
| Gemma 3 12B IT | 8 | 2 | 6 | 0.25 | numeric_mismatch |
| Gemma 3 27B IT | 8 | 3 | 5 | 0.375 | numeric_mismatch |
| Gemma 4 31B IT | 8 | 5 | 3 | 0.625 | numeric_mismatch |
| Granite 4.1 8B | 6 | 5 | 1 | 0.833333 | numeric_mismatch |
| Llama 3.1 8B Instruct | 7 | 2 | 5 | 0.285714 | numeric_mismatch |
| Ministral 3 8B | 8 | 2 | 6 | 0.25 | numeric_mismatch |
| Mistral NeMo 12B | 8 | 1 | 7 | 0.125 | numeric_mismatch |
| Mistral Small 3.2 24B Instruct | 8 | 4 | 4 | 0.5 | numeric_mismatch |

## Failed Fields And Failure Tags

- numeric_mismatch: 36
- unparseable_value: 1
- CM_APSIDAL_001 / Gemma 3 12B IT: failed_fields=apsidal_n_minus1_deg;precession_per_period_deg error_tags=apsidal_n_minus1_deg:MISMATCH;precession_per_period_deg:MISMATCH
- CM_APSIDAL_001 / Gemma 3 27B IT: failed_fields=apsidal_n_minus1_deg;precession_per_period_deg error_tags=apsidal_n_minus1_deg:MISMATCH;precession_per_period_deg:MISMATCH
- CM_APSIDAL_001 / Llama 3.1 8B Instruct: failed_fields=apsidal_n_minus1_deg;precession_per_period_deg error_tags=apsidal_n_minus1_deg:MISMATCH;precession_per_period_deg:MISMATCH
- CM_APSIDAL_001 / Ministral 3 8B: failed_fields=apsidal_n_minus1_deg;precession_per_period_deg error_tags=apsidal_n_minus1_deg:MISMATCH;precession_per_period_deg:MISMATCH
- CM_APSIDAL_001 / Mistral NeMo 12B: failed_fields=apsidal_n_minus1_deg;precession_per_period_deg error_tags=apsidal_n_minus1_deg:MISMATCH;precession_per_period_deg:MISMATCH
- COS_DL_001 / Gemma 3 12B IT: failed_fields=hubble_distance_mpc error_tags=hubble_distance_mpc:MISMATCH
- COS_DL_001 / Ministral 3 8B: failed_fields=dl_eds_mpc;dl_lcdm_mpc;dl_linear_mpc;hubble_distance_mpc error_tags=dl_eds_mpc:MISMATCH;dl_lcdm_mpc:MISMATCH;dl_linear_mpc:MISMATCH;hubble_distance_mpc:MISMATCH
- COS_DL_001 / Mistral NeMo 12B: failed_fields=dl_eds_mpc;dl_lcdm_mpc;dl_linear_mpc;hubble_distance_mpc error_tags=dl_eds_mpc:MISMATCH;dl_lcdm_mpc:MISMATCH;dl_linear_mpc:MISMATCH;hubble_distance_mpc:MISMATCH
- GR_GPS_001 / Gemma 3 12B IT: failed_fields=grav_shift_us_day;net_shift_us_day;velocity_shift_us_day error_tags=grav_shift_us_day:MISMATCH;net_shift_us_day:MISMATCH;velocity_shift_us_day:MISMATCH
- GR_GPS_001 / Gemma 3 27B IT: failed_fields=grav_shift_us_day;net_shift_us_day;velocity_shift_us_day error_tags=grav_shift_us_day:MISMATCH;net_shift_us_day:MISMATCH;velocity_shift_us_day:MISMATCH
- GR_GPS_001 / Gemma 4 31B IT: failed_fields=velocity_shift_us_day error_tags=velocity_shift_us_day:MISMATCH
- GR_GPS_001 / Granite 4.1 8B: failed_fields=velocity_shift_us_day error_tags=velocity_shift_us_day:MISMATCH
- GR_GPS_001 / Llama 3.1 8B Instruct: failed_fields=grav_shift_us_day;net_shift_us_day;velocity_shift_us_day error_tags=grav_shift_us_day:MISMATCH;net_shift_us_day:MISMATCH;velocity_shift_us_day:MISMATCH
- GR_GPS_001 / Ministral 3 8B: failed_fields=grav_shift_us_day;net_shift_us_day;velocity_shift_us_day error_tags=grav_shift_us_day:MISMATCH;net_shift_us_day:MISMATCH;velocity_shift_us_day:MISMATCH
- GR_GPS_001 / Mistral NeMo 12B: failed_fields=grav_shift_us_day;net_shift_us_day;velocity_shift_us_day error_tags=grav_shift_us_day:MISMATCH;net_shift_us_day:MISMATCH;velocity_shift_us_day:MISMATCH
- GR_GPS_001 / Mistral Small 3.2 24B Instruct: failed_fields=grav_shift_us_day;net_shift_us_day;velocity_shift_us_day error_tags=grav_shift_us_day:MISMATCH;net_shift_us_day:MISMATCH;velocity_shift_us_day:MISMATCH
- QFT_CASIMIR_001 / Gemma 3 12B IT: failed_fields=energy_per_area_uJ_m2;pressure_double_d_pa;pressure_pa error_tags=energy_per_area_uJ_m2:MISMATCH;pressure_double_d_pa:MISMATCH;pressure_pa:MISMATCH
- QFT_CASIMIR_001 / Gemma 3 27B IT: failed_fields=energy_per_area_uJ_m2;pressure_double_d_pa;pressure_pa error_tags=energy_per_area_uJ_m2:MISMATCH;pressure_double_d_pa:MISMATCH;pressure_pa:MISMATCH
- QFT_CASIMIR_001 / Gemma 4 31B IT: failed_fields=energy_per_area_uJ_m2;pressure_double_d_pa;pressure_pa error_tags=energy_per_area_uJ_m2:MISMATCH;pressure_double_d_pa:MISMATCH;pressure_pa:MISMATCH
- QFT_CASIMIR_001 / Llama 3.1 8B Instruct: failed_fields=energy_per_area_uJ_m2;pressure_double_d_pa;pressure_pa error_tags=energy_per_area_uJ_m2:MISMATCH;pressure_double_d_pa:MISMATCH;pressure_pa:MISMATCH
- QFT_CASIMIR_001 / Ministral 3 8B: failed_fields=energy_per_area_uJ_m2;pressure_double_d_pa;pressure_pa error_tags=energy_per_area_uJ_m2:MISMATCH;pressure_double_d_pa:MISMATCH;pressure_pa:MISMATCH
- QFT_CASIMIR_001 / Mistral NeMo 12B: failed_fields=energy_per_area_uJ_m2;pressure_double_d_pa;pressure_pa error_tags=energy_per_area_uJ_m2:MISMATCH;pressure_double_d_pa:MISMATCH;pressure_pa:MISMATCH
- QFT_CASIMIR_001 / Mistral Small 3.2 24B Instruct: failed_fields=energy_per_area_uJ_m2;pressure_double_d_pa;pressure_pa error_tags=energy_per_area_uJ_m2:MISMATCH;pressure_double_d_pa:MISMATCH;pressure_pa:MISMATCH
- QI_WERNER_001 / Llama 3.1 8B Instruct: failed_fields=concurrence_at_p05 error_tags=concurrence_at_p05:MISMATCH
- QI_WERNER_001 / Mistral NeMo 12B: failed_fields=concurrence_at_p05 error_tags=concurrence_at_p05:MISMATCH
- QM_TUNNEL_001 / Gemma 3 12B IT: failed_fields=kappa_L;kappa_per_nm;log10_T error_tags=kappa_L:MISMATCH;kappa_per_nm:MISMATCH;log10_T:MISMATCH
- QM_TUNNEL_001 / Gemma 3 27B IT: failed_fields=kappa_L;kappa_per_nm;log10_T error_tags=kappa_L:MISMATCH;kappa_per_nm:MISMATCH;log10_T:MISMATCH
- QM_TUNNEL_001 / Llama 3.1 8B Instruct: failed_fields=kappa_L;kappa_per_nm;log10_T error_tags=kappa_L:MISMATCH;kappa_per_nm:MISMATCH;log10_T:MISMATCH
- QM_TUNNEL_001 / Ministral 3 8B: failed_fields=kappa_L;kappa_per_nm;log10_T error_tags=kappa_L:MISMATCH;kappa_per_nm:MISMATCH;log10_T:MISMATCH
- QM_TUNNEL_001 / Mistral NeMo 12B: failed_fields=kappa_L;kappa_per_nm;log10_T;prefactor error_tags=kappa_L:MISMATCH;kappa_per_nm:UNPARSEABLE:parse-fail:SympifyError;log10_T:MISMATCH;prefactor:MISMATCH
- QM_TUNNEL_001 / Mistral Small 3.2 24B Instruct: failed_fields=kappa_L;kappa_per_nm;log10_T error_tags=kappa_L:MISMATCH;kappa_per_nm:MISMATCH;log10_T:MISMATCH
- STAT_BEC_001 / Gemma 3 12B IT: failed_fields=tc_nK;tc_no_zeta_nK error_tags=tc_nK:MISMATCH;tc_no_zeta_nK:MISMATCH
- STAT_BEC_001 / Gemma 3 27B IT: failed_fields=tc_nK;tc_no_zeta_nK error_tags=tc_nK:MISMATCH;tc_no_zeta_nK:MISMATCH
- STAT_BEC_001 / Gemma 4 31B IT: failed_fields=tc_nK;tc_no_zeta_nK error_tags=tc_nK:MISMATCH;tc_no_zeta_nK:MISMATCH
- STAT_BEC_001 / Ministral 3 8B: failed_fields=tc_nK;tc_no_zeta_nK error_tags=tc_nK:MISMATCH;tc_no_zeta_nK:MISMATCH
- STAT_BEC_001 / Mistral NeMo 12B: failed_fields=psd_at_2tc;tc_nK;tc_no_zeta_nK error_tags=psd_at_2tc:MISMATCH;tc_nK:MISMATCH;tc_no_zeta_nK:MISMATCH
- STAT_BEC_001 / Mistral Small 3.2 24B Instruct: failed_fields=tc_nK;tc_no_zeta_nK error_tags=tc_nK:MISMATCH;tc_no_zeta_nK:MISMATCH
