# Gate Audit Cards

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

### Card 043 - UNCLASSIFIED_LARGE_GATE

**Scenario:** GR_ISCO_001  
**Model:** Gemma 3 27B IT  
**Batch:** V2  
**Field:** f_orbital_hz  

| Item | Value |
|---|---:|
| Gold value | 219.802347 |
| Model value | 2014.5 |
| Relative error | 8.16505227308 |
| Relative error percent | 816.505227308 |
| Model / gold ratio | 9.16505227308 |
| log10 ratio | 0.962134946313 |
| Original tolerance | rel=0.01; abs=2.19802347 |
| Original field pass? | false |
| Preliminary pattern | LARGE_NUMERIC_GT100PCT_UNCLASSIFIED |

**Plain-English diagnosis:**  
The field is more than 100% away from gold but did not match a simple gate heuristic.

**Possible gate:**  
UNCLASSIFIED_LARGE_GATE

**Audit question:**  
What is the simplest human-readable explanation for this large numeric miss?

**Recommended manual decision options:**  
CONFIRM_GATE;REJECT_GATE_FALSE_POSITIVE;REASSIGN_TO_DIFFERENT_GATE;NEEDS_SCENARIO_CONTEXT;NEEDS_RAW_ANSWER_REVIEW

**Notes:**  
No raw final-answer block included; normalized extracted value is shown.

### Card 044 - UNCLASSIFIED_LARGE_GATE

**Scenario:** CM_APSIDAL_001  
**Model:** Gemma 3 12B IT  
**Batch:** V3  
**Field:** precession_per_period_deg  

| Item | Value |
|---|---:|
| Gold value | -105.441559 |
| Model value | 528.8 |
| Relative error | 6.01510035526 |
| Relative error percent | 601.510035526 |
| Model / gold ratio | 5.01510035526 |
| log10 ratio | 0.700279627945 |
| Original tolerance | rel=0.01; abs=1.05441559 |
| Original field pass? | false |
| Preliminary pattern | LARGE_NUMERIC_GT100PCT_UNCLASSIFIED |

**Plain-English diagnosis:**  
The field is more than 100% away from gold but did not match a simple gate heuristic.

**Possible gate:**  
UNCLASSIFIED_LARGE_GATE

**Audit question:**  
What is the simplest human-readable explanation for this large numeric miss?

**Recommended manual decision options:**  
CONFIRM_GATE;REJECT_GATE_FALSE_POSITIVE;REASSIGN_TO_DIFFERENT_GATE;NEEDS_SCENARIO_CONTEXT;NEEDS_RAW_ANSWER_REVIEW

**Notes:**  
No raw final-answer block included; normalized extracted value is shown.

### Card 045 - UNCLASSIFIED_LARGE_GATE

**Scenario:** QM_RT_001  
**Model:** Ministral 3 8B  
**Batch:** V5  
**Field:** first_resonance_ev  

| Item | Value |
|---|---:|
| Gold value | 11.151697 |
| Model value | 77.23 |
| Relative error | 5.92540337134 |
| Relative error percent | 592.540337134 |
| Model / gold ratio | 6.92540337134 |
| log10 ratio | 0.840445074032 |
| Original tolerance | rel=0.02; abs=0.22303394 |
| Original field pass? | false |
| Preliminary pattern | LARGE_NUMERIC_GT100PCT_UNCLASSIFIED |

**Plain-English diagnosis:**  
The field is more than 100% away from gold but did not match a simple gate heuristic.

**Possible gate:**  
UNCLASSIFIED_LARGE_GATE

**Audit question:**  
What is the simplest human-readable explanation for this large numeric miss?

**Recommended manual decision options:**  
CONFIRM_GATE;REJECT_GATE_FALSE_POSITIVE;REASSIGN_TO_DIFFERENT_GATE;NEEDS_SCENARIO_CONTEXT;NEEDS_RAW_ANSWER_REVIEW

**Notes:**  
No raw final-answer block included; normalized extracted value is shown.

### Card 046 - UNCLASSIFIED_LARGE_GATE

**Scenario:** QM_RT_001  
**Model:** Mistral Small 3.2 24B Instruct  
**Batch:** V5  
**Field:** first_resonance_ev  

