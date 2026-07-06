# SIGN_FLIP_GATE

The magnitude is similar but the sign is wrong.

## Count Summary

- fields_detected: 6
- rows_detected: 6
- false_positive_risk: medium

## Suggested Manual Decision Checklist

- Does the ratio heuristic match the actual scientific mistake?
- Could this be a field swap or unit/context issue instead?
- Should this gate become a formal diagnostic flag?

## Selected Audit Cards

### Card 032 - SIGN_FLIP_GATE

**Scenario:** GR_GPS_001  
**Model:** Gemma 3 12B IT  
**Batch:** V3  
**Field:** velocity_shift_us_day  

| Item | Value |
|---|---:|
| Gold value | 7.213057 |
| Model value | -7.21 |
| Relative error | 1.99957618524 |
| Relative error percent | 199.957618524 |
| Model / gold ratio | 0.999576185243 |
| log10 ratio | -0.000184099425116 |
| Original tolerance | rel=0.01; abs=0.07213057 |
| Original field pass? | false |
| Preliminary pattern | SIGN_FLIP |

**Plain-English diagnosis:**  
The model value has the opposite sign while the magnitude is close, producing 199.96% relative error.

**Possible gate:**  
SIGN_FLIP_GATE

**Audit question:**  
Is this a genuine sign-convention mistake, or did the prompt allow the opposite convention?

**Recommended manual decision options:**  
CONFIRM_GATE;REJECT_GATE_FALSE_POSITIVE;REASSIGN_TO_DIFFERENT_GATE;NEEDS_SCENARIO_CONTEXT;NEEDS_RAW_ANSWER_REVIEW

**Notes:**  
No raw final-answer block included; normalized extracted value is shown.

### Card 033 - SIGN_FLIP_GATE

**Scenario:** GR_GPS_001  
**Model:** Gemma 3 27B IT  
**Batch:** V3  
**Field:** velocity_shift_us_day  

| Item | Value |
|---|---:|
| Gold value | 7.213057 |
| Model value | -7.21 |
| Relative error | 1.99957618524 |
| Relative error percent | 199.957618524 |
| Model / gold ratio | 0.999576185243 |
| log10 ratio | -0.000184099425116 |
| Original tolerance | rel=0.01; abs=0.07213057 |
| Original field pass? | false |
| Preliminary pattern | SIGN_FLIP |

**Plain-English diagnosis:**  
The model value has the opposite sign while the magnitude is close, producing 199.96% relative error.

**Possible gate:**  
SIGN_FLIP_GATE

**Audit question:**  
Is this a genuine sign-convention mistake, or did the prompt allow the opposite convention?

**Recommended manual decision options:**  
CONFIRM_GATE;REJECT_GATE_FALSE_POSITIVE;REASSIGN_TO_DIFFERENT_GATE;NEEDS_SCENARIO_CONTEXT;NEEDS_RAW_ANSWER_REVIEW

**Notes:**  
No raw final-answer block included; normalized extracted value is shown.

### Card 034 - SIGN_FLIP_GATE

**Scenario:** GR_GPS_001  
**Model:** Gemma 4 31B IT  
**Batch:** V3  
**Field:** velocity_shift_us_day  

| Item | Value |
|---|---:|
| Gold value | 7.213057 |
| Model value | -7.2 |
| Relative error | 1.99818981051 |
| Relative error percent | 199.818981051 |
| Model / gold ratio | 0.998189810506 |
| log10 ratio | -0.000786867713277 |
| Original tolerance | rel=0.01; abs=0.07213057 |
| Original field pass? | false |
| Preliminary pattern | SIGN_FLIP |

**Plain-English diagnosis:**  
The model value has the opposite sign while the magnitude is close, producing 199.82% relative error.

**Possible gate:**  
SIGN_FLIP_GATE

**Audit question:**  
Is this a genuine sign-convention mistake, or did the prompt allow the opposite convention?

**Recommended manual decision options:**  
CONFIRM_GATE;REJECT_GATE_FALSE_POSITIVE;REASSIGN_TO_DIFFERENT_GATE;NEEDS_SCENARIO_CONTEXT;NEEDS_RAW_ANSWER_REVIEW

