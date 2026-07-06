# EXTREME_EXPLOSION_GATE

The answer is more than 1000% away from gold.

## Count Summary

- fields_detected: 48
- rows_detected: 31
- false_positive_risk: low

## Suggested Manual Decision Checklist

- Does the ratio heuristic match the actual scientific mistake?
- Could this be a field swap or unit/context issue instead?
- Should this gate become a formal diagnostic flag?

## Selected Audit Cards

### Card 012 - EXTREME_EXPLOSION_GATE

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
The numeric distance is extreme: relative error is 263508880247.00%, so this is not a tolerance-boundary error.

**Possible gate:**  
EXTREME_EXPLOSION_GATE

**Audit question:**  
Is this an extreme magnitude failure suitable for a generic gate, or does it need scenario context?

**Recommended manual decision options:**  
CONFIRM_GATE;REJECT_GATE_FALSE_POSITIVE;REASSIGN_TO_DIFFERENT_GATE;NEEDS_SCENARIO_CONTEXT;NEEDS_RAW_ANSWER_REVIEW

**Notes:**  
same-row pattern cluster

### Card 013 - EXTREME_EXPLOSION_GATE

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
The numeric distance is extreme: relative error is 4153631.81%, so this is not a tolerance-boundary error.

**Possible gate:**  
EXTREME_EXPLOSION_GATE

**Audit question:**  
Is this an extreme magnitude failure suitable for a generic gate, or does it need scenario context?

**Recommended manual decision options:**  
CONFIRM_GATE;REJECT_GATE_FALSE_POSITIVE;REASSIGN_TO_DIFFERENT_GATE;NEEDS_SCENARIO_CONTEXT;NEEDS_RAW_ANSWER_REVIEW

**Notes:**  
same-row pattern cluster

### Card 014 - EXTREME_EXPLOSION_GATE

**Scenario:** GR_ISCO_001  
**Model:** Gemma 3 12B IT  
**Batch:** V2  
**Field:** f_gw_hz  

| Item | Value |
|---|---:|
| Gold value | 439.604695 |
| Model value | 1.826e7 |
| Relative error | 41536.3179761 |
| Relative error percent | 4153631.79761 |
| Model / gold ratio | 41537.3179761 |
| log10 ratio | 4.61843845114 |
| Original tolerance | rel=0.01; abs=4.39604695 |
| Original field pass? | false |
| Preliminary pattern | ORDER_OF_MAGNITUDE_GT10X |

**Plain-English diagnosis:**  
The numeric distance is extreme: relative error is 4153631.80%, so this is not a tolerance-boundary error.

**Possible gate:**  
EXTREME_EXPLOSION_GATE

**Audit question:**  
Is this an extreme magnitude failure suitable for a generic gate, or does it need scenario context?

**Recommended manual decision options:**  
CONFIRM_GATE;REJECT_GATE_FALSE_POSITIVE;REASSIGN_TO_DIFFERENT_GATE;NEEDS_SCENARIO_CONTEXT;NEEDS_RAW_ANSWER_REVIEW

**Notes:**  
same-row pattern cluster

### Card 015 - EXTREME_EXPLOSION_GATE

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
The numeric distance is extreme: relative error is 1999443.40%, so this is not a tolerance-boundary error.

**Possible gate:**  
EXTREME_EXPLOSION_GATE

**Audit question:**  
Is this an extreme magnitude failure suitable for a generic gate, or does it need scenario context?

**Recommended manual decision options:**  
CONFIRM_GATE;REJECT_GATE_FALSE_POSITIVE;REASSIGN_TO_DIFFERENT_GATE;NEEDS_SCENARIO_CONTEXT;NEEDS_RAW_ANSWER_REVIEW

**Notes:**  
same-row pattern cluster

### Card 016 - EXTREME_EXPLOSION_GATE

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
The numeric distance is extreme: relative error is 1634896.11%, so this is not a tolerance-boundary error.

**Possible gate:**  
EXTREME_EXPLOSION_GATE

**Audit question:**  
Is this an extreme magnitude failure suitable for a generic gate, or does it need scenario context?

**Recommended manual decision options:**  
CONFIRM_GATE;REJECT_GATE_FALSE_POSITIVE;REASSIGN_TO_DIFFERENT_GATE;NEEDS_SCENARIO_CONTEXT;NEEDS_RAW_ANSWER_REVIEW

**Notes:**  
same-row pattern cluster

### Card 017 - EXTREME_EXPLOSION_GATE

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
The numeric distance is extreme: relative error is 1001062.56%, so this is not a tolerance-boundary error.

