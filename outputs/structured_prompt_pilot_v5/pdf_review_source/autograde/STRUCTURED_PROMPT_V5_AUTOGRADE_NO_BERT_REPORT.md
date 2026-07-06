# Structured Prompt v5 Autograde No BERT Report

## Inputs

- raw_runs: /Users/upigdir/Desktop/Pipeline SQL proj/outputs/structured_prompt_pilot_v5/structured_prompt_pilot_v5_runs.json
- review_layer_csv: /Users/upigdir/Desktop/Pipeline SQL proj/outputs/structured_prompt_pilot_v5/review_layer_v1/review_layer_v1.csv
- review_layer_json: /Users/upigdir/Desktop/Pipeline SQL proj/outputs/structured_prompt_pilot_v5/review_layer_v1/review_layer_v1.json

## Safety

- learning_db_modified: no
- db_backup_created: no
- BERTScore was not run.

## Counts

- CLEAN rows autograded: 64
- REVIEW rows excluded: 0

## Extraction Status Distribution

- OK: 64

## Deterministic Grade Distribution

- FAIL: 27
- PASS: 37
- overall_pass_rate: 0.578125

## Summary By Scenario

| scenario_id | clean_rows | pass_count | fail_count | pass_rate | most_common_failure_mode |
|---|---:|---:|---:|---:|---|
| CM_TOP_001 | 8 | 6 | 2 | 0.75 | numeric_mismatch |
| COS_AGE_001 | 8 | 1 | 7 | 0.125 | numeric_mismatch |
| GR_CHIRP_001 | 8 | 0 | 8 | 0.0 | numeric_mismatch |
| QFT_YUKAWA_001 | 8 | 7 | 1 | 0.875 | numeric_mismatch |
| QI_CLONE_001 | 8 | 8 | 0 | 1.0 | none |
| QM_RT_001 | 8 | 1 | 7 | 0.125 | numeric_mismatch |
| SR_FIZEAU_001 | 8 | 8 | 0 | 1.0 | none |
| STAT_NEGT_001 | 8 | 6 | 2 | 0.75 | numeric_mismatch |

## Summary By Model

| model_name | clean_rows | pass_count | fail_count | pass_rate | most_common_failure_mode |
|---|---:|---:|---:|---:|---|
| Gemma 3 12B IT | 8 | 5 | 3 | 0.625 | numeric_mismatch |
| Gemma 3 27B IT | 8 | 5 | 3 | 0.625 | numeric_mismatch |
| Gemma 4 31B IT | 8 | 7 | 1 | 0.875 | numeric_mismatch |
| Granite 4.1 8B | 8 | 5 | 3 | 0.625 | numeric_mismatch |
| Llama 3.1 8B Instruct | 8 | 3 | 5 | 0.375 | numeric_mismatch |
| Ministral 3 8B | 8 | 5 | 3 | 0.625 | numeric_mismatch |
| Mistral NeMo 12B | 8 | 2 | 6 | 0.25 | numeric_mismatch |
| Mistral Small 3.2 24B Instruct | 8 | 5 | 3 | 0.625 | numeric_mismatch |

## Failed Fields And Failure Tags

