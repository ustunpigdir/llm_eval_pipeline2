# Representative Cases Digest

Compact cases covering clean extraction, recoverable repetition, blank/no-valid/conflict blocks, operator/unit/symbolic edge cases, and clean extraction with wrong reasoning.



---

# Repeated identical GPS final blocks recoverable

- case_id: `case_run_214`
- scenario_id: `unknown`
- model_name: `NVIDIA Nemotron 3 Nano 30B-A3B`
- source_batch: `original_layer1b`
- helper_status: `KEEP_RECOVERABLE_WITH_WARNINGS`
- deterministic_grade: ``
- why_included: Recoverable repeated filled blocks plus blank templates/tail pollution.
- source_paths: run_214_full_answer.txt, remaining_layer1b_flag_classification_v3.csv

## Raw Final-Answer / Evidence Excerpt

```text
k run slower (negative shift). The two effects oppose each other; the net is still faster but less than the gravitational effect alone.

Now we need to produce final answer in LaTeX block with fields:

\[
\begin{aligned}
\mathrm{grav\_shift\_us\_day} &= \\
\mathrm{velocity\_shift\_us\_day} &= \\
\mathrm{net\_shift\_us\_day} &=
\end{aligned}
\]

We need to fill these with numeric values (presumably with appropriate sign). The problem says "report each effect as microseconds per day of satellite-clock rate relative to a ground clock; 'gravitational' = potential difference term; 'velocity' = special-relativistic dilation with orbital speed v^2 = GM_E/r." So we need to output the values.

We need to decide on rounding. The problem didn't specify rounding; we can give values to maybe two decimal places? But we need to be consistent. Usually GPS relativistic correction is about +45.7 microseconds per day gravitational, -7.2 microseconds per day velocity, net +38.5 microseconds per day. Many references say +38 microseconds per day net. So we can give values: gravitational shift = +45.7 us/day, velocity shift = -7.2 us/day, net shift = +38.5 us/day. Or maybe we can give more precise values: gravitational shift = +45.70 us/day, velocity shift = -7.18 us/day, net shift = +38.52 us/day. Let's compute more precisely using more accurate numbers.

Let's compute more precisely using high prec
[snippet truncated]
```

## Extracted Fields

```json
[
  {
    "field": "grav_shift_us_day",
    "raw_value": ""
  },
  {
    "field": "velocity_shift_us_day",
    "raw_value": ""
  }
]
```

## Expected / Gold Fields

```json
[]
```



---

# Long invalid/meta output unusable

- case_id: `case_run_380`
- scenario_id: `unknown`
- model_name: `Ministral 3 8B`
- source_batch: `original_layer1b`
- helper_status: `UNUSABLE`
- deterministic_grade: ``
- why_included: Counterexample where many headings/meta output should remain UNUSABLE.
- source_paths: run_380_full_answer.txt, remaining_layer1b_flag_classification_v3.csv

## Raw Final-Answer / Evidence Excerpt

```text
derivation** is as follows:

The **optimal fidelity** for the Buzek-Hillery machine is:
\[
F = \frac{4}{3} \cdot \frac{1}{3} \quad \text{(no)}.
\]

---

### **Final Answer:**

The **optimal universal cloning fidelity** for the Buzek-Hillery machine is:
\[
F = \frac{4}{3} \cdot \frac{1}{3} \quad \text{(no)}.
\]

The **correct optimal fidelity** for the Buzek-Hillery machine is:
\[
F = \frac{4}{3} \cdot \frac{1}{3} \quad \text{(no)}.
\]

The **correct derivation** is as follows:

The **optimal fidelity** for the Buzek-Hillery machine is:
\[
F = \frac{4}{3} \cdot \frac{1}{3} \quad \text{(no)}.
\]

---

### **Correct Derivation (from Buzek-Hillery paper):**

The **optimal fidelity** for the Buzek-Hillery machine is:
\[
F = \frac{4}{3} \cdot \frac{1}{3} \quad \text{(no)}.
\]

Instead, the **correct optimal fidelity** for the Buzek-Hillery machine is:
\[
F = \frac{4}{3} \cdot \frac{1}{3} \quad \text{(no)}.
\]

The **correct derivation** is as follows:

The **optimal fidelity** for the Buzek-Hillery machine is:
\[
F = \frac{4}{3} \cdot \frac{1}{3} \quad \text{(no)}.
\]

---

### **Final Correct Derivation:**

The **optimal fidelity** for the Buzek-Hillery machine is:
\[
F = \frac{4}{3} \cdot \frac{1}{3} \quad \text{(no)}.
\]

The **correct optimal fidelity** for the Buzek-Hillery machine is:
\[
F = \frac{4}{3} \cdot \frac{1}{3} \quad \text{(no)}.
\]

The **correct derivation** is as 
[snippet truncated]
```

