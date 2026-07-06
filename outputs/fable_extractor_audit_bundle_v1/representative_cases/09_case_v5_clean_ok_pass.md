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