| Item | Value |
|---|---:|
| Gold value | 11.151697 |
| Model value | 60.9 |
| Relative error | 4.46105225061 |
| Relative error percent | 446.105225061 |
| Model / gold ratio | 5.46105225061 |
| log10 ratio | 0.737276331827 |
| Original tolerance | rel=0.02; abs=0.22303394 |
| Original field pass? | false |
| Preliminary pattern | LARGE_NUMERIC_GT100PCT_UNCLASSIFIED |

**Plain-English diagnosis:**  
The field is more than 100% away from gold but did not match a simple gate heuristic.

**Possible gate:**  
UNCLASSIFIED_LARGE_GATE

**Audit question:**  
What is the simplest human-readable explanation for this large numeric miss?

**Recommended manual decision options:**  
CONFIRM_GATE;REJECT_GATE_FALSE_POSITIVE;REASSIGN_TO_DIFFERENT_GATE;NEEDS_SCENARIO_CONTEXT;NEEDS_RAW_ANSWER_REVIEW

**Notes:**  
No raw final-answer block included; normalized extracted value is shown.

### Card 047 - UNCLASSIFIED_LARGE_GATE

**Scenario:** COS_AGE_001  
**Model:** Mistral NeMo 12B  
**Batch:** V5  
**Field:** matter_age_gyr  

| Item | Value |
|---|---:|
| Gold value | 9.312307 |
| Model value | 46.67 |
| Relative error | 4.01164748971 |
| Relative error percent | 401.164748971 |
| Model / gold ratio | 5.01164748971 |
| log10 ratio | 0.699980515902 |
| Original tolerance | rel=0.01; abs=0.09312307 |
| Original field pass? | false |
| Preliminary pattern | LARGE_NUMERIC_GT100PCT_UNCLASSIFIED |

**Plain-English diagnosis:**  
The field is more than 100% away from gold but did not match a simple gate heuristic.

**Possible gate:**  
UNCLASSIFIED_LARGE_GATE

**Audit question:**  
What is the simplest human-readable explanation for this large numeric miss?

**Recommended manual decision options:**  
CONFIRM_GATE;REJECT_GATE_FALSE_POSITIVE;REASSIGN_TO_DIFFERENT_GATE;NEEDS_SCENARIO_CONTEXT;NEEDS_RAW_ANSWER_REVIEW

**Notes:**  
No raw final-answer block included; normalized extracted value is shown.

### Card 048 - UNCLASSIFIED_LARGE_GATE

**Scenario:** COS_DESITTER_001  
**Model:** Gemma 3 12B IT  
**Batch:** V4  
**Field:** gh_temp_e30_K  

| Item | Value |
|---|---:|
| Gold value | 2.757786 |
| Model value | 13.5 |
| Relative error | 3.89523117457 |
| Relative error percent | 389.523117457 |
| Model / gold ratio | 4.89523117457 |
| log10 ratio | 0.689773205939 |
| Original tolerance | rel=0.01; abs=0.02757786 |
| Original field pass? | false |
| Preliminary pattern | LARGE_NUMERIC_GT100PCT_UNCLASSIFIED |

**Plain-English diagnosis:**  
The field is more than 100% away from gold but did not match a simple gate heuristic.

**Possible gate:**  
UNCLASSIFIED_LARGE_GATE

**Audit question:**  
What is the simplest human-readable explanation for this large numeric miss?

**Recommended manual decision options:**  
CONFIRM_GATE;REJECT_GATE_FALSE_POSITIVE;REASSIGN_TO_DIFFERENT_GATE;NEEDS_SCENARIO_CONTEXT;NEEDS_RAW_ANSWER_REVIEW

**Notes:**  
No raw final-answer block included; normalized extracted value is shown.

### Card 049 - UNCLASSIFIED_LARGE_GATE

**Scenario:** QFT_CASIMIR_001  
**Model:** Mistral NeMo 12B  
**Batch:** V3  
**Field:** energy_per_area_uJ_m2  

| Item | Value |
|---|---:|
| Gold value | 0.433375 |
| Model value | 2.00 |
| Relative error | 3.61494087107 |
| Relative error percent | 361.494087107 |
| Model / gold ratio | 4.61494087107 |
| log10 ratio | 0.664166141 |
| Original tolerance | rel=0.01; abs=0.00433375 |
| Original field pass? | false |
| Preliminary pattern | LARGE_NUMERIC_GT100PCT_UNCLASSIFIED |

**Plain-English diagnosis:**  
The field is more than 100% away from gold but did not match a simple gate heuristic.

**Possible gate:**  
UNCLASSIFIED_LARGE_GATE

