# POWER_OF_TEN_SCALE_GATE

The answer looks shifted by decimal or scientific-notation scale.

## Count Summary

- fields_detected: 16
- rows_detected: 12
- false_positive_risk: medium

## Suggested Manual Decision Checklist

- Does the ratio heuristic match the actual scientific mistake?
- Could this be a field swap or unit/context issue instead?
- Should this gate become a formal diagnostic flag?

## Selected Audit Cards

### Card 022 - POWER_OF_TEN_SCALE_GATE

**Scenario:** COS_CMB_001  
**Model:** Llama 3.1 8B Instruct  
**Batch:** V2  
**Field:** T_rec_K  

| Item | Value |
|---|---:|
| Gold value | 3000.225 |
| Model value | 29885.275 |
| Relative error | 8.96101125749 |
| Relative error percent | 896.101125749 |
| Model / gold ratio | 9.96101125749 |
| log10 ratio | 0.998303430919 |
| Original tolerance | rel=0.01; abs=30.00225 |
| Original field pass? | false |
| Preliminary pattern | DECIMAL_OR_POWER_OF_TEN_SCALE |

**Plain-English diagnosis:**  
The model value is about 9.961 times the gold value, consistent with a decimal or power-of-ten scale mistake.

**Possible gate:**  
POWER_OF_TEN_SCALE_GATE

**Audit question:**  
Does this look like a decimal/scientific-notation scale mistake, or a different conceptual error?

**Recommended manual decision options:**  
CONFIRM_GATE;REJECT_GATE_FALSE_POSITIVE;REASSIGN_TO_DIFFERENT_GATE;NEEDS_SCENARIO_CONTEXT;NEEDS_RAW_ANSWER_REVIEW

**Notes:**  
No raw final-answer block included; normalized extracted value is shown.

### Card 023 - POWER_OF_TEN_SCALE_GATE

**Scenario:** GR_ISCO_001  
**Model:** Ministral 3 8B  
**Batch:** V2  
**Field:** r_isco_km  

| Item | Value |
|---|---:|
| Gold value | 88.620232 |
| Model value | 8.86 \times 10^{3} \, \mathrm{km} |
| Relative error | 98.9771699988 |
| Relative error percent | 9897.71699988 |
| Model / gold ratio | 99.9771699988 |
| log10 ratio | 1.99990083925 |
| Original tolerance | rel=0.01; abs=0.88620232 |
| Original field pass? | false |
| Preliminary pattern | DECIMAL_OR_POWER_OF_TEN_SCALE |

**Plain-English diagnosis:**  
The model value is about 99.98 times the gold value, consistent with a decimal or power-of-ten scale mistake.

**Possible gate:**  
POWER_OF_TEN_SCALE_GATE

**Audit question:**  
Does this look like a decimal/scientific-notation scale mistake, or a different conceptual error?

**Recommended manual decision options:**  
CONFIRM_GATE;REJECT_GATE_FALSE_POSITIVE;REASSIGN_TO_DIFFERENT_GATE;NEEDS_SCENARIO_CONTEXT;NEEDS_RAW_ANSWER_REVIEW

**Notes:**  
No raw final-answer block included; normalized extracted value is shown.

### Card 024 - POWER_OF_TEN_SCALE_GATE

**Scenario:** GR_ISCO_001  
**Model:** Mistral Small 3.2 24B Instruct  
**Batch:** V2  
**Field:** r_isco_km  

| Item | Value |
|---|---:|
| Gold value | 88.620232 |
| Model value | 8859.6 |
| Relative error | 98.9726563568 |
| Relative error percent | 9897.26563568 |
| Model / gold ratio | 99.9726563568 |
| log10 ratio | 1.99988123183 |
| Original tolerance | rel=0.01; abs=0.88620232 |
| Original field pass? | false |
| Preliminary pattern | DECIMAL_OR_POWER_OF_TEN_SCALE |

**Plain-English diagnosis:**  
The model value is about 99.97 times the gold value, consistent with a decimal or power-of-ten scale mistake.

**Possible gate:**  
POWER_OF_TEN_SCALE_GATE

**Audit question:**  
Does this look like a decimal/scientific-notation scale mistake, or a different conceptual error?

**Recommended manual decision options:**  
CONFIRM_GATE;REJECT_GATE_FALSE_POSITIVE;REASSIGN_TO_DIFFERENT_GATE;NEEDS_SCENARIO_CONTEXT;NEEDS_RAW_ANSWER_REVIEW

**Notes:**  
No raw final-answer block included; normalized extracted value is shown.

### Card 025 - POWER_OF_TEN_SCALE_GATE

**Scenario:** COS_DL_001  
**Model:** Mistral NeMo 12B  
**Batch:** V3  
**Field:** hubble_distance_mpc  