**Notes:**  
No raw final-answer block included; normalized extracted value is shown.

### Card 035 - SIGN_FLIP_GATE

**Scenario:** GR_GPS_001  
**Model:** Granite 4.1 8B  
**Batch:** V3  
**Field:** velocity_shift_us_day  

| Item | Value |
|---|---:|
| Gold value | 7.213057 |
| Model value | -7.2 |
| Relative error | 1.99818981051 |
| Relative error percent | 199.818981051 |
| Model / gold ratio | 0.998189810506 |
| log10 ratio | -0.000786867713277 |
| Original tolerance | rel=0.01; abs=0.07213057 |
| Original field pass? | false |
| Preliminary pattern | SIGN_FLIP |

**Plain-English diagnosis:**  
The model value has the opposite sign while the magnitude is close, producing 199.82% relative error.

**Possible gate:**  
SIGN_FLIP_GATE

**Audit question:**  
Is this a genuine sign-convention mistake, or did the prompt allow the opposite convention?

**Recommended manual decision options:**  
CONFIRM_GATE;REJECT_GATE_FALSE_POSITIVE;REASSIGN_TO_DIFFERENT_GATE;NEEDS_SCENARIO_CONTEXT;NEEDS_RAW_ANSWER_REVIEW

**Notes:**  
No raw final-answer block included; normalized extracted value is shown.

### Card 036 - SIGN_FLIP_GATE

**Scenario:** GR_GPS_001  
**Model:** Mistral NeMo 12B  
**Batch:** V3  
**Field:** velocity_shift_us_day  

| Item | Value |
|---|---:|
| Gold value | 7.213057 |
| Model value | -7.21 |
| Relative error | 1.99957618524 |
| Relative error percent | 199.957618524 |
| Model / gold ratio | 0.999576185243 |
| log10 ratio | -0.000184099425116 |
| Original tolerance | rel=0.01; abs=0.07213057 |
| Original field pass? | false |
| Preliminary pattern | SIGN_FLIP |

**Plain-English diagnosis:**  
The model value has the opposite sign while the magnitude is close, producing 199.96% relative error.

**Possible gate:**  
SIGN_FLIP_GATE

**Audit question:**  
Is this a genuine sign-convention mistake, or did the prompt allow the opposite convention?

**Recommended manual decision options:**  
CONFIRM_GATE;REJECT_GATE_FALSE_POSITIVE;REASSIGN_TO_DIFFERENT_GATE;NEEDS_SCENARIO_CONTEXT;NEEDS_RAW_ANSWER_REVIEW

**Notes:**  
No raw final-answer block included; normalized extracted value is shown.

### Card 037 - SIGN_FLIP_GATE

**Scenario:** GR_GPS_001  
**Model:** Mistral Small 3.2 24B Instruct  
**Batch:** V3  
**Field:** velocity_shift_us_day  

| Item | Value |
|---|---:|
| Gold value | 7.213057 |
| Model value | -7.2 |
| Relative error | 1.99818981051 |
| Relative error percent | 199.818981051 |
| Model / gold ratio | 0.998189810506 |
| log10 ratio | -0.000786867713277 |
| Original tolerance | rel=0.01; abs=0.07213057 |
| Original field pass? | false |
| Preliminary pattern | SIGN_FLIP |

**Plain-English diagnosis:**  
The model value has the opposite sign while the magnitude is close, producing 199.82% relative error.

**Possible gate:**  
SIGN_FLIP_GATE

**Audit question:**  
Is this a genuine sign-convention mistake, or did the prompt allow the opposite convention?

**Recommended manual decision options:**  
CONFIRM_GATE;REJECT_GATE_FALSE_POSITIVE;REASSIGN_TO_DIFFERENT_GATE;NEEDS_SCENARIO_CONTEXT;NEEDS_RAW_ANSWER_REVIEW

**Notes:**  
No raw final-answer block included; normalized extracted value is shown.