## Extracted Fields

```json
[]
```

## Expected / Gold Fields

```json
[]
```



---

# Looping unusable without complete final block

- case_id: `case_run_514`
- scenario_id: `unknown`
- model_name: `Gemma 3 12B IT`
- source_batch: `original_layer1b`
- helper_status: `UNUSABLE`
- deterministic_grade: ``
- why_included: No complete filled final-answer block; repetition prevents recovery.
- source_paths: run_514_full_answer.txt, remaining_layer1b_flag_classification_v3.csv

## Raw Final-Answer / Evidence Excerpt

```text
Let's break down the problem step by step.

1. **Evaluate $\kappa$ in nm$^{-1}$ and the dimensionless product $\kappa L$.**

First, we need to convert the energy values to SI units (Joules).
$E = 1.00 \text{ eV} = 1.00 \times 1.602 \times 10^{-19} \text{ J}$
$V_0 = 5.00 \text{ eV} = 5.00 \times 1.602 \times 10^{-19} \text{ J}$
$L = 1.00 \text{ nm} = 1.00 \times 10^{-9} \text{ m}$
$\hbar = 1.054 \times 10^{-34} \text{ J s}$
$m_e = 9.109 \times 10^{-31} \text{ kg}$ (electron mass)

Now, we can calculate $\kappa$:
$\kappa = \sqrt{\frac{2m_e(V_0 - E)}{\hbar^2}} = \sqrt{\frac{2 \times 9.109 \times 10^{-31} \text{ kg} \times (5.00 \times 1.602 \times 10^{-19} \text{ J} - 1.00 \times 1.602 \times 10^{-19} \text{ J})}{\left(1.054 \times 10^{-34} \text{ J s}\right)^2}}$
$\kappa = \sqrt{\frac{2 \times 9.109 \times 10^{-31} \times 3.999 \times 10^{-19}}{1.1105 \times 10^{-68}}} = \sqrt{\frac{7.305 \times 10^{-50}}{1.1105 \times 10^{-68}}} = \sqrt{6.574 \times 10^{18}} = 2.564 \times 10^9 \text{ m}^{-1}$

To convert to nm$^{-1}$:
$\kappa = 2.564 \times 10^9 \text{ m}^{-1} \times \frac{1 \text{ nm}}{10^{-9} \text{ m}} = 2.564 \times 10^{18} \text{ nm}^{-1}$

Now, we calculate $\kappa L$:
$\kappa L = (2.564 \times 10^{18} \text{ nm}^{-1}) \times (1.00 \times 10^{-9} \text{ nm}) = 2.564 \times 10^9$

2. **Evaluate the prefactor $16E(V_0-E)/V_0^2$.**

$16 E (V_0 - E) / V_0^2 = 16 \times (1.00
```

## Extracted Fields

```json
[]
```

## Expected / Gold Fields

```json
[]
```



---

# Repeated identical blocks plus later blank templates recoverable

- case_id: `case_run_235`
- scenario_id: `unknown`
- model_name: `NVIDIA Nemotron 3 Nano 30B-A3B`
- source_batch: `original_layer1b`
- helper_status: `KEEP_RECOVERABLE_WITH_WARNINGS`
- deterministic_grade: ``
- why_included: Local full answer not present; classification table preserves compact audited evidence.
- source_paths: remaining_layer1b_flag_classification_v3.csv

## Raw Final-Answer / Evidence Excerpt

```text
classification=KEEP_RECOVERABLE_WITH_WARNINGS
reason=filled final-answer block is recoverable (values: 88.6, 219.9, 439.8) but answer has structural pollution: 9 repeated identical filled final-answer blocks; blank template final-answer block(s) appear after the chosen final block; meta-discussion about the answer format continues after the final-answer block
filled_final_block_count=9 blank_template_block_count=4 distinct_filled_final_block_count=1
```

## Extracted Fields

```json
[]
```

## Expected / Gold Fields

```json
[]
```



---

# Granite operator variant &\approx accepted

