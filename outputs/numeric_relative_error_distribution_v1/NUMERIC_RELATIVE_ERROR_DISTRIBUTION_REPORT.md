# Numeric Relative-Error Distribution v1

## 1. Purpose

Analyze numeric distance between extracted final-answer fields and gold values without changing deterministic labels.

## 2. Input Artifacts

- structured_prompt_pilot_v2..v5 clean autograde CSVs
- gold_fields from learning.db opened read-only
- existing normalized final-answer fields only

## 3. Row and Field Coverage

- clean rows represented: 252
- PASS rows: 117
- FAIL rows: 135
- numeric field comparisons total: 746
- included in distribution: 740
- excluded from distribution: 6
- protected inputs unchanged: yes

## 4. Relative-Error Definition

`relative_error = abs(extracted_value - expected_value) / abs(expected_value)`.

## 5. Handling of Zero/Near-Zero Gold Values

Expected values with `abs(expected_value) <= 1e-12` are retained in the field-level file but excluded from relative-error distribution statistics. This mirrors the autograder's special absolute-tolerance handling near zero.

## 6. Overall Numeric Error Distribution

- count: 740
- mean_rel_error: 3561130.74339
- median_rel_error: 0.00108678588195
- min_rel_error: 0
- max_rel_error: 2635088802.47
- stddev_rel_error: 96802310.2427
- p0_rel_error: 0
- p1_rel_error: 0
- p5_rel_error: 0
- p10_rel_error: 0
- p25_rel_error: 1.97999960401e-05
- p50_rel_error: 0.00108678588195
- p75_rel_error: 0.722934517168
- p90_rel_error: 2.53099598168
- p95_rel_error: 15.819639595
- p99_rel_error: 2653.54669884
- p100_rel_error: 2635088802.47

## 7. Distribution by Original PASS/FAIL

| subset | count | mean | median | p90 | p95 | max |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| all_numeric_comparisons | 740 | 3561130.74339 | 0.00108678588195 | 2.53099598168 | 15.819639595 | 2635088802.47 |
| original_PASS_rows | 342 | 0.000554920613327 | 8.09730661285e-05 | 0.00148272156855 | 0.00310470160983 | 0.00811481903088 |
| original_FAIL_rows | 398 | 6621197.86412 | 0.653979893651 | 11.5904751955 | 222.787356532 | 2635088802.47 |
| originally_failed_numeric_fields | 303 | 8697150.98961 | 0.907348547365 | 47.5470611318 | 516.781756313 | 2635088802.47 |
| originally_passed_numeric_fields | 437 | 0.000590356374431 | 8.72789082423e-05 | 0.0017862901658 | 0.00283244102559 | 0.00811481903088 |

## 8. Distribution for Original FAIL Rows

- count: 398
- mean_rel_error: 6621197.86412
- median_rel_error: 0.653979893651
- min_rel_error: 0
- max_rel_error: 2635088802.47
- stddev_rel_error: 131919007.599
- p0_rel_error: 0
- p1_rel_error: 0
- p5_rel_error: 0
- p10_rel_error: 8.5102334746e-05
- p25_rel_error: 0.0134803203449
- p50_rel_error: 0.653979893651
- p75_rel_error: 1
- p90_rel_error: 11.5904751955
- p95_rel_error: 222.787356532
- p99_rel_error: 16458.3253012
- p100_rel_error: 2635088802.47

## 9. Distribution by Batch

| batch | included | median | p95 | max | <=1% | >10% |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| V2 | 173 | 0.000521773465704 | 8.16505226057 | 41536.3180706 | 116 | 47 |
| V3 | 219 | 0.000692285999056 | 222.787356532 | 2635088802.47 | 126 | 85 |
| V4 | 173 | 0.0933333333333 | 8.98740567428 | 414.201514742 | 82 | 86 |
| V5 | 175 | 0.00108678588195 | 4.90035758683 | 1068.3427031 | 113 | 56 |

## 10. Distribution by Scenario

