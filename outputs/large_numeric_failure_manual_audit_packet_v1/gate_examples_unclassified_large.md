# UNCLASSIFIED_LARGE_GATE

The answer is more than 100% wrong but did not match a simple ratio heuristic.

## Count Summary

- fields_detected: 24
- rows_detected: 17
- false_positive_risk: medium

## Suggested Manual Decision Checklist

- Does the ratio heuristic match the actual scientific mistake?
- Could this be a field swap or unit/context issue instead?
- Should this gate become a formal diagnostic flag?

## Selected Audit Cards

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