- case_id: `case_run_496`
- scenario_id: `unknown`
- model_name: `Granite 4.1 8B`
- source_batch: `original_layer1b`
- helper_status: `KEEP_CLEAN`
- deterministic_grade: ``
- why_included: Local full answer not present; classification table preserves compact audited evidence.
- source_paths: remaining_layer1b_flag_classification_v3.csv

## Raw Final-Answer / Evidence Excerpt

```text
classification=KEEP_CLEAN
reason=single clean filled final-answer block near the end, no repetition or pollution detected
filled_final_block_count=1 blank_template_block_count=0 distinct_filled_final_block_count=1
```

## Extracted Fields

```json
[]
```

## Expected / Gold Fields

```json
[]
```



---

# Granite operator variant &\approx accepted

- case_id: `case_run_497`
- scenario_id: `unknown`
- model_name: `Granite 4.1 8B`
- source_batch: `original_layer1b`
- helper_status: `KEEP_CLEAN`
- deterministic_grade: ``
- why_included: Local full answer not present; classification table preserves compact audited evidence.
- source_paths: remaining_layer1b_flag_classification_v3.csv

## Raw Final-Answer / Evidence Excerpt

```text
classification=KEEP_CLEAN
reason=single clean filled final-answer block near the end, no repetition or pollution detected
filled_final_block_count=1 blank_template_block_count=0 distinct_filled_final_block_count=1
```

## Extracted Fields

```json
[]
```

## Expected / Gold Fields

```json
[]
```



---

# Granite operator variant &\approx accepted

- case_id: `case_run_498`
- scenario_id: `unknown`
- model_name: `Granite 4.1 8B`
- source_batch: `original_layer1b`
- helper_status: `KEEP_CLEAN`
- deterministic_grade: ``
- why_included: Local full answer not present; classification table preserves compact audited evidence.
- source_paths: remaining_layer1b_flag_classification_v3.csv

## Raw Final-Answer / Evidence Excerpt

```text
classification=KEEP_CLEAN
reason=single clean filled final-answer block near the end, no repetition or pollution detected
filled_final_block_count=1 blank_template_block_count=0 distinct_filled_final_block_count=1
```

## Extracted Fields

```json
[]
```

## Expected / Gold Fields

```json
[]
```



---

# LaTeX text units and display-span pollution recoverable

- case_id: `case_run_290`
- scenario_id: `unknown`
- model_name: `Mistral NeMo 12B`
- source_batch: `original_layer1b`
- helper_status: `KEEP_RECOVERABLE_WITH_WARNINGS`
- deterministic_grade: ``
- why_included: Local full answer not present; classification table preserves compact audited evidence.
- source_paths: remaining_layer1b_flag_classification_v3.csv

## Raw Final-Answer / Evidence Excerpt

```text
classification=KEEP_RECOVERABLE_WITH_WARNINGS
reason=filled final-answer block is recoverable (values: 1.3 \times 10^{-3} \text{ Pa}, 3.9 \times 10^{-5} \text{ μJ/m}^2, 1.56 \times 10^{-4} \text{ Pa}) but answer has structural pollution: the stored display_math span for this block also swallowed surrounding prose
filled_final_block_count=1 blank_template_block_count=0 distinct_filled_final_block_count=1
```

## Extracted Fields

```json
[]
```

## Expected / Gold Fields

```json
[]
```



---

# Clean V5 OK extraction and deterministic PASS

- case_id: `case_v5_clean_ok_pass`
- scenario_id: `QI_CLONE_001`
- model_name: `Gemma 3 12B IT`
- source_batch: `structured_prompt_pilot_v5`
- helper_status: `OK`
- deterministic_grade: `PASS`
- why_included: Shows current structured prompt extraction stability when model answer is correct.
- source_paths: outputs/structured_prompt_pilot_v5/structured_prompt_pilot_v5_runs.json

## Raw Final-Answer / Evidence Excerpt

```text
.**.
4. **Quantum advantage.** 5/6 − 2/3 = **1/6 = 0.1666...**. Beating measure-and-prepare is allowed precisely because 5/6 < 1 — no-cloning is not violated.

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{classical\_fidelity} &= 0.6666... \\
\mathrm{optimal\_fidelity}   &= 0.8333... \\
\mathrm{quantum\_advantage}  &= 0.1666... \\
\end{aligned}
\]
```

## Extracted Fields