**Possible gate:**  
EXTREME_EXPLOSION_GATE

**Audit question:**  
Is this an extreme magnitude failure suitable for a generic gate, or does it need scenario context?

**Recommended manual decision options:**  
CONFIRM_GATE;REJECT_GATE_FALSE_POSITIVE;REASSIGN_TO_DIFFERENT_GATE;NEEDS_SCENARIO_CONTEXT;NEEDS_RAW_ANSWER_REVIEW

**Notes:**  
same-row pattern cluster

### Card 018 - EXTREME_EXPLOSION_GATE

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
The numeric distance is extreme: relative error is 529079.32%, so this is not a tolerance-boundary error.

**Possible gate:**  
EXTREME_EXPLOSION_GATE

**Audit question:**  
Is this an extreme magnitude failure suitable for a generic gate, or does it need scenario context?

**Recommended manual decision options:**  
CONFIRM_GATE;REJECT_GATE_FALSE_POSITIVE;REASSIGN_TO_DIFFERENT_GATE;NEEDS_SCENARIO_CONTEXT;NEEDS_RAW_ANSWER_REVIEW

**Notes:**  
same-row pattern cluster

### Card 019 - EXTREME_EXPLOSION_GATE

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
The numeric distance is extreme: relative error is 330750.04%, so this is not a tolerance-boundary error.

**Possible gate:**  
EXTREME_EXPLOSION_GATE

**Audit question:**  
Is this an extreme magnitude failure suitable for a generic gate, or does it need scenario context?

**Recommended manual decision options:**  
CONFIRM_GATE;REJECT_GATE_FALSE_POSITIVE;REASSIGN_TO_DIFFERENT_GATE;NEEDS_SCENARIO_CONTEXT;NEEDS_RAW_ANSWER_REVIEW

**Notes:**  
same-row pattern cluster

### Card 020 - EXTREME_EXPLOSION_GATE

**Scenario:** GR_GPS_001  
**Model:** Llama 3.1 8B Instruct  
**Batch:** V3  
**Field:** grav_shift_us_day  

| Item | Value |
|---|---:|
| Gold value | 45.719299 |
| Model value | 74600 |
| Relative error | 1630.69605903 |
| Relative error percent | 163069.605903 |
| Model / gold ratio | 1631.69605903 |
| log10 ratio | 3.2126392646 |
| Original tolerance | rel=0.01; abs=0.45719299 |
| Original field pass? | false |
| Preliminary pattern | ORDER_OF_MAGNITUDE_GT10X |

**Plain-English diagnosis:**  
The numeric distance is extreme: relative error is 163069.61%, so this is not a tolerance-boundary error.

**Possible gate:**  
EXTREME_EXPLOSION_GATE

**Audit question:**  
Is this an extreme magnitude failure suitable for a generic gate, or does it need scenario context?

**Recommended manual decision options:**  
CONFIRM_GATE;REJECT_GATE_FALSE_POSITIVE;REASSIGN_TO_DIFFERENT_GATE;NEEDS_SCENARIO_CONTEXT;NEEDS_RAW_ANSWER_REVIEW

**Notes:**  
same-row pattern cluster

### Card 021 - EXTREME_EXPLOSION_GATE

**Scenario:** STAT_NEGT_001  
**Model:** Mistral NeMo 12B  
**Batch:** V5  
**Field:** abs_temperature_K  

| Item | Value |
|---|---:|
| Gold value | 1.318567 |
| Model value | 1.41 \times 10^3 |
| Relative error | 1068.3427031 |
| Relative error percent | 106834.27031 |
| Model / gold ratio | 1069.3427031 |
| log10 ratio | 3.02911691027 |
| Original tolerance | rel=0.01; abs=0.01318567 |
| Original field pass? | false |
| Preliminary pattern | ORDER_OF_MAGNITUDE_GT10X |

**Plain-English diagnosis:**  
The numeric distance is extreme: relative error is 106834.27%, so this is not a tolerance-boundary error.

**Possible gate:**  
EXTREME_EXPLOSION_GATE

**Audit question:**  
Is this an extreme magnitude failure suitable for a generic gate, or does it need scenario context?

**Recommended manual decision options:**  
CONFIRM_GATE;REJECT_GATE_FALSE_POSITIVE;REASSIGN_TO_DIFFERENT_GATE;NEEDS_SCENARIO_CONTEXT;NEEDS_RAW_ANSWER_REVIEW

**Notes:**  
No raw final-answer block included; normalized extracted value is shown.
