# WRONG_FIELD_SCALE_GATE

The answer looks closer to another field's expected value than to its own.

## Count Summary

- fields_detected: 5
- rows_detected: 5
- false_positive_risk: medium

## Suggested Manual Decision Checklist

- Does the ratio heuristic match the actual scientific mistake?
- Could this be a field swap or unit/context issue instead?
- Should this gate become a formal diagnostic flag?

## Selected Audit Cards

### Card 038 - WRONG_FIELD_SCALE_GATE

**Scenario:** QFT_CASIMIR_001  
**Model:** Ministral 3 8B  
**Batch:** V3  
**Field:** energy_per_area_uJ_m2  

| Item | Value |
|---|---:|
| Gold value | 0.433375 |
| Model value | 13.6 |
| Relative error | 30.3815979233 |
| Relative error percent | 3038.15979233 |
| Model / gold ratio | 31.3815979233 |
| log10 ratio | 1.49667505371 |
| Original tolerance | rel=0.01; abs=0.00433375 |
| Original field pass? | false |
| Preliminary pattern | WRONG_FIELD_SCALE |

**Plain-English diagnosis:**  
The extracted value is closer to pressure_pa than to this field's gold value, suggesting a field-scale mixup.

**Possible gate:**  
WRONG_FIELD_SCALE_GATE

**Audit question:**  
Does this value genuinely correspond to another field, or is the ratio match accidental?

**Recommended manual decision options:**  
CONFIRM_GATE;REJECT_GATE_FALSE_POSITIVE;REASSIGN_TO_DIFFERENT_GATE;NEEDS_SCENARIO_CONTEXT;NEEDS_RAW_ANSWER_REVIEW

**Notes:**  
No raw final-answer block included; normalized extracted value is shown.

### Card 039 - WRONG_FIELD_SCALE_GATE

**Scenario:** STAT_BEC_001  
**Model:** Gemma 4 31B IT  
**Batch:** V3  
**Field:** tc_nK  

| Item | Value |
|---|---:|
| Gold value | 85.817924 |
| Model value | 183.5 |
| Relative error | 1.13824794923 |
| Relative error percent | 113.824794923 |
| Model / gold ratio | 2.13824794923 |
| log10 ratio | 0.330058064174 |
| Original tolerance | rel=0.01; abs=0.85817924 |
| Original field pass? | false |
| Preliminary pattern | WRONG_FIELD_SCALE |

**Plain-English diagnosis:**  
The extracted value is closer to tc_no_zeta_nK than to this field's gold value, suggesting a field-scale mixup.

**Possible gate:**  
WRONG_FIELD_SCALE_GATE

**Audit question:**  
Does this value genuinely correspond to another field, or is the ratio match accidental?

**Recommended manual decision options:**  
CONFIRM_GATE;REJECT_GATE_FALSE_POSITIVE;REASSIGN_TO_DIFFERENT_GATE;NEEDS_SCENARIO_CONTEXT;NEEDS_RAW_ANSWER_REVIEW

**Notes:**  
No raw final-answer block included; normalized extracted value is shown.

### Card 040 - WRONG_FIELD_SCALE_GATE

**Scenario:** GR_PERI_001  
**Model:** Llama 3.1 8B Instruct  
**Batch:** V4  
**Field:** advance_arcsec_orbit  

| Item | Value |
|---|---:|
| Gold value | 0.103516 |
| Model value | 42.98 |
| Relative error | 414.201514742 |
| Relative error percent | 41420.1514742 |
| Model / gold ratio | 415.201514742 |
| log10 ratio | 2.61825892924 |
| Original tolerance | rel=0.01; abs=0.00103516 |
| Original field pass? | false |
| Preliminary pattern | WRONG_FIELD_SCALE |

**Plain-English diagnosis:**  
The extracted value is closer to advance_arcsec_century than to this field's gold value, suggesting a field-scale mixup.

**Possible gate:**  
WRONG_FIELD_SCALE_GATE

**Audit question:**  
Does this value genuinely correspond to another field, or is the ratio match accidental?

**Recommended manual decision options:**  
CONFIRM_GATE;REJECT_GATE_FALSE_POSITIVE;REASSIGN_TO_DIFFERENT_GATE;NEEDS_SCENARIO_CONTEXT;NEEDS_RAW_ANSWER_REVIEW

**Notes:**  
No raw final-answer block included; normalized extracted value is shown.

### Card 041 - WRONG_FIELD_SCALE_GATE

**Scenario:** QFT_UNRUH_001  
**Model:** Gemma 3 12B IT  
**Batch:** V4  
**Field:** unruh_temp_K  

| Item | Value |
|---|---:|
| Gold value | 0.405501 |
| Model value | 2.64 |
| Relative error | 5.51046483239 |
| Relative error percent | 551.046483239 |
| Model / gold ratio | 6.51046483239 |
| log10 ratio | 0.813611997314 |
| Original tolerance | rel=0.01; abs=0.00405501 |
| Original field pass? | false |
| Preliminary pattern | COMMON_FACTOR_2_OR_PI |

**Plain-English diagnosis:**  
The extracted value is closer to accel_for_1K_e20 than to this field's gold value, suggesting a field-scale mixup.

**Possible gate:**  
WRONG_FIELD_SCALE_GATE

**Audit question:**  
Does this value genuinely correspond to another field, or is the ratio match accidental?

**Recommended manual decision options:**  
CONFIRM_GATE;REJECT_GATE_FALSE_POSITIVE;REASSIGN_TO_DIFFERENT_GATE;NEEDS_SCENARIO_CONTEXT;NEEDS_RAW_ANSWER_REVIEW

**Notes:**  
No raw final-answer block included; normalized extracted value is shown.

### Card 042 - WRONG_FIELD_SCALE_GATE

**Scenario:** QM_RT_001  
**Model:** Ministral 3 8B  
**Batch:** V5  
**Field:** energy_unit_ev  

| Item | Value |
|---|---:|
| Gold value | 2.350189 |
| Model value | 9.47 |
| Relative error | 3.02946316232 |
| Relative error percent | 302.946316232 |
| Model / gold ratio | 4.02946316232 |
| log10 ratio | 0.605247189771 |
| Original tolerance | rel=0.02; abs=0.04700378 |
| Original field pass? | false |
| Preliminary pattern | WRONG_FIELD_SCALE |

**Plain-English diagnosis:**  
The extracted value is closer to first_resonance_ev than to this field's gold value, suggesting a field-scale mixup.

**Possible gate:**  
WRONG_FIELD_SCALE_GATE

**Audit question:**  
Does this value genuinely correspond to another field, or is the ratio match accidental?

**Recommended manual decision options:**  
CONFIRM_GATE;REJECT_GATE_FALSE_POSITIVE;REASSIGN_TO_DIFFERENT_GATE;NEEDS_SCENARIO_CONTEXT;NEEDS_RAW_ANSWER_REVIEW

**Notes:**  
No raw final-answer block included; normalized extracted value is shown.
