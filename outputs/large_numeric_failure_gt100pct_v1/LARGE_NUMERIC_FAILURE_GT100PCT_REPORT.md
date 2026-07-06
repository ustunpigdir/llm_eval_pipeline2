# Large Numeric Failure >100% v1 Report

## 1. Purpose

Inspect numeric comparisons where relative error is greater than 100% to identify preliminary scenario-independent logical gates.

## 2. Inputs

- input_artifact: outputs/numeric_relative_error_distribution_v1/numeric_relative_error_field_level.csv
- optional metric/context artifacts aligned by source_run_id

## 3. Definition of >100% Relative-Error Failure

`abs(extracted_value - expected_value) / abs(expected_value) > 1.0`.

## 4. Coverage

- source field comparisons: 746
- included numeric comparisons: 740
- rows with >100% numeric failure: 62
- protected inputs unchanged: yes

## 5. Overall Count of >100% Failures

- gt100_field_count: 98

## 6. >1000% Extreme Subset

- gt1000_field_count: 42

## 7. Results by Scenario

| scenario | rows | fields >100% | fields >1000% | median rel_error | pattern |
| --- | ---: | ---: | ---: | ---: | --- |
| CM_APSIDAL_001 | 3 | 4 | 0 | 1.79068015256 | LARGE_NUMERIC_GT100PCT_UNCLASSIFIED |
| CM_KAPITZA_001 | 4 | 8 | 0 | 5.52612237886 | DECIMAL_OR_POWER_OF_TEN_SCALE |
| CM_TOP_001 | 2 | 2 | 2 | 350.662241872 | ORDER_OF_MAGNITUDE_GT10X |
| COS_AGE_001 | 1 | 1 | 0 | 4.01164748971 | LARGE_NUMERIC_GT100PCT_UNCLASSIFIED |
| COS_CMB_001 | 1 | 1 | 0 | 8.96101125749 | DECIMAL_OR_POWER_OF_TEN_SCALE |
| COS_DESITTER_001 | 3 | 3 | 0 | 2.0821325275 | COMMON_FACTOR_2_OR_PI |
| COS_DL_001 | 1 | 3 | 2 | 49.0346031609 | ORDER_OF_MAGNITUDE_GT10X |
| GR_CHIRP_001 | 1 | 3 | 0 | 3.09283128351 | LARGE_NUMERIC_GT100PCT_UNCLASSIFIED |
| GR_GPS_001 | 8 | 14 | 5 | 1.99957618524 | SIGN_FLIP |
| GR_ISCO_001 | 5 | 7 | 5 | 98.9771699988 | ORDER_OF_MAGNITUDE_GT10X |
| GR_PERI_001 | 5 | 7 | 5 | 45.5307194418 | ORDER_OF_MAGNITUDE_GT10X |
| QFT_CASIMIR_001 | 6 | 11 | 7 | 149.447072397 | ORDER_OF_MAGNITUDE_GT10X |
| QFT_G2_001 | 2 | 2 | 0 | 3.67522235903 | COMMON_FACTOR_2_OR_PI |
| QFT_UNRUH_001 | 3 | 4 | 1 | 7.18740274377 | COMMON_FACTOR_2_OR_PI |
| QI_HOLEVO_001 | 1 | 1 | 0 | 1.33333333333 | LARGE_NUMERIC_GT100PCT_UNCLASSIFIED |
| QM_RT_001 | 4 | 8 | 3 | 7.33465028214 | ORDER_OF_MAGNITUDE_GT10X |
| QM_TUNNEL_001 | 3 | 5 | 5 | 253.757252833 | ORDER_OF_MAGNITUDE_GT10X |
| SR_ROCKET_001 | 2 | 3 | 2 | 701.58499046 | ORDER_OF_MAGNITUDE_GT10X |
| STAT_BEC_001 | 3 | 6 | 2 | 2.89662116584 | LARGE_NUMERIC_GT100PCT_UNCLASSIFIED |
| STAT_LANDAUER_001 | 3 | 3 | 1 | 9.13591530973 | DECIMAL_OR_POWER_OF_TEN_SCALE |
| STAT_NEGT_001 | 1 | 2 | 2 | 1068.3427031 | ORDER_OF_MAGNITUDE_GT10X |

## 8. Results by Model

| model | rows | fields >100% | fields >1000% | median rel_error | pattern |
| --- | ---: | ---: | ---: | ---: | --- |
| Gemma 3 12B IT | 13 | 24 | 14 | 14.3169170016 | ORDER_OF_MAGNITUDE_GT10X |
| Gemma 3 27B IT | 9 | 14 | 5 | 5.68814646188 | LARGE_NUMERIC_GT100PCT_UNCLASSIFIED |
| Gemma 4 31B IT | 4 | 9 | 0 | 3.09283128351 | LARGE_NUMERIC_GT100PCT_UNCLASSIFIED |
| Granite 4.1 8B | 1 | 1 | 0 | 1.99818981051 | SIGN_FLIP |
| Llama 3.1 8B Instruct | 8 | 12 | 8 | 471.190537837 | ORDER_OF_MAGNITUDE_GT10X |
| Ministral 3 8B | 8 | 11 | 4 | 3.02946316232 | LARGE_NUMERIC_GT100PCT_UNCLASSIFIED |
| Mistral NeMo 12B | 9 | 14 | 8 | 45.3535779674 | ORDER_OF_MAGNITUDE_GT10X |
| Mistral Small 3.2 24B Instruct | 10 | 13 | 3 | 8.86434065514 | DECIMAL_OR_POWER_OF_TEN_SCALE |