| scenario | included | median | p95 | max | >10% |
| --- | ---: | ---: | ---: | ---: | ---: |
| CM_APSIDAL_001 | 32 | 8.6816998986e-07 | 1.72059455381 | 6.01510035526 | 7 |
| CM_FOUCAULT_001 | 24 | 0.00239103215066 | 0.013089331586 | 0.0146532686001 | 0 |
| CM_KAPITZA_001 | 16 | 1.06869242223 | 8.98414209513 | 9.00045999087 | 13 |
| CM_TOP_001 | 24 | 6.78540741302e-05 | 40.993416773 | 653.273337189 | 6 |
| COS_AGE_001 | 23 | 0.0106282295972 | 0.892422323047 | 4.01164748971 | 8 |
| COS_CMB_001 | 24 | 0.000128967488229 | 0.667958376615 | 8.96101125749 | 7 |
| COS_DESITTER_001 | 24 | 0.499525139819 | 2.0821325275 | 3.89523117457 | 15 |
| COS_DL_001 | 32 | 0.000692285594456 | 27.0193786263 | 49.5400043364 | 9 |
| GR_CHIRP_001 | 24 | 0.913214285714 | 3.09272801955 | 3.09283128351 | 22 |
| GR_GPS_001 | 24 | 1.85358288671 | 1388.03351881 | 10010.6255998 | 15 |
| GR_ISCO_001 | 24 | 0.999999199281 | 38305.0353797 | 41536.3180706 | 21 |
| GR_PERI_001 | 24 | 0.00166645438902 | 101.742571197 | 414.201514742 | 10 |
| QFT_CASIMIR_001 | 24 | 0.999999998738 | 700.933525928 | 5290.79316719 | 21 |
| QFT_G2_001 | 16 | 0.00104958091177 | 2.89864475078 | 5.22837757553 | 5 |
| QFT_UNRUH_001 | 14 | 0.191907775133 | 31.3841832644 | 73.2067481103 | 10 |
| QFT_YUKAWA_001 | 24 | 0.000337049702865 | 0.00427713628346 | 0.742888312101 | 1 |
| QI_CLONE_001 | 24 | 1.99999600012e-06 | 0.000371399257202 | 0.000401999196002 | 0 |
| QI_HOLEVO_001 | 23 | 0.138071187457 | 0.653360950565 | 1.33333333333 | 13 |
| QI_TELEPORT_001 | 23 | 3.53571554846e-05 | 0.00100049949975 | 0.357142627551 | 1 |
| QI_WERNER_001 | 32 | 9.89949187335e-06 | 0.450549450549 | 1 | 2 |
| QM_AB_001 | 24 | 0.0961043540296 | 0.900619187144 | 0.900636319847 | 12 |
| QM_BERRY_001 | 16 | 2.08044135888e-07 | 2.54647961918e-06 | 2.54647961918e-06 | 0 |
| QM_RT_001 | 24 | 0.7612861957 | 15.3038151379 | 24.8974037763 | 15 |
| QM_TUNNEL_001 | 27 | 0.669149961342 | 2391.37744646 | 2635088802.47 | 18 |
| SR_BELL_001 | 24 | 9.999998e-06 | 0.00172982935997 | 0.001999997996 | 0 |
| SR_FIZEAU_001 | 16 | 0.000677463991096 | 0.00293056920253 | 0.00636065678756 | 0 |
| SR_ROCKET_001 | 22 | 0.109506113578 | 666.599563492 | 16348.9611146 | 11 |
| SR_TWIN_001 | 32 | 0 | 0.5 | 0.6 | 3 |
| STAT_BEC_001 | 24 | 0.330739667949 | 16.0080434679 | 18.3512413407 | 13 |
| STAT_ISING_001 | 24 | 8.15270680882e-05 | 0.51483697895 | 0.605687330776 | 2 |
| STAT_LANDAUER_001 | 16 | 0.55126746407 | 33.0737427895 | 104.887225229 | 10 |
| STAT_NEGT_001 | 16 | 0.00108678588195 | 1068.3427031 | 1068.3427031 | 4 |

## 11. Distribution by Model

| model | included | median | p95 | max | >10% |
| --- | ---: | ---: | ---: | ---: | ---: |
| Gemma 3 12B IT | 95 | 0.00109023369356 | 700.084314871 | 41536.3180706 | 36 |
| Gemma 3 27B IT | 95 | 0.000834217860529 | 9.65349362355 | 3307.50038658 | 31 |
| Gemma 4 31B IT | 95 | 0.000151320804348 | 3.09234938505 | 9.00749927892 | 11 |
| Granite 4.1 8B | 85 | 0.000460491024148 | 0.991891330739 | 1.99818981051 | 18 |
| Llama 3.1 8B Instruct | 90 | 0.114231399305 | 596.981137873 | 19994.4339998 | 46 |
| Ministral 3 8B | 93 | 0.0035554689444 | 4.18783924593 | 2635088802.47 | 40 |
| Mistral NeMo 12B | 92 | 0.413109088169 | 48.4937020273 | 1068.3427031 | 56 |
| Mistral Small 3.2 24B Instruct | 95 | 0.00108678588195 | 8.9424599946 | 149.447072397 | 36 |