| Item | Value |
|---|---:|
| Gold value | 4282.7494 |
| Model value | 42857.14 |
| Relative error | 9.00692218882 |
| Relative error percent | 900.692218882 |
| Model / gold ratio | 10.0069221888 |
| log10 ratio | 1.00030052284 |
| Original tolerance | rel=0.01; abs=42.827494 |
| Original field pass? | false |
| Preliminary pattern | DECIMAL_OR_POWER_OF_TEN_SCALE |

**Plain-English diagnosis:**  
The model value is about 10.01 times the gold value, consistent with a decimal or power-of-ten scale mistake.

**Possible gate:**  
POWER_OF_TEN_SCALE_GATE

**Audit question:**  
Does this look like a decimal/scientific-notation scale mistake, or a different conceptual error?

**Recommended manual decision options:**  
CONFIRM_GATE;REJECT_GATE_FALSE_POSITIVE;REASSIGN_TO_DIFFERENT_GATE;NEEDS_SCENARIO_CONTEXT;NEEDS_RAW_ANSWER_REVIEW

**Notes:**  
No raw final-answer block included; normalized extracted value is shown.

### Card 026 - POWER_OF_TEN_SCALE_GATE

**Scenario:** GR_GPS_001  
**Model:** Ministral 3 8B  
**Batch:** V3  
**Field:** velocity_shift_us_day  

| Item | Value |
|---|---:|
| Gold value | 7.213057 |
| Model value | -72.2. |
| Relative error | 11.0096255998 |
| Relative error percent | 1100.96255998 |
| Model / gold ratio | 10.0096255998 |
| log10 ratio | 1.00041783343 |
| Original tolerance | rel=0.01; abs=0.07213057 |
| Original field pass? | false |
| Preliminary pattern | DECIMAL_OR_POWER_OF_TEN_SCALE |

**Plain-English diagnosis:**  
The model value is about 10.01 times the gold value, consistent with a decimal or power-of-ten scale mistake.

**Possible gate:**  
POWER_OF_TEN_SCALE_GATE

**Audit question:**  
Does this look like a decimal/scientific-notation scale mistake, or a different conceptual error?

**Recommended manual decision options:**  
CONFIRM_GATE;REJECT_GATE_FALSE_POSITIVE;REASSIGN_TO_DIFFERENT_GATE;NEEDS_SCENARIO_CONTEXT;NEEDS_RAW_ANSWER_REVIEW

**Notes:**  
No raw final-answer block included; normalized extracted value is shown.

### Card 027 - POWER_OF_TEN_SCALE_GATE

**Scenario:** QFT_CASIMIR_001  
**Model:** Gemma 4 31B IT  
**Batch:** V3  
**Field:** energy_per_area_uJ_m2  

| Item | Value |
|---|---:|
| Gold value | 0.433375 |
| Model value | 4.337 |
| Relative error | 9.00749927892 |
| Relative error percent | 900.749927892 |
| Model / gold ratio | 10.0074992789 |
| log10 ratio | 1.00032556748 |
| Original tolerance | rel=0.01; abs=0.00433375 |
| Original field pass? | false |
| Preliminary pattern | DECIMAL_OR_POWER_OF_TEN_SCALE |

**Plain-English diagnosis:**  
The model value is about 10.01 times the gold value, consistent with a decimal or power-of-ten scale mistake.

**Possible gate:**  
POWER_OF_TEN_SCALE_GATE

**Audit question:**  
Does this look like a decimal/scientific-notation scale mistake, or a different conceptual error?

**Recommended manual decision options:**  
CONFIRM_GATE;REJECT_GATE_FALSE_POSITIVE;REASSIGN_TO_DIFFERENT_GATE;NEEDS_SCENARIO_CONTEXT;NEEDS_RAW_ANSWER_REVIEW

**Notes:**  
No raw final-answer block included; normalized extracted value is shown.

### Card 028 - POWER_OF_TEN_SCALE_GATE

**Scenario:** CM_KAPITZA_001  
**Model:** Gemma 3 12B IT  
**Batch:** V4  
**Field:** f_min_hz  

| Item | Value |
|---|---:|
| Gold value | 15.763572 |
| Model value | 155.9 |
| Relative error | 8.88989043854 |
| Relative error percent | 888.989043854 |
| Model / gold ratio | 9.88989043854 |
| log10 ratio | 0.995191480454 |
| Original tolerance | rel=0.01; abs=0.15763572 |
| Original field pass? | false |
| Preliminary pattern | DECIMAL_OR_POWER_OF_TEN_SCALE |

**Plain-English diagnosis:**  
The model value is about 9.890 times the gold value, consistent with a decimal or power-of-ten scale mistake.

