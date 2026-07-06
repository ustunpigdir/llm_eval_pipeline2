# Structured Prompt v2 Autograde No BERT Report

## Inputs

- raw_runs: /Users/upigdir/Desktop/Pipeline SQL proj/outputs/structured_prompt_pilot_v2/structured_prompt_pilot_v2_runs.json
- review_layer_csv: /Users/upigdir/Desktop/Pipeline SQL proj/outputs/structured_prompt_pilot_v2/review_layer_v1/review_layer_v1.csv
- review_layer_json: /Users/upigdir/Desktop/Pipeline SQL proj/outputs/structured_prompt_pilot_v2/review_layer_v1/review_layer_v1.json

## Safety

- learning_db_modified: no
- db_backup_created: no
- BERTScore was not run.

## Counts

- CLEAN rows autograded: 64
- REVIEW rows excluded: 8

## Extraction Status Distribution

- OK: 64

## Deterministic Grade Distribution

- FAIL: 27
- PASS: 37
- overall_pass_rate: 0.578125

## Summary By Scenario

| scenario_id | clean_rows | pass_count | fail_count | pass_rate | most_common_failure_mode |
|---|---:|---:|---:|---:|---|
| CM_FOUCAULT_001 | 8 | 7 | 1 | 0.875 | numeric_mismatch |
| COS_CMB_001 | 8 | 5 | 3 | 0.625 | numeric_mismatch |
| GR_ISCO_001 | 8 | 0 | 8 | 0.0 | numeric_mismatch |
| QFT_G2_001 | 8 | 3 | 5 | 0.375 | numeric_mismatch |
| QI_TELEPORT_001 | 8 | 6 | 2 | 0.75 | unparseable_value |
| QM_BERRY_001 | 8 | 8 | 0 | 1.0 | none |
| SR_ROCKET_001 | 8 | 1 | 7 | 0.125 | numeric_mismatch |
| STAT_ISING_001 | 8 | 7 | 1 | 0.875 | numeric_mismatch |

## Summary By Model

| model_name | clean_rows | pass_count | fail_count | pass_rate | most_common_failure_mode |
|---|---:|---:|---:|---:|---|
| Gemma 3 12B IT | 8 | 5 | 3 | 0.625 | numeric_mismatch |
| Gemma 3 27B IT | 8 | 6 | 2 | 0.75 | numeric_mismatch |
| Gemma 4 31B IT | 8 | 7 | 1 | 0.875 | numeric_mismatch |
| Granite 4.1 8B | 8 | 6 | 2 | 0.75 | numeric_mismatch |
| Llama 3.1 8B Instruct | 8 | 4 | 4 | 0.5 | numeric_mismatch |
| Ministral 3 8B | 8 | 4 | 4 | 0.5 | numeric_mismatch |
| Mistral NeMo 12B | 8 | 1 | 7 | 0.125 | numeric_mismatch |
| Mistral Small 3.2 24B Instruct | 8 | 4 | 4 | 0.5 | numeric_mismatch |

## Failed Fields And Failure Tags

