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