**Possible gate:**  
POWER_OF_TEN_SCALE_GATE

**Audit question:**  
Does this look like a decimal/scientific-notation scale mistake, or a different conceptual error?

**Recommended manual decision options:**  
CONFIRM_GATE;REJECT_GATE_FALSE_POSITIVE;REASSIGN_TO_DIFFERENT_GATE;NEEDS_SCENARIO_CONTEXT;NEEDS_RAW_ANSWER_REVIEW

**Notes:**  
No raw final-answer block included; normalized extracted value is shown.

### Card 029 - POWER_OF_TEN_SCALE_GATE

**Scenario:** CM_KAPITZA_001  
**Model:** Mistral Small 3.2 24B Instruct  
**Batch:** V4  
**Field:** f_min_hz  

| Item | Value |
|---|---:|
| Gold value | 15.763572 |
| Model value | 157.3 |
| Relative error | 8.97870279655 |
| Relative error percent | 897.870279655 |
| Model / gold ratio | 9.97870279655 |
| log10 ratio | 0.999074087889 |
| Original tolerance | rel=0.01; abs=0.15763572 |
| Original field pass? | false |
| Preliminary pattern | DECIMAL_OR_POWER_OF_TEN_SCALE |

**Plain-English diagnosis:**  
The model value is about 9.979 times the gold value, consistent with a decimal or power-of-ten scale mistake.

**Possible gate:**  
POWER_OF_TEN_SCALE_GATE

**Audit question:**  
Does this look like a decimal/scientific-notation scale mistake, or a different conceptual error?

**Recommended manual decision options:**  
CONFIRM_GATE;REJECT_GATE_FALSE_POSITIVE;REASSIGN_TO_DIFFERENT_GATE;NEEDS_SCENARIO_CONTEXT;NEEDS_RAW_ANSWER_REVIEW

**Notes:**  
No raw final-answer block included; normalized extracted value is shown.

### Card 030 - POWER_OF_TEN_SCALE_GATE

**Scenario:** QFT_UNRUH_001  
**Model:** Mistral Small 3.2 24B Instruct  
**Batch:** V4  
**Field:** unruh_temp_K  

| Item | Value |
|---|---:|
| Gold value | 0.405501 |
| Model value | 4.00 |
| Relative error | 8.86434065514 |
| Relative error percent | 886.434065514 |
| Model / gold ratio | 9.86434065514 |
| log10 ratio | 0.994068061772 |
| Original tolerance | rel=0.01; abs=0.00405501 |
| Original field pass? | false |
| Preliminary pattern | DECIMAL_OR_POWER_OF_TEN_SCALE |

**Plain-English diagnosis:**  
The model value is about 9.864 times the gold value, consistent with a decimal or power-of-ten scale mistake.

**Possible gate:**  
POWER_OF_TEN_SCALE_GATE

**Audit question:**  
Does this look like a decimal/scientific-notation scale mistake, or a different conceptual error?

**Recommended manual decision options:**  
CONFIRM_GATE;REJECT_GATE_FALSE_POSITIVE;REASSIGN_TO_DIFFERENT_GATE;NEEDS_SCENARIO_CONTEXT;NEEDS_RAW_ANSWER_REVIEW

**Notes:**  
No raw final-answer block included; normalized extracted value is shown.

### Card 031 - POWER_OF_TEN_SCALE_GATE

**Scenario:** STAT_LANDAUER_001  
**Model:** Gemma 3 12B IT  
**Batch:** V4  
**Field:** landauer_zJ  

| Item | Value |
|---|---:|
| Gold value | 2.870979 |
| Model value | 29.1 |
| Relative error | 9.13591530973 |
| Relative error percent | 913.591530973 |
| Model / gold ratio | 10.1359153097 |
| log10 ratio | 1.00586297316 |
| Original tolerance | rel=0.01; abs=0.02870979 |
| Original field pass? | false |
| Preliminary pattern | DECIMAL_OR_POWER_OF_TEN_SCALE |

**Plain-English diagnosis:**  
The model value is about 10.14 times the gold value, consistent with a decimal or power-of-ten scale mistake.

**Possible gate:**  
POWER_OF_TEN_SCALE_GATE

**Audit question:**  
Does this look like a decimal/scientific-notation scale mistake, or a different conceptual error?

**Recommended manual decision options:**  
CONFIRM_GATE;REJECT_GATE_FALSE_POSITIVE;REASSIGN_TO_DIFFERENT_GATE;NEEDS_SCENARIO_CONTEXT;NEEDS_RAW_ANSWER_REVIEW

**Notes:**  
No raw final-answer block included; normalized extracted value is shown.