- numeric_mismatch: 26
- unparseable_value: 1
- CM_TOP_001 / Llama 3.1 8B Instruct: failed_fields=precession_double_spin;precession_period_s;precession_rad_s error_tags=precession_double_spin:MISMATCH;precession_period_s:MISMATCH;precession_rad_s:MISMATCH
- CM_TOP_001 / Mistral NeMo 12B: failed_fields=precession_double_spin;precession_period_s;precession_rad_s error_tags=precession_double_spin:MISMATCH;precession_period_s:MISMATCH;precession_rad_s:MISMATCH
- COS_AGE_001 / Gemma 3 12B IT: failed_fields=hubble_time_gyr;lcdm_age_gyr;matter_age_gyr error_tags=hubble_time_gyr:MISMATCH;lcdm_age_gyr:MISMATCH;matter_age_gyr:MISMATCH
- COS_AGE_001 / Gemma 3 27B IT: failed_fields=lcdm_age_gyr error_tags=lcdm_age_gyr:MISMATCH
- COS_AGE_001 / Granite 4.1 8B: failed_fields=lcdm_age_gyr error_tags=lcdm_age_gyr:MISMATCH
- COS_AGE_001 / Llama 3.1 8B Instruct: failed_fields=hubble_time_gyr;lcdm_age_gyr;matter_age_gyr error_tags=hubble_time_gyr:UNPARSEABLE:parse-fail:SympifyError;lcdm_age_gyr:MISMATCH;matter_age_gyr:MISMATCH
- COS_AGE_001 / Ministral 3 8B: failed_fields=lcdm_age_gyr error_tags=lcdm_age_gyr:MISMATCH
- COS_AGE_001 / Mistral NeMo 12B: failed_fields=hubble_time_gyr;lcdm_age_gyr;matter_age_gyr error_tags=hubble_time_gyr:MISMATCH;lcdm_age_gyr:MISMATCH;matter_age_gyr:MISMATCH
- COS_AGE_001 / Mistral Small 3.2 24B Instruct: failed_fields=lcdm_age_gyr error_tags=lcdm_age_gyr:MISMATCH
- GR_CHIRP_001 / Gemma 3 12B IT: failed_fields=chirp_mass_msun;each_mass_msun;total_mass_msun error_tags=chirp_mass_msun:MISMATCH;each_mass_msun:MISMATCH;total_mass_msun:MISMATCH
- GR_CHIRP_001 / Gemma 3 27B IT: failed_fields=chirp_mass_msun;each_mass_msun;total_mass_msun error_tags=chirp_mass_msun:MISMATCH;each_mass_msun:MISMATCH;total_mass_msun:MISMATCH
- GR_CHIRP_001 / Gemma 4 31B IT: failed_fields=chirp_mass_msun;each_mass_msun;total_mass_msun error_tags=chirp_mass_msun:MISMATCH;each_mass_msun:MISMATCH;total_mass_msun:MISMATCH
- GR_CHIRP_001 / Granite 4.1 8B: failed_fields=chirp_mass_msun;each_mass_msun;total_mass_msun error_tags=chirp_mass_msun:MISMATCH;each_mass_msun:MISMATCH;total_mass_msun:MISMATCH
- GR_CHIRP_001 / Llama 3.1 8B Instruct: failed_fields=chirp_mass_msun;each_mass_msun;total_mass_msun error_tags=chirp_mass_msun:MISMATCH;each_mass_msun:MISMATCH;total_mass_msun:MISMATCH
- GR_CHIRP_001 / Ministral 3 8B: failed_fields=chirp_mass_msun;each_mass_msun;total_mass_msun error_tags=chirp_mass_msun:MISMATCH;each_mass_msun:MISMATCH;total_mass_msun:MISMATCH
- GR_CHIRP_001 / Mistral NeMo 12B: failed_fields=chirp_mass_msun;each_mass_msun;total_mass_msun error_tags=chirp_mass_msun:MISMATCH;each_mass_msun:MISMATCH;total_mass_msun:MISMATCH
- GR_CHIRP_001 / Mistral Small 3.2 24B Instruct: failed_fields=chirp_mass_msun;each_mass_msun;total_mass_msun error_tags=chirp_mass_msun:MISMATCH;each_mass_msun:MISMATCH;total_mass_msun:MISMATCH
- QFT_YUKAWA_001 / Mistral NeMo 12B: failed_fields=nonreduced_fm error_tags=nonreduced_fm:MISMATCH
- QM_RT_001 / Gemma 3 12B IT: failed_fields=energy_unit_ev;first_resonance_ev error_tags=energy_unit_ev:MISMATCH;first_resonance_ev:MISMATCH
- QM_RT_001 / Gemma 3 27B IT: failed_fields=energy_unit_ev;first_resonance_ev error_tags=energy_unit_ev:MISMATCH;first_resonance_ev:MISMATCH
- QM_RT_001 / Granite 4.1 8B: failed_fields=energy_unit_ev;first_resonance_ev;n_lowest error_tags=energy_unit_ev:MISMATCH;first_resonance_ev:MISMATCH;n_lowest:MISMATCH
- QM_RT_001 / Llama 3.1 8B Instruct: failed_fields=energy_unit_ev;first_resonance_ev error_tags=energy_unit_ev:MISMATCH;first_resonance_ev:MISMATCH
- QM_RT_001 / Ministral 3 8B: failed_fields=energy_unit_ev;first_resonance_ev error_tags=energy_unit_ev:MISMATCH;first_resonance_ev:MISMATCH
- QM_RT_001 / Mistral NeMo 12B: failed_fields=energy_unit_ev;first_resonance_ev error_tags=energy_unit_ev:MISMATCH;first_resonance_ev:MISMATCH
- QM_RT_001 / Mistral Small 3.2 24B Instruct: failed_fields=energy_unit_ev;first_resonance_ev error_tags=energy_unit_ev:MISMATCH;first_resonance_ev:MISMATCH
- STAT_NEGT_001 / Llama 3.1 8B Instruct: failed_fields=abs_temperature_K;temperature_K error_tags=abs_temperature_K:MISMATCH;temperature_K:MISMATCH
- STAT_NEGT_001 / Mistral NeMo 12B: failed_fields=abs_temperature_K;temperature_K error_tags=abs_temperature_K:MISMATCH;temperature_K:MISMATCH