```json
[
  {
    "field": "classical_fidelity",
    "raw_value": "0.6666..."
  },
  {
    "field": "optimal_fidelity",
    "raw_value": "0.8333..."
  },
  {
    "field": "quantum_advantage",
    "raw_value": "0.1666..."
  }
]
```

## Expected / Gold Fields

```json
[
  {
    "field_index": 0,
    "field_name": "classical_fidelity",
    "expected_value_raw": "0.666667"
  },
  {
    "field_index": 1,
    "field_name": "optimal_fidelity",
    "expected_value_raw": "0.833333"
  },
  {
    "field_index": 2,
    "field_name": "quantum_advantage",
    "expected_value_raw": "0.166667"
  }
]
```



---

# Clean extraction but genuine reasoning/calculation failure

- case_id: `case_v5_clean_extraction_reasoning_fail`
- scenario_id: `GR_CHIRP_001`
- model_name: `Gemma 3 12B IT`
- source_batch: `structured_prompt_pilot_v5`
- helper_status: `OK`
- deterministic_grade: `FAIL`
- why_included: Demonstrates CLEAN extraction does not imply correctness; autograder catches numeric mismatch.
- source_paths: outputs/structured_prompt_pilot_v5/autograde_no_bert_v1/structured_prompt_v5_clean_autograde.json

## Raw Final-Answer / Evidence Excerpt

```text
the combination 𝓜; the individual masses / mass ratio enter only at higher post-Newtonian order. So a leading-order chirp measures **𝓜**, not the total mass.

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{chirp\_mass\_msun} &= 53.8 \\
\mathrm{each\_mass\_msun}  &= 61.7 \\
\mathrm{total\_mass\_msun} &= 123.4 \\
\end{aligned}
\]
```

## Extracted Fields

```json
[
  {
    "field": "chirp_mass_msun",
    "raw_value": "53.8"
  },
  {
    "field": "each_mass_msun",
    "raw_value": "61.7"
  },
  {
    "field": "total_mass_msun",
    "raw_value": "123.4"
  }
]
```

## Expected / Gold Fields

```json
[
  {
    "field_index": 0,
    "field_name": "chirp_mass_msun",
    "expected_value_raw": "28.0"
  },
  {
    "field_index": 1,
    "field_name": "each_mass_msun",
    "expected_value_raw": "32.163554"
  },
  {
    "field_index": 2,
    "field_name": "total_mass_msun",
    "expected_value_raw": "64.327108"
  }
]
```



---

# Structured V2 non-clean helper status ALL_BLANK

- case_id: `case_v2_all_blank`
- scenario_id: `CM_FOUCAULT_001`
- model_name: `NVIDIA Nemotron 3 Nano 30B-A3B`
- source_batch: `structured_prompt_pilot_v2`
- helper_status: `ALL_BLANK`
- deterministic_grade: ``
- why_included: Compact example of helper_status=ALL_BLANK driving REVIEW.
- source_paths: outputs/structured_prompt_pilot_v2/review_layer_v1/review_layer_v1.json, outputs/structured_prompt_pilot_v2/non_clean_raw_outputs.md

## Raw Final-Answer / Evidence Excerpt

```text
in(48.85°) = ____. Rate = 15·____ = **____°/h**; ×24 = **____°/day**.
3. **Period.** Full turn = 360°/(____°/h) = **____ h**.
4. **Limits.** ... (explanation)

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{period\_hours}        &=  \\
\mathrm{rate\_deg\_per\_day}  &=  \\
\mathrm{rate\_deg\_per\_hour} &=  \\
\end{aligned}
\] 

We need to fill in the missing values by doing the calculation. The placeholders are:

- sin(48.85°) = ____. So we need to compute sin(48.85°). Let's compute approximate value.

sin(48.85°). Use degrees. sin(48.85) approximate. Let's compute precisely.

We can compute using known values or approximate. 48.85 degrees is close to 49 degrees. sin(49°) ≈ 0.7547. Let's compute more precisely: sin(48.85°). Use radian conversion: 48.85° * π/180 = 0.8529 rad? Actually 48.85 * π/180 = 0.8529 rad? Let's compute: π ≈ 3.1415926535. 48.85/180 = 0.2713889. Multiply by π: 0.2713889 * 3.14159265 = 0.852... Let's compute precisely: 3.14159265 * 0.2713889 = 0.852... Actually 3.14159265 * 0.27 = 0.8482, plus extra 0.0013889*3.14159265 ≈ 0.00436, sum ≈ 0.8526. So rad ≈ 0.8526 rad. sin(0.8526) ≈ 0.752? Let's compute sin using series or approximate. sin(0.8526) =? Use known sin(0.85) ≈ 0.7513. Actually sin(0.85 rad) ≈ 0.7513. Slightly larger rad (0.8526) yields sin ~0.7525. So sin(48.85°) ≈ 0.752. Let's compute more precisely using a calculator mental: sin(48.85°). Use known sin
[snippet truncated]
```