- numeric_mismatch: 25
- unparseable_value: 2
- CM_FOUCAULT_001 / Mistral NeMo 12B: failed_fields=period_hours;rate_deg_per_day;rate_deg_per_hour error_tags=period_hours:MISMATCH;rate_deg_per_day:MISMATCH;rate_deg_per_hour:MISMATCH
- COS_CMB_001 / Llama 3.1 8B Instruct: failed_fields=T_rec_K;log10_energy_ratio;log10_number_ratio error_tags=T_rec_K:MISMATCH;log10_energy_ratio:MISMATCH;log10_number_ratio:MISMATCH
- COS_CMB_001 / Mistral NeMo 12B: failed_fields=log10_energy_ratio;log10_number_ratio error_tags=log10_energy_ratio:MISMATCH;log10_number_ratio:MISMATCH
- COS_CMB_001 / Mistral Small 3.2 24B Instruct: failed_fields=log10_energy_ratio;log10_number_ratio error_tags=log10_energy_ratio:MISMATCH;log10_number_ratio:MISMATCH
- GR_ISCO_001 / Gemma 3 12B IT: failed_fields=f_gw_hz;f_orbital_hz;r_isco_km error_tags=f_gw_hz:MISMATCH;f_orbital_hz:MISMATCH;r_isco_km:MISMATCH
- GR_ISCO_001 / Gemma 3 27B IT: failed_fields=f_gw_hz;f_orbital_hz error_tags=f_gw_hz:MISMATCH;f_orbital_hz:MISMATCH
- GR_ISCO_001 / Gemma 4 31B IT: failed_fields=f_gw_hz;f_orbital_hz error_tags=f_gw_hz:MISMATCH;f_orbital_hz:MISMATCH
- GR_ISCO_001 / Granite 4.1 8B: failed_fields=f_gw_hz;f_orbital_hz error_tags=f_gw_hz:MISMATCH;f_orbital_hz:MISMATCH
- GR_ISCO_001 / Llama 3.1 8B Instruct: failed_fields=f_gw_hz;f_orbital_hz;r_isco_km error_tags=f_gw_hz:MISMATCH;f_orbital_hz:MISMATCH;r_isco_km:MISMATCH
- GR_ISCO_001 / Ministral 3 8B: failed_fields=f_gw_hz;f_orbital_hz;r_isco_km error_tags=f_gw_hz:MISMATCH;f_orbital_hz:MISMATCH;r_isco_km:MISMATCH
- GR_ISCO_001 / Mistral NeMo 12B: failed_fields=f_gw_hz;f_orbital_hz;r_isco_km error_tags=f_gw_hz:MISMATCH;f_orbital_hz:MISMATCH;r_isco_km:MISMATCH
- GR_ISCO_001 / Mistral Small 3.2 24B Instruct: failed_fields=f_gw_hz;f_orbital_hz;r_isco_km error_tags=f_gw_hz:MISMATCH;f_orbital_hz:MISMATCH;r_isco_km:MISMATCH
- QI_TELEPORT_001 / Ministral 3 8B: failed_fields=classical_limit error_tags=classical_limit:UNPARSEABLE:parse-fail:TokenError
- QI_TELEPORT_001 / Mistral NeMo 12B: failed_fields=teleport_fidelity error_tags=teleport_fidelity:MISMATCH
- QFT_G2_001 / Gemma 3 12B IT: failed_fields=anomaly_times_1e3 error_tags=anomaly_times_1e3:MISMATCH
- QFT_G2_001 / Llama 3.1 8B Instruct: failed_fields=anomaly_times_1e3 error_tags=anomaly_times_1e3:MISMATCH
- QFT_G2_001 / Ministral 3 8B: failed_fields=anomaly_times_1e3 error_tags=anomaly_times_1e3:MISMATCH
- QFT_G2_001 / Mistral NeMo 12B: failed_fields=anomaly_times_1e3 error_tags=anomaly_times_1e3:MISMATCH
- QFT_G2_001 / Mistral Small 3.2 24B Instruct: failed_fields=anomaly_times_1e3 error_tags=anomaly_times_1e3:MISMATCH
- SR_ROCKET_001 / Gemma 3 12B IT: failed_fields=distance_ly;final_beta;lab_time_yr error_tags=distance_ly:MISMATCH;final_beta:MISMATCH;lab_time_yr:MISMATCH
- SR_ROCKET_001 / Gemma 3 27B IT: failed_fields=distance_ly;final_beta;lab_time_yr error_tags=distance_ly:MISMATCH;final_beta:MISMATCH;lab_time_yr:MISMATCH
- SR_ROCKET_001 / Granite 4.1 8B: failed_fields=distance_ly;lab_time_yr error_tags=distance_ly:MISMATCH;lab_time_yr:MISMATCH
- SR_ROCKET_001 / Llama 3.1 8B Instruct: failed_fields=distance_ly;final_beta;lab_time_yr error_tags=distance_ly:MISMATCH;final_beta:MISMATCH;lab_time_yr:MISMATCH
- SR_ROCKET_001 / Ministral 3 8B: failed_fields=distance_ly;final_beta;lab_time_yr error_tags=distance_ly:MISMATCH;final_beta:MISMATCH;lab_time_yr:MISMATCH
- SR_ROCKET_001 / Mistral NeMo 12B: failed_fields=distance_ly;final_beta;lab_time_yr error_tags=distance_ly:UNPARSEABLE:parse-fail:TokenError;final_beta:MISMATCH;lab_time_yr:UNPARSEABLE:parse-fail:TokenError
- SR_ROCKET_001 / Mistral Small 3.2 24B Instruct: failed_fields=distance_ly;final_beta;lab_time_yr error_tags=distance_ly:MISMATCH;final_beta:MISMATCH;lab_time_yr:MISMATCH
- STAT_ISING_001 / Mistral NeMo 12B: failed_fields=ratio_exact_mf;tc_exact error_tags=ratio_exact_mf:MISMATCH;tc_exact:MISMATCH

## Original Vs Structured Comparison

- status: not_generated: original subset is not a clean 1:1 scenario/model match (missing_pairs=0, non_singleton_pairs=40)