**Audit question:**  
What is the simplest human-readable explanation for this large numeric miss?

**Recommended manual decision options:**  
CONFIRM_GATE;REJECT_GATE_FALSE_POSITIVE;REASSIGN_TO_DIFFERENT_GATE;NEEDS_SCENARIO_CONTEXT;NEEDS_RAW_ANSWER_REVIEW

**Notes:**  
No raw final-answer block included; normalized extracted value is shown.

### Card 050 - UNCLASSIFIED_LARGE_GATE

**Scenario:** GR_PERI_001  
**Model:** Gemma 3 27B IT  
**Batch:** V4  
**Field:** advance_arcsec_century  

| Item | Value |
|---|---:|
| Gold value | 42.980208 |
| Model value | 181.0 |
| Relative error | 3.21124067152 |
| Relative error percent | 321.124067152 |
| Model / gold ratio | 4.21124067152 |
| log10 ratio | 0.624410061968 |
| Original tolerance | rel=0.01; abs=0.42980208 |
| Original field pass? | false |
| Preliminary pattern | LARGE_NUMERIC_GT100PCT_UNCLASSIFIED |

**Plain-English diagnosis:**  
The field is more than 100% away from gold but did not match a simple gate heuristic.

**Possible gate:**  
UNCLASSIFIED_LARGE_GATE

**Audit question:**  
What is the simplest human-readable explanation for this large numeric miss?

**Recommended manual decision options:**  
CONFIRM_GATE;REJECT_GATE_FALSE_POSITIVE;REASSIGN_TO_DIFFERENT_GATE;NEEDS_SCENARIO_CONTEXT;NEEDS_RAW_ANSWER_REVIEW

**Notes:**  
No raw final-answer block included; normalized extracted value is shown.

### Card 051 - UNCLASSIFIED_LARGE_GATE

**Scenario:** GR_CHIRP_001  
**Model:** Gemma 4 31B IT  
**Batch:** V5  
**Field:** each_mass_msun  

| Item | Value |
|---|---:|
| Gold value | 32.163554 |
| Model value | 131.64 |
| Relative error | 3.09283128351 |
| Relative error percent | 309.283128351 |
| Model / gold ratio | 4.09283128351 |
| log10 ratio | 0.612023842336 |
| Original tolerance | rel=0.01; abs=0.32163554 |
| Original field pass? | false |
| Preliminary pattern | LARGE_NUMERIC_GT100PCT_UNCLASSIFIED |

**Plain-English diagnosis:**  
The field is more than 100% away from gold but did not match a simple gate heuristic.

**Possible gate:**  
UNCLASSIFIED_LARGE_GATE

**Audit question:**  
What is the simplest human-readable explanation for this large numeric miss?

**Recommended manual decision options:**  
CONFIRM_GATE;REJECT_GATE_FALSE_POSITIVE;REASSIGN_TO_DIFFERENT_GATE;NEEDS_SCENARIO_CONTEXT;NEEDS_RAW_ANSWER_REVIEW

**Notes:**  
No raw final-answer block included; normalized extracted value is shown.

### Card 052 - UNCLASSIFIED_LARGE_GATE

**Scenario:** STAT_BEC_001  
**Model:** Mistral Small 3.2 24B Instruct  
**Batch:** V3  
**Field:** tc_no_zeta_nK  

| Item | Value |
|---|---:|
| Gold value | 162.780255 |
| Model value | 636.0 |
| Relative error | 2.90710777545 |
| Relative error percent | 290.710777545 |
| Model / gold ratio | 3.90710777545 |
| log10 ratio | 0.591855391168 |
| Original tolerance | rel=0.01; abs=1.62780255 |
| Original field pass? | false |
| Preliminary pattern | LARGE_NUMERIC_GT100PCT_UNCLASSIFIED |

**Plain-English diagnosis:**  
The field is more than 100% away from gold but did not match a simple gate heuristic.

**Possible gate:**  
UNCLASSIFIED_LARGE_GATE

**Audit question:**  
What is the simplest human-readable explanation for this large numeric miss?

**Recommended manual decision options:**  
CONFIRM_GATE;REJECT_GATE_FALSE_POSITIVE;REASSIGN_TO_DIFFERENT_GATE;NEEDS_SCENARIO_CONTEXT;NEEDS_RAW_ANSWER_REVIEW

**Notes:**  
No raw final-answer block included; normalized extracted value is shown.