## Extracted Fields

```json
[
  {
    "field": "period_hours",
    "raw_value": ""
  },
  {
    "field": "rate_deg_per_day",
    "raw_value": ""
  },
  {
    "field": "rate_deg_per_hour",
    "raw_value": ""
  }
]
```

## Expected / Gold Fields

```json
[
  {
    "field_index": 0,
    "field_name": "period_hours",
    "expected_value_raw": "31.872957"
  },
  {
    "field_index": 1,
    "field_name": "rate_deg_per_day",
    "expected_value_raw": "271.076197"
  },
  {
    "field_index": 2,
    "field_name": "rate_deg_per_hour",
    "expected_value_raw": "11.294842"
  }
]
```



---

# Structured V2 non-clean helper status NO_VALID_BLOCK

- case_id: `case_v2_no_valid_block`
- scenario_id: `SR_ROCKET_001`
- model_name: `NVIDIA Nemotron 3 Nano 30B-A3B`
- source_batch: `structured_prompt_pilot_v2`
- helper_status: `NO_VALID_BLOCK`
- deterministic_grade: ``
- why_included: Compact example of helper_status=NO_VALID_BLOCK driving REVIEW.
- source_paths: outputs/structured_prompt_pilot_v2/review_layer_v1/review_layer_v1.json, outputs/structured_prompt_pilot_v2/non_clean_raw_outputs.md

## Raw Final-Answer / Evidence Excerpt

```text
We need to fill in the missing values in the derivation steps and final answer. The problem statement: "Solve the following scenario. A rocket maintains constant proper acceleration a = 9.8 m/s^2 (as measured by an on-board accelerometer), starting from rest. Use 1 yr = 3.15576×10^7 s and 1 ly = c × 1 yr."

Conventions: hyperbolic (Rindler) motion; τ is proper time on the rocket.

Tasks:

1. Write exact expressions for lab time t(τ), lab distance x(τ), and velocity β(τ) for constant proper acceleration.

2. After τ = 1.00 proper year, evaluate the elapsed lab time in years.

3. Evaluate the distance covered in light-years.

4. Evaluate the final speed β = v/c.

5. A student uses v = aτ and gets β > 1. Explain the error and why the correct β stays below 1.

Use answer structure. Keep same sections and step order. Fill in missing values by doing calculation. Do not copy placeholders. Do not add extra final-answer fields. Do not include more than one FINAL ANSWER block. Keep final answer field names exactly as shown.

**Derivation** (provided). It includes placeholders: aτ/c = ____, Lab time = (c/a) sinh(___
```

## Extracted Fields

```json
[]
```

## Expected / Gold Fields

```json
[
  {
    "field_index": 0,
    "field_name": "distance_ly",
    "expected_value_raw": "0.563194"
  },
  {
    "field_index": 1,
    "field_name": "final_beta",
    "expected_value_raw": "0.774547"
  },
  {
    "field_index": 2,
    "field_name": "lab_time_yr",
    "expected_value_raw": "1.187045"
  }
]
```



---

# Structured V2 non-clean helper status CONFLICT

- case_id: `case_v2_conflict`
- scenario_id: `COS_CMB_001`
- model_name: `NVIDIA Nemotron 3 Nano 30B-A3B`
- source_batch: `structured_prompt_pilot_v2`
- helper_status: `CONFLICT`
- deterministic_grade: ``
- why_included: Compact example of helper_status=CONFLICT driving REVIEW.
- source_paths: outputs/structured_prompt_pilot_v2/review_layer_v1/review_layer_v1.json, outputs/structured_prompt_pilot_v2/non_clean_raw_outputs.md

## Raw Final-Answer / Evidence Excerpt

