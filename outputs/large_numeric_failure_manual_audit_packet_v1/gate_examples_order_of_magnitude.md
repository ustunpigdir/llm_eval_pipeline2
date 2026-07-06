# ORDER_OF_MAGNITUDE_GATE

The answer is at least 10 times too large or too small.

## Count Summary

- fields_detected: 50
- rows_detected: 33
- false_positive_risk: low

## Suggested Manual Decision Checklist

- Does the ratio heuristic match the actual scientific mistake?
- Could this be a field swap or unit/context issue instead?
- Should this gate become a formal diagnostic flag?

## Selected Audit Cards

### Card 001 - ORDER_OF_MAGNITUDE_GATE

**Scenario:** QM_TUNNEL_001  
**Model:** Ministral 3 8B  
**Batch:** V3  
**Field:** kappa_per_nm  

| Item | Value |
|---|---:|
| Gold value | 10.246334 |
| Model value | 2.70 \times 10^{10} |
| Relative error | 2635088802.47 |
| Relative error percent | 263508880247 |
| Model / gold ratio | 2635088803.47 |
| log10 ratio | 9.42079525568 |
| Original tolerance | rel=0.01; abs=0.10246334 |
| Original field pass? | false |
| Preliminary pattern | ORDER_OF_MAGNITUDE_GT10X |

**Plain-English diagnosis:**  
The model value is about 2635088803.5 times the gold value, indicating an order-of-magnitude scale error.

**Possible gate:**  
ORDER_OF_MAGNITUDE_GATE

**Audit question:**  
Does this look like a genuine order-of-magnitude mistake, or does the value correspond to another field/unit?

**Recommended manual decision options:**  
CONFIRM_GATE;REJECT_GATE_FALSE_POSITIVE;REASSIGN_TO_DIFFERENT_GATE;NEEDS_SCENARIO_CONTEXT;NEEDS_RAW_ANSWER_REVIEW

**Notes:**  
same-row pattern cluster

### Card 002 - ORDER_OF_MAGNITUDE_GATE

**Scenario:** GR_ISCO_001  
**Model:** Gemma 3 12B IT  
**Batch:** V2  
**Field:** f_orbital_hz  

| Item | Value |
|---|---:|
| Gold value | 219.802347 |
| Model value | 9.13e6 |
| Relative error | 41536.3180706 |
| Relative error percent | 4153631.80706 |
| Model / gold ratio | 41537.3180706 |
| log10 ratio | 4.61843845212 |
| Original tolerance | rel=0.01; abs=2.19802347 |
| Original field pass? | false |
| Preliminary pattern | ORDER_OF_MAGNITUDE_GT10X |

**Plain-English diagnosis:**  
The model value is about 41537.3 times the gold value, indicating an order-of-magnitude scale error.

**Possible gate:**  
ORDER_OF_MAGNITUDE_GATE

**Audit question:**  
Does this look like a genuine order-of-magnitude mistake, or does the value correspond to another field/unit?

**Recommended manual decision options:**  
CONFIRM_GATE;REJECT_GATE_FALSE_POSITIVE;REASSIGN_TO_DIFFERENT_GATE;NEEDS_SCENARIO_CONTEXT;NEEDS_RAW_ANSWER_REVIEW

**Notes:**  
same-row pattern cluster

### Card 003 - ORDER_OF_MAGNITUDE_GATE

**Scenario:** GR_ISCO_001  
**Model:** Llama 3.1 8B Instruct  
**Batch:** V2  
**Field:** r_isco_km  

| Item | Value |
|---|---:|
| Gold value | 88.620232 |
| Model value | 1.772\times10^{6} |
| Relative error | 19994.4339998 |
| Relative error percent | 1999443.39998 |
| Model / gold ratio | 19995.4339998 |
| log10 ratio | 4.30093083491 |
| Original tolerance | rel=0.01; abs=0.88620232 |
| Original field pass? | false |
| Preliminary pattern | ORDER_OF_MAGNITUDE_GT10X |

**Plain-English diagnosis:**  
The model value is about 19995.4 times the gold value, indicating an order-of-magnitude scale error.

**Possible gate:**  
ORDER_OF_MAGNITUDE_GATE

**Audit question:**  
Does this look like a genuine order-of-magnitude mistake, or does the value correspond to another field/unit?

**Recommended manual decision options:**  
CONFIRM_GATE;REJECT_GATE_FALSE_POSITIVE;REASSIGN_TO_DIFFERENT_GATE;NEEDS_SCENARIO_CONTEXT;NEEDS_RAW_ANSWER_REVIEW

**Notes:**  
same-row pattern cluster

### Card 004 - ORDER_OF_MAGNITUDE_GATE

**Scenario:** SR_ROCKET_001  
**Model:** Gemma 3 12B IT  
**Batch:** V2  
**Field:** distance_ly  

| Item | Value |
|---|---:|
| Gold value | 0.563194 |
| Model value | 9208.2 |
| Relative error | 16348.9611146 |
| Relative error percent | 1634896.11146 |
| Model / gold ratio | 16349.9611146 |
| log10 ratio | 4.21351672411 |
| Original tolerance | rel=0.01; abs=0.00563194 |
| Original field pass? | false |
| Preliminary pattern | ORDER_OF_MAGNITUDE_GT10X |