## 12. Distribution by Field

See `numeric_relative_error_by_field.csv` for scenario-field summaries.

## 13. Relative-Error Bins

| bin | fields | share | row FAIL fields |
| --- | ---: | ---: | ---: |
| exact_or_zero_error | 108 | 0.145945945946 | 29 |
| gt_0_to_0_1_percent | 247 | 0.333783783784 | 42 |
| gt_0_1_to_0_5_percent | 76 | 0.102702702703 | 23 |
| gt_0_5_to_1_percent | 6 | 0.00810810810811 | 1 |
| gt_1_to_1_25_percent | 3 | 0.00405405405405 | 3 |
| gt_1_25_to_2_percent | 5 | 0.00675675675676 | 5 |
| gt_2_to_3_percent | 4 | 0.00540540540541 | 4 |
| gt_3_to_5_percent | 5 | 0.00675675675676 | 5 |
| gt_5_to_10_percent | 12 | 0.0162162162162 | 12 |
| gt_10_to_25_percent | 30 | 0.0405405405405 | 30 |
| gt_25_to_50_percent | 28 | 0.0378378378378 | 28 |
| gt_50_to_100_percent | 118 | 0.159459459459 | 118 |
| gt_100_to_1000_percent | 56 | 0.0756756756757 | 56 |
| gt_1000_percent | 42 | 0.0567567567568 | 42 |

## 14. Exploratory Threshold Table for Future Tolerance Layers

| threshold % | qualifying FAIL rows | share of FAIL rows | without blocker | with blocker |
| ---: | ---: | ---: | ---: | ---: |
| 1.25 | 0 | 0 | 0 | 0 |
| 2 | 2 | 0.0148148148148 | 1 | 1 |
| 3 | 4 | 0.0296296296296 | 3 | 1 |
| 5 | 4 | 0.0296296296296 | 3 | 1 |
| 10 | 5 | 0.037037037037 | 4 | 1 |
| 25 | 15 | 0.111111111111 | 14 | 1 |
| 50 | 25 | 0.185185185185 | 24 | 1 |
| 100 | 72 | 0.533333333333 | 69 | 3 |

## 15. Extreme-Error Examples

- V3 / QM_TUNNEL_001 / Ministral 3 8B / kappa_per_nm: rel_error=2635088802.47 extracted=2.70 \times 10^{10} expected=10.246334
- V2 / GR_ISCO_001 / Gemma 3 12B IT / f_orbital_hz: rel_error=41536.3180706 extracted=9.13e6 expected=219.802347
- V2 / GR_ISCO_001 / Gemma 3 12B IT / f_gw_hz: rel_error=41536.3179761 extracted=1.826e7 expected=439.604695
- V2 / GR_ISCO_001 / Llama 3.1 8B Instruct / r_isco_km: rel_error=19994.4339998 extracted=1.772\times10^{6} expected=88.620232
- V2 / SR_ROCKET_001 / Gemma 3 12B IT / distance_ly: rel_error=16348.9611146 extracted=9208.2 expected=0.563194
- V3 / GR_GPS_001 / Llama 3.1 8B Instruct / velocity_shift_us_day: rel_error=10010.6255998 extracted=-72200 expected=7.213057
- V3 / QFT_CASIMIR_001 / Llama 3.1 8B Instruct / pressure_double_d_pa: rel_error=5290.79316719 extracted=4300 expected=0.812579
- V3 / QM_TUNNEL_001 / Gemma 3 27B IT / kappa_per_nm: rel_error=3307.50038658 extracted=3.39 \times 10^4 expected=10.246334
- V3 / GR_GPS_001 / Llama 3.1 8B Instruct / grav_shift_us_day: rel_error=1630.69605903 extracted=74600 expected=45.719299
- V5 / STAT_NEGT_001 / Mistral NeMo 12B / abs_temperature_K: rel_error=1068.3427031 extracted=1.41 \times 10^3 expected=1.318567

## 16. Interpretation

This layer separates field-level numeric distance from row-level correctness. If failed numeric fields concentrate far above 10%, tolerance relaxation is not the main issue; if they cluster around 1-5%, future soft-fail layers may be useful.

## 17. Limitations

- Does not change labels.
- Does not revisit raw outputs.
- Non-numeric fields remain in field-level data but are excluded from numeric distribution statistics.
- Charts were skipped; CSV summaries are the source of truth.

## 18. Recommended Next Tolerance/Categorization Layer

Use the threshold table to test a small set of explicit tolerance alternatives, then separately classify unparseable/missing-field failures.