```text
We need to fill in the missing values in the derivation and final answer. The problem asks to solve the scenario with given conventions. We need to compute:

1. Temperature at recombination: T_rec = T0 * (1+z) = 2.725 K * (1+1100) = 2.725 * 1101 K. Compute that.

2. Number density scaling: n ∝ (1+z)^3. So ratio n_rec / n0 = (1+z)^3 = 1101^3. Then log10 of that ratio = 3 * log10(1101). Compute log10(1101). Let's compute precisely.

3. Energy density scaling: u ∝ (1+z)^4. So log10(u_rec / u0) = 4 * log10(1101). Compute that.

4. Explanation: extra factor of (1+z) relative to number density is per-photon energy redshift.

5. Blackbody preserved: explanation.

We need to fill in the missing values in the derivation and final answer. The final answer block includes three fields: T_rec_K, log10_energy_ratio, log10_number_ratio. They want the final answer row order exactly as sho
```

## Extracted Fields

```json
[
  {
    "field": "T_rec_K",
    "raw_value": ""
  },
  {
    "field": "log10_energy_ratio",
    "raw_value": ""
  },
  {
    "field": "log10_number_ratio",
    "raw_value": ""
  }
]
```

## Expected / Gold Fields

```json
[
  {
    "field_index": 0,
    "field_name": "T_rec_K",
    "expected_value_raw": "3000.225"
  },
  {
    "field_index": 1,
    "field_name": "log10_energy_ratio",
    "expected_value_raw": "12.167149"
  },
  {
    "field_index": 2,
    "field_name": "log10_number_ratio",
    "expected_value_raw": "9.125362"
  }
]
```



---

# Degree notation/unit-wrapper accepted in official grade sample

- case_id: `case_degree_notation_units`
- scenario_id: `CM_APSIDAL_001`
- model_name: `Gemma 4 31B IT`
- source_batch: `official_baseline`
- helper_status: `OK`
- deterministic_grade: `MATCH`
- why_included: Covers degree notation / unit-wrapper normalization risk.
- source_paths: official_grade.csv

## Raw Final-Answer / Evidence Excerpt

```text
official_grade.csv rows show values like 90^\circ, 127.28^\circ matched numerically.
```

## Extracted Fields

```json
[
  {
    "field": "apsidal_harmonic_deg",
    "raw_value": "90^\\circ"
  },
  {
    "field": "apsidal_n_minus1_deg",
    "raw_value": "127.28^\\circ"
  }
]
```

## Expected / Gold Fields

```json
[
  {
    "field_index": 0,
    "field_name": "apsidal_harmonic_deg",
    "expected_value_raw": "90.0"
  },
  {
    "field_index": 1,
    "field_name": "apsidal_kepler_deg",
    "expected_value_raw": "180.0"
  },
  {
    "field_index": 2,
    "field_name": "apsidal_n_minus1_deg",
    "expected_value_raw": "127.279221"
  },
  {
    "field_index": 3,
    "field_name": "precession_per_period_deg",
    "expected_value_raw": "-105.441559"
  }
]
```



---

# STAT_ISING sqrt2 shorthand / symbolic expression boundary

- case_id: `case_sqrt2_unsupported_or_symbolic`
- scenario_id: `STAT_ISING_001`
- model_name: `Gemma/Llama examples`
- source_batch: `official_baseline`
- helper_status: `OK`
- deterministic_grade: `MATCH or UNSUPPORTED depending layer`
- why_included: Covers unsupported-expression versus parser-bug boundary and symbolic equivalence risk.
- source_paths: final_answer_values_review.csv, grade_results_sample.csv

## Raw Final-Answer / Evidence Excerpt

```text
final_answer_values_review.csv classified expressions like 2/\ln(1+\sqrt2) as UNSUPPORTED; later grade_results_sample shows symbolic handling can match when safely evaluated.
```

## Extracted Fields

```json
[
  {
    "field": "tc_exact",
    "raw_value": "2/\\ln(1+\\sqrt2)"
  },
  {
    "field": "ratio_exact_mf",
    "raw_value": "\\frac{1}{2\\ln(1+\\sqrt2)}"
  }
]
```

## Expected / Gold Fields

```json
[
  {
    "field_index": 0,
    "field_name": "ratio_exact_mf",
    "expected_value_raw": "0.567296"
  },
  {
    "field_index": 1,
    "field_name": "tc_exact",
    "expected_value_raw": "2.269185"
  },
  {
    "field_index": 2,
    "field_name": "tc_meanfield",
    "expected_value_raw": "4.0"
  }
]
```