**Plain-English diagnosis:**  
The model value is about 16350.0 times the gold value, indicating an order-of-magnitude scale error.

**Possible gate:**  
ORDER_OF_MAGNITUDE_GATE

**Audit question:**  
Does this look like a genuine order-of-magnitude mistake, or does the value correspond to another field/unit?

**Recommended manual decision options:**  
CONFIRM_GATE;REJECT_GATE_FALSE_POSITIVE;REASSIGN_TO_DIFFERENT_GATE;NEEDS_SCENARIO_CONTEXT;NEEDS_RAW_ANSWER_REVIEW

**Notes:**  
same-row pattern cluster

### Card 005 - ORDER_OF_MAGNITUDE_GATE

**Scenario:** GR_GPS_001  
**Model:** Llama 3.1 8B Instruct  
**Batch:** V3  
**Field:** velocity_shift_us_day  

| Item | Value |
|---|---:|
| Gold value | 7.213057 |
| Model value | -72200 |
| Relative error | 10010.6255998 |
| Relative error percent | 1001062.55998 |
| Model / gold ratio | 10009.6255998 |
| log10 ratio | 4.00041783343 |
| Original tolerance | rel=0.01; abs=0.07213057 |
| Original field pass? | false |
| Preliminary pattern | ORDER_OF_MAGNITUDE_GT10X |

**Plain-English diagnosis:**  
The model value is about 10009.6 times the gold value, indicating an order-of-magnitude scale error.

**Possible gate:**  
ORDER_OF_MAGNITUDE_GATE

**Audit question:**  
Does this look like a genuine order-of-magnitude mistake, or does the value correspond to another field/unit?

**Recommended manual decision options:**  
CONFIRM_GATE;REJECT_GATE_FALSE_POSITIVE;REASSIGN_TO_DIFFERENT_GATE;NEEDS_SCENARIO_CONTEXT;NEEDS_RAW_ANSWER_REVIEW

**Notes:**  
same-row pattern cluster

### Card 006 - ORDER_OF_MAGNITUDE_GATE

**Scenario:** QFT_CASIMIR_001  
**Model:** Llama 3.1 8B Instruct  
**Batch:** V3  
**Field:** pressure_double_d_pa  

| Item | Value |
|---|---:|
| Gold value | 0.812579 |
| Model value | 4300 |
| Relative error | 5290.79316719 |
| Relative error percent | 529079.316719 |
| Model / gold ratio | 5291.79316719 |
| log10 ratio | 3.72360286119 |
| Original tolerance | rel=0.01; abs=0.00812579 |
| Original field pass? | false |
| Preliminary pattern | ORDER_OF_MAGNITUDE_GT10X |

**Plain-English diagnosis:**  
The model value is about 5291.8 times the gold value, indicating an order-of-magnitude scale error.

**Possible gate:**  
ORDER_OF_MAGNITUDE_GATE

**Audit question:**  
Does this look like a genuine order-of-magnitude mistake, or does the value correspond to another field/unit?

**Recommended manual decision options:**  
CONFIRM_GATE;REJECT_GATE_FALSE_POSITIVE;REASSIGN_TO_DIFFERENT_GATE;NEEDS_SCENARIO_CONTEXT;NEEDS_RAW_ANSWER_REVIEW

**Notes:**  
same-row pattern cluster

### Card 007 - ORDER_OF_MAGNITUDE_GATE

**Scenario:** QM_TUNNEL_001  
**Model:** Gemma 3 27B IT  
**Batch:** V3  
**Field:** kappa_per_nm  

| Item | Value |
|---|---:|
| Gold value | 10.246334 |
| Model value | 3.39 \times 10^4 |
| Relative error | 3307.50038658 |
| Relative error percent | 330750.038658 |
| Model / gold ratio | 3308.50038658 |
| log10 ratio | 3.51963118972 |
| Original tolerance | rel=0.01; abs=0.10246334 |
| Original field pass? | false |
| Preliminary pattern | ORDER_OF_MAGNITUDE_GT10X |

**Plain-English diagnosis:**  
The model value is about 3308.5 times the gold value, indicating an order-of-magnitude scale error.

**Possible gate:**  
ORDER_OF_MAGNITUDE_GATE

**Audit question:**  
Does this look like a genuine order-of-magnitude mistake, or does the value correspond to another field/unit?

**Recommended manual decision options:**  
CONFIRM_GATE;REJECT_GATE_FALSE_POSITIVE;REASSIGN_TO_DIFFERENT_GATE;NEEDS_SCENARIO_CONTEXT;NEEDS_RAW_ANSWER_REVIEW

**Notes:**  
same-row pattern cluster

### Card 008 - ORDER_OF_MAGNITUDE_GATE

**Scenario:** CM_APSIDAL_001  
**Model:** Llama 3.1 8B Instruct  
**Batch:** V3  
**Field:** precession_per_period_deg  