## 9. Results by Field

See `large_numeric_failure_by_field.csv`.

## 10. Preliminary Failure-Pattern Taxonomy

| pattern | fields | rows | median rel_error | max rel_error |
| --- | ---: | ---: | ---: | ---: |
| COMMON_FACTOR_2_OR_PI | 9 | 8 | 2.16235431919 | 5.51046483239 |
| DECIMAL_OR_POWER_OF_TEN_SCALE | 16 | 12 | 9.00282051279 | 98.9771699988 |
| LARGE_NUMERIC_GT100PCT_UNCLASSIFIED | 24 | 17 | 3.09248707032 | 8.16505227308 |
| ORDER_OF_MAGNITUDE_GT10X | 39 | 25 | 222.787356532 | 2635088802.47 |
| SIGN_FLIP | 6 | 6 | 1.99888299788 | 1.99957618524 |
| WRONG_FIELD_SCALE | 4 | 4 | 16.7055305428 | 414.201514742 |

## 11. Scenario-Independent Gate Candidates

| gate | fields | rows | risk | recommendation |
| --- | ---: | ---: | --- | --- |
| SIGN_FLIP_GATE | 6 | 6 | medium | useful_candidate |
| ZERO_SUBSTITUTION_GATE | 0 | 0 | high | not_observed_in_current_data |
| RECIPROCAL_INVERSION_GATE | 0 | 0 | high | not_observed_in_current_data |
| POWER_OF_TEN_SCALE_GATE | 16 | 12 | medium | useful_candidate |
| UNIT_SCALE_GATE | 0 | 0 | high | not_observed_in_current_data |
| WRONG_FIELD_SCALE_GATE | 5 | 5 | medium | useful_candidate |
| ORDER_OF_MAGNITUDE_GATE | 50 | 33 | low | useful_candidate |
| EXTREME_EXPLOSION_GATE | 48 | 31 | low | useful_candidate |

## 12. Extreme Examples

- V3 / QM_TUNNEL_001 / Ministral 3 8B / kappa_per_nm: rel_error=2635088802.47, pattern=ORDER_OF_MAGNITUDE_GT10X
- V2 / GR_ISCO_001 / Gemma 3 12B IT / f_orbital_hz: rel_error=41536.3180706, pattern=ORDER_OF_MAGNITUDE_GT10X
- V2 / GR_ISCO_001 / Gemma 3 12B IT / f_gw_hz: rel_error=41536.3179761, pattern=ORDER_OF_MAGNITUDE_GT10X
- V2 / GR_ISCO_001 / Llama 3.1 8B Instruct / r_isco_km: rel_error=19994.4339998, pattern=ORDER_OF_MAGNITUDE_GT10X
- V2 / SR_ROCKET_001 / Gemma 3 12B IT / distance_ly: rel_error=16348.9611146, pattern=ORDER_OF_MAGNITUDE_GT10X
- V3 / GR_GPS_001 / Llama 3.1 8B Instruct / velocity_shift_us_day: rel_error=10010.6255998, pattern=ORDER_OF_MAGNITUDE_GT10X
- V3 / QFT_CASIMIR_001 / Llama 3.1 8B Instruct / pressure_double_d_pa: rel_error=5290.79316719, pattern=ORDER_OF_MAGNITUDE_GT10X
- V3 / QM_TUNNEL_001 / Gemma 3 27B IT / kappa_per_nm: rel_error=3307.50038658, pattern=ORDER_OF_MAGNITUDE_GT10X
- V3 / GR_GPS_001 / Llama 3.1 8B Instruct / grav_shift_us_day: rel_error=1630.69605903, pattern=ORDER_OF_MAGNITUDE_GT10X
- V5 / STAT_NEGT_001 / Mistral NeMo 12B / abs_temperature_K: rel_error=1068.3427031, pattern=ORDER_OF_MAGNITUDE_GT10X

## 13. Interaction With Text/Reasoning Metrics

| metric | rows | mean | median |
| --- | ---: | ---: | ---: |
| bertscore_reasoning_only_v2_f1 | 62 | 0.585714186181 | 0.673797726631 |
| rouge_l_f1 | 62 | 0.754682790609 | 0.831024696065 |
| chrf_score | 62 | 0.750183587675 | 0.850889028012 |
| roscoe_reasoning_alignment | 62 | 0.919370130185 | 0.932082414627 |

## 14. Interpretation

These are not tolerance-boundary failures. They are large numeric-distance cases where ratio heuristics can suggest structural mistakes, but all pattern labels are preliminary.

## 15. Limitations

- Ratio heuristics do not prove cause.
- This layer does not change grades or implement Phase 2 semantics.
- It only inspects numeric comparisons with rel_error > 1.0.

## 16. Recommended Next Layer

Manually audit the high-count gate candidates, then convert only robust, low-risk checks into scenario-independent diagnostic flags.