| Item | Value |
|---|---:|
| Gold value | -105.441559 |
| Model value | 6.86 |
| Relative error | 1.06505973608 |
| Relative error percent | 106.505973608 |
| Model / gold ratio | 0.0650597360762 |
| log10 ratio | -1.18668770283 |
| Original tolerance | rel=0.01; abs=1.05441559 |
| Original field pass? | false |
| Preliminary pattern | ORDER_OF_MAGNITUDE_GT10X |

**Plain-English diagnosis:**  
The model value is about 0.065 times the gold value, indicating an order-of-magnitude scale error.

**Possible gate:**  
ORDER_OF_MAGNITUDE_GATE

**Audit question:**  
Does this look like a genuine order-of-magnitude mistake, or does the value correspond to another field/unit?

**Recommended manual decision options:**  
CONFIRM_GATE;REJECT_GATE_FALSE_POSITIVE;REASSIGN_TO_DIFFERENT_GATE;NEEDS_SCENARIO_CONTEXT;NEEDS_RAW_ANSWER_REVIEW

**Notes:**  
No raw final-answer block included; normalized extracted value is shown.

### Card 009 - ORDER_OF_MAGNITUDE_GATE

**Scenario:** CM_APSIDAL_001  
**Model:** Ministral 3 8B  
**Batch:** V3  
**Field:** precession_per_period_deg  

| Item | Value |
|---|---:|
| Gold value | -105.441559 |
| Model value | 9.4712 |
| Relative error | 1.08982416506 |
| Relative error percent | 108.982416506 |
| Model / gold ratio | 0.0898241650619 |
| log10 ratio | -1.04660681098 |
| Original tolerance | rel=0.01; abs=1.05441559 |
| Original field pass? | false |
| Preliminary pattern | ORDER_OF_MAGNITUDE_GT10X |

**Plain-English diagnosis:**  
The model value is about 0.090 times the gold value, indicating an order-of-magnitude scale error.

**Possible gate:**  
ORDER_OF_MAGNITUDE_GATE

**Audit question:**  
Does this look like a genuine order-of-magnitude mistake, or does the value correspond to another field/unit?

**Recommended manual decision options:**  
CONFIRM_GATE;REJECT_GATE_FALSE_POSITIVE;REASSIGN_TO_DIFFERENT_GATE;NEEDS_SCENARIO_CONTEXT;NEEDS_RAW_ANSWER_REVIEW

**Notes:**  
No raw final-answer block included; normalized extracted value is shown.

### Card 010 - ORDER_OF_MAGNITUDE_GATE

**Scenario:** GR_GPS_001  
**Model:** Gemma 3 12B IT  
**Batch:** V3  
**Field:** grav_shift_us_day  

| Item | Value |
|---|---:|
| Gold value | 45.719299 |
| Model value | 544 |
| Relative error | 10.8986951222 |
| Relative error percent | 1089.86951222 |
| Model / gold ratio | 11.8986951222 |
| log10 ratio | 1.07549933683 |
| Original tolerance | rel=0.01; abs=0.45719299 |
| Original field pass? | false |
| Preliminary pattern | ORDER_OF_MAGNITUDE_GT10X |

**Plain-English diagnosis:**  
The model value is about 11.90 times the gold value, indicating an order-of-magnitude scale error.

**Possible gate:**  
ORDER_OF_MAGNITUDE_GATE

**Audit question:**  
Does this look like a genuine order-of-magnitude mistake, or does the value correspond to another field/unit?

**Recommended manual decision options:**  
CONFIRM_GATE;REJECT_GATE_FALSE_POSITIVE;REASSIGN_TO_DIFFERENT_GATE;NEEDS_SCENARIO_CONTEXT;NEEDS_RAW_ANSWER_REVIEW

**Notes:**  
No raw final-answer block included; normalized extracted value is shown.

### Card 011 - ORDER_OF_MAGNITUDE_GATE

**Scenario:** QM_RT_001  
**Model:** Gemma 3 27B IT  
**Batch:** V5  
**Field:** energy_unit_ev  

| Item | Value |
|---|---:|
| Gold value | 2.350189 |
| Model value | 33.2 |
| Relative error | 13.1265234413 |
| Relative error percent | 1312.65234413 |
| Model / gold ratio | 14.1265234413 |
| log10 ratio | 1.15003529447 |
| Original tolerance | rel=0.02; abs=0.04700378 |
| Original field pass? | false |
| Preliminary pattern | ORDER_OF_MAGNITUDE_GT10X |

**Plain-English diagnosis:**  
The model value is about 14.13 times the gold value, indicating an order-of-magnitude scale error.

**Possible gate:**  
ORDER_OF_MAGNITUDE_GATE

**Audit question:**  
Does this look like a genuine order-of-magnitude mistake, or does the value correspond to another field/unit?

**Recommended manual decision options:**  
CONFIRM_GATE;REJECT_GATE_FALSE_POSITIVE;REASSIGN_TO_DIFFERENT_GATE;NEEDS_SCENARIO_CONTEXT;NEEDS_RAW_ANSWER_REVIEW

**Notes:**  
No raw final-answer block included; normalized extracted value is shown.
