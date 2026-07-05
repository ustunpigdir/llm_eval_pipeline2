#!/usr/bin/env python3
"""Export the eight-scenario structured-prompt pilot pack."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sqlite3
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DB = ROOT / "learning.db"
PILOT_VERSION = "v2"
OUTPUT_DIR = ROOT / "outputs" / f"structured_prompt_pilot_{PILOT_VERSION}"
PILOT_NAME = f"structured_prompt_pilot_{PILOT_VERSION}"

SCENARIO_ORDER = [
    "CM_FOUCAULT_001",
    "COS_CMB_001",
    "GR_ISCO_001",
    "QI_TELEPORT_001",
    "QM_BERRY_001",
    "QFT_G2_001",
    "SR_ROCKET_001",
    "STAT_ISING_001",
]

STRUCTURED_PROMPTS = {
    "CM_FOUCAULT_001": """Solve the scenario. Use the following answer structure. Keep the same sections, step order, field names, and final-answer block format. Fill in the missing values by doing the calculation.
Do not copy the placeholders.
Do not add extra final-answer fields.
Do not include more than one FINAL ANSWER block.
**Derivation**
1. **The sin λ factor.** The Coriolis coupling that rotates the swing plane is the **vertical** component of Earth's angular velocity, Ω_E sin λ. (The horizontal component Ω_E cos λ tilts the local vertical; it does not precess the plane.)
2. **Rate.** Ω_E = 360°/24 h = 15°/h. sin(48.85°) = ____. Rate = 15·____ = **____°/h**; ×24 = **____°/day**.
3. **Period.** Full turn = 360°/(____°/h) = **____ h**.
4. **Limits.** Equator (λ = 0): sin λ = 0 → no precession. Pole (λ = 90°): 15°/h → 24 h period. A student using cos λ takes the horizontal component — wrong; it tilts, it does not precess the plane.
**FINAL ANSWER**

[
\\begin{aligned}
\\mathrm{rate_deg_per_day}  &=  \\
\\mathrm{rate_deg_per_hour} &=  \\
\\mathrm{period_hours}       &=
\\end{aligned}
]""",
    "COS_CMB_001": """Solve the scenario. Use the following answer structure. Keep the same sections, step order, field names, and final-answer block format. Fill in the missing values by doing the calculation.
Do not copy the placeholders.
Do not add extra final-answer fields.
Do not include more than one FINAL ANSWER block.
**Derivation**
1. **Temperature.** T ∝ (1+z): T_rec = 2.725·1101 = **____ K**.
2. **Number density.** n ∝ (1+z)³: log₁₀(n_rec/n₀) = 3·log₁₀(1101) = **____**.
3. **Energy density.** u ∝ (1+z)⁴: log₁₀(u_rec/u₀) = 4·log₁₀(1101) = **____**. The extra factor of (1+z) over the number density is the **per-photon energy redshift** — each photon's energy scales as (1+z).
4. **Blackbody preserved.** T ∝ 1/a keeps the Planck spectrum form-invariant: redshifting a Planck spectrum at T yields a Planck spectrum at T/(1+z). No scattering or rethermalization is required.
**FINAL ANSWER**

[
\\begin{aligned}
\\mathrm{T_rec_K}            &=  \\
\\mathrm{log10_number_ratio} &=  \\
\\mathrm{log10_energy_ratio} &=
\\end{aligned}
]""",
    "GR_ISCO_001": """Solve the scenario. Use the following answer structure. Keep the same sections, step order, field names, and final-answer block format. Fill in the missing values by doing the calculation.
Do not copy the placeholders.
Do not add extra final-answer fields.
Do not include more than one FINAL ANSWER block.
**Derivation**
1. **Characteristic radii** (units of GM/c²): event horizon 2GM/c², photon sphere 3GM/c², **ISCO 6GM/c²** — three distinct radii. With GM/c² = G·10M_⊙/c² ≈ ____ km: horizon ____ km, photon sphere ____ km, **r_ISCO = 6·____ ≈ ____ km**.
2. **Orbital frequency.** f = Ω/2π = (1/2π)√(GM/r_ISCO³), GM = ____ m³/s², r_ISCO = ____ m ⟹ **f_orb = ____ Hz**.
3. **GW frequency.** Dominant emission at twice the orbital frequency: **f_GW = 2·____ = ____ Hz**.
4. **Interpretation.** No stable circular orbit exists inside r_ISCO, so the inspiral transitions to plunge/merger there — the quasi-periodic chirp "shuts off." Since r_ISCO ∝ M and f ∝ M⁻¹, heavier binaries merge at **lower** frequency (f_ISCO ∝ 1/M).
**FINAL ANSWER**

[
\\begin{aligned}
\\mathrm{r_isco_km}    &=  \\
\\mathrm{f_orbital_hz} &=  \\
\\mathrm{f_gw_hz}      &=
\\end{aligned}
]""",
    "QI_TELEPORT_001": """Solve the scenario. Use the following answer structure. Keep the same sections, step order, field names, and final-answer block format. Fill in the missing values by doing the calculation.
Do not copy the placeholders.
Do not add extra final-answer fields.
Do not include more than one FINAL ANSWER block.
**Derivation**
1. **Output fidelity.** F = (2·0.900 + 1)/3 = ____/3 = **____**.
2. **Classical limit.** Best measure-and-send strategy with no shared entanglement: **F_cl = 2/3 = ____** (Massar–Popescu).
3. **Threshold to beat it.** (2f+1)/3 > 2/3 ⟹ 2f+1 > 2 ⟹ **f > 1/2 = ____**.
4. **Interpretation.** f > 1/2 is exactly the entanglement threshold of the isotropic resource; since no classical strategy exceeds 2/3, any F > 2/3 certifies a genuinely quantum (entanglement-assisted) channel. Note the bookkeeping: the resource quality f = 0.900 is **not** the teleportation fidelity F = ____.
**FINAL ANSWER**

[
\\begin{aligned}
\\mathrm{teleport_fidelity} &=  \\
\\mathrm{classical_limit}   &=  \\
\\mathrm{f_threshold}       &=
\\end{aligned}
]""",
    "QM_BERRY_001": """Solve the scenario. Use the following answer structure. Keep the same sections, step order, field names, and final-answer block format. Fill in the missing values by doing the calculation.
Do not copy the placeholders.
Do not add extra final-answer fields.
Do not include more than one FINAL ANSWER block.
**Derivation**
1. **Solid angle.** Ω = 2π(1 − cos θ) = 2π(1 − cos 60°) = 2π(1 − 0.5) = **π = ____ sr**.
2. **Berry phase (spin-½).** γ = −½ Ω, so |γ| = Ω/2 = π/2 = **____ rad**. The factor ½ is the spin.
3. **Spin-1 (m = 1).** In general |γ| = m·Ω for the aligned |S,m⟩ state, so spin-1 m = 1 gives |γ| = π (scales with m).
4. **Why geometric.** γ depends only on the solid angle Ω enclosed by the field's path — **not** on the traversal speed (as long as adiabatic), the field magnitude, or elapsed time. It is distinct from the dynamical phase (∝ energy × time).
**FINAL ANSWER**

[
\\begin{aligned}
\\mathrm{solid_angle_sr}  &=  \\
\\mathrm{berry_phase_rad} &=
\\end{aligned}
]""",
    "QFT_G2_001": """Solve the scenario. Use the following answer structure. Keep the same sections, step order, field names, and final-answer block format. Fill in the missing values by doing the calculation.
Do not copy the placeholders.
Do not add extra final-answer fields.
Do not include more than one FINAL ANSWER block.
**Derivation**
1. **Schwinger one-loop.** a_e = α/(2π).
2. **Anomaly.** a_e = (1/137.036)/(2π) = ____/____ = ____×10⁻³ ⟹ **a_e×10³ = ____**.
3. **g-factor.** g = 2(1 + a_e) = 2·____ = **____**.
4. **Meaning.** The anomaly is the deviation from the tree-level Dirac value g = 2, produced by the electron emitting and reabsorbing a virtual photon (one loop). The leading coefficient α/(2π) is **mass-independent**, so the muon receives the same α/(2π) at leading order; mass-dependent contributions enter only at higher order.
**FINAL ANSWER**

[
\\begin{aligned}
\\mathrm{anomaly_times_1e3} &=  \\
\\mathrm{g_factor}           &=
\\end{aligned}
]""",
    "SR_ROCKET_001": """Solve the scenario. Use the following answer structure. Keep the same sections, step order, field names, and final-answer block format. Fill in the missing values by doing the calculation.
Do not copy the placeholders.
Do not add extra final-answer fields.
Do not include more than one FINAL ANSWER block.
**Derivation**
1. **Exact hyperbolic motion.** t(τ) = (c/a) sinh(aτ/c), x(τ) = (c²/a)(cosh(aτ/c) − 1), β(τ) = tanh(aτ/c). The dimensionless combination aτ/c is the **rapidity**.
2. **Rapidity & lab time.** aτ/c = 9.8·3.15576×10⁷ / 2.99792458×10⁸ = ____. Lab time = (c/a) sinh(____) ⟹ **____ yr** (> 1 proper year — the correct dilation direction).
3. **Distance.** x = (c²/a)(cosh ____ − 1) ⟹ **____ ly**.
4. **Final speed.** β = tanh(____) = **____**.
5. **The student's error.** v = aτ gives β = aτ/c = ____ > 1 (superluminal). The resolution: the **rapidity** aτ/c grows linearly, but velocity β = tanh(rapidity) saturates below 1. Newtonian kinematics wrongly adds velocities instead of rapidities.
**FINAL ANSWER**

[
\\begin{aligned}
\\mathrm{lab_time_yr}  &=  \\
\\mathrm{distance_ly}   &=  \\
\\mathrm{final_beta}    &=
\\end{aligned}
]""",
    "STAT_ISING_001": """Solve the scenario. Use the following answer structure. Keep the same sections, step order, field names, and final-answer block format. Fill in the missing values by doing the calculation.
Do not copy the placeholders.
Do not add extra final-answer fields.
Do not include more than one FINAL ANSWER block.
**Derivation**
1. **Mean field.** k_B T_c^{MF}/J = z = **____**.
2. **Onsager exact.** k_B T_c/J = 2/ln(1+√2) = 2/____ = **____**.
3. **Ratio.** T_c^{exact}/T_c^{MF} = ____/____ = **____**. Mean field **overestimates** T_c because it replaces each spin's neighbors by their average and ignores fluctuations; thermal fluctuations destroy long-range order at a lower temperature than the mean-field estimate.
4. **One dimension.** T_c = 0 — no finite-temperature transition. A single domain wall costs energy 2J but gains entropy k ln N; for any T > 0 the free-energy term −TΔS wins for large N, so order is always destroyed (Peierls / domain-wall argument).
**FINAL ANSWER**

[
\\begin{aligned}
\\mathrm{tc_exact}      &=  \\
\\mathrm{tc_meanfield}  &=  \\
\\mathrm{ratio_exact_mf} &=
\\end{aligned}
]""",
}

FINAL_ANSWER_RE = re.compile(r"\*\*FINAL ANSWER\*\*", re.S)
BENCHMARK_INSTRUCTION_MARKER = "\nYou are solving a scientific reasoning benchmark."


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def connect(db_path: Path) -> sqlite3.Connection:
    con = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    con.row_factory = sqlite3.Row
    return con


def load_scenarios(con: sqlite3.Connection) -> dict[str, sqlite3.Row]:
    placeholders = ",".join("?" for _ in SCENARIO_ORDER)
    rows = con.execute(
        f"""
        SELECT scenario_id, title, category, prompt
        FROM scenarios
        WHERE scenario_id IN ({placeholders})
        """,
        SCENARIO_ORDER,
    ).fetchall()
    by_id = {row["scenario_id"]: row for row in rows}
    missing = [scenario_id for scenario_id in SCENARIO_ORDER if scenario_id not in by_id]
    if missing:
        raise SystemExit("Missing scenario(s) in DB: " + ", ".join(missing))
    return by_id


def load_gold_fields(con: sqlite3.Connection) -> dict[str, list[sqlite3.Row]]:
    placeholders = ",".join("?" for _ in SCENARIO_ORDER)
    rows = con.execute(
        f"""
        SELECT scenario_id, field_index, field_name, expected_value_raw
        FROM gold_fields
        WHERE scenario_id IN ({placeholders})
        ORDER BY scenario_id, field_index
        """,
        SCENARIO_ORDER,
    ).fetchall()
    by_scenario: dict[str, list[sqlite3.Row]] = {scenario_id: [] for scenario_id in SCENARIO_ORDER}
    for row in rows:
        by_scenario[row["scenario_id"]].append(row)
    missing = [scenario_id for scenario_id, fields in by_scenario.items() if not fields]
    if missing:
        raise SystemExit("Missing gold field(s) in DB: " + ", ".join(missing))
    return by_scenario


def load_model_names(con: sqlite3.Connection) -> list[str]:
    rows = con.execute(
        """
        SELECT DISTINCT model_name
        FROM official_gradeable_runs
        WHERE model_name IS NOT NULL AND TRIM(model_name) != ''
        ORDER BY model_name
        """
    ).fetchall()
    if not rows:
        raise SystemExit("No model identities found in official_gradeable_runs")
    return [row["model_name"] for row in rows]


def latex_field_name(field_name: str) -> str:
    return field_name.replace("_", r"\_")


def scaffold_derivation(scaffold: str) -> str:
    derivation_start = scaffold.index("**Derivation**")
    final_match = FINAL_ANSWER_RE.search(scaffold)
    if final_match is None:
        raise SystemExit("Structured scaffold is missing FINAL ANSWER marker")
    return scaffold[derivation_start:final_match.start()].strip()


def original_question_text(db_prompt: str) -> str:
    """Keep DB-sourced scenario text without the original runner answer template."""
    prompt = db_prompt.strip()
    marker_index = prompt.find(BENCHMARK_INSTRUCTION_MARKER)
    if marker_index >= 0:
        return prompt[:marker_index].strip()
    return prompt


def final_answer_block(fields: list[sqlite3.Row]) -> str:
    max_field_len = max(len(latex_field_name(row["field_name"])) for row in fields)
    lines = [
        "**FINAL ANSWER**",
        "",
        r"\[",
        r"\begin{aligned}",
    ]
    for row in fields:
        field = latex_field_name(row["field_name"])
        padding = " " * (max_field_len - len(field) + 1)
        lines.append(rf"\mathrm{{{field}}}{padding}&=  \\")
    lines.extend(
        [
            r"\end{aligned}",
            r"\]",
        ]
    )
    return "\n".join(lines)


def build_prompt(original_question: str, scaffold: str, fields: list[sqlite3.Row]) -> str:
    parts = [
        "Solve the following scenario.",
        original_question_text(original_question),
        "Use the following answer structure. Keep the same sections and step order. Fill in the missing values by doing the calculation.",
        "Do not copy the placeholders.",
        "Do not add extra final-answer fields.",
        "Do not include more than one FINAL ANSWER block.",
        "Keep the final answer field names exactly as shown.",
        "Keep the final answer row order exactly as shown.",
        scaffold_derivation(scaffold),
        final_answer_block(fields),
    ]
    return "\n".join(parts)


def build_rows(
    scenarios: dict[str, sqlite3.Row],
    gold_fields: dict[str, list[sqlite3.Row]],
    model_names: list[str],
) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    sequence = 1
    for scenario_id in SCENARIO_ORDER:
        scenario = scenarios[scenario_id]
        prompt = build_prompt(
            scenario["prompt"] or "",
            STRUCTURED_PROMPTS[scenario_id],
            gold_fields[scenario_id],
        )
        for model_name in model_names:
            rows.append(
                {
                    "pilot_name": PILOT_NAME,
                    "prompt_sequence": str(sequence),
                    "scenario_id": scenario_id,
                    "scenario_title": scenario["title"] or "",
                    "category": scenario["category"] or "",
                    "model_name": model_name,
                    "prompt": prompt,
                    "prompt_sha256": sha256_text(prompt),
                }
            )
            sequence += 1
    return rows


def write_jsonl(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_report(path: Path, rows: list[dict[str, str]], model_names: list[str]) -> None:
    lines = [
        "# Structured Prompt Pilot v2",
        "",
        f"- Created at: {utc_now()}",
        f"- Scenarios: {len(SCENARIO_ORDER)}",
        f"- Model identities: {len(model_names)}",
        f"- Prompt assignments: {len(rows)}",
        "- Original question source: scenarios.prompt",
        "- Original question extraction: scenario problem statement before the original runner instruction/template tail",
        "- Scaffold source: user-provided eight scenario-specific structured prompts",
        "- Final-answer field order source: gold_fields.field_index",
        "",
        "## Scenarios",
        "",
        "| scenario_id | assignments | prompt_sha256 |",
        "|---|---:|---|",
    ]
    for scenario_id in SCENARIO_ORDER:
        prompt_hash = next(row["prompt_sha256"] for row in rows if row["scenario_id"] == scenario_id)
        lines.append(f"| {scenario_id} | {len(model_names)} | `{prompt_hash}` |")
    lines.extend(
        [
            "",
            "## Model Identities",
            "",
        ]
    )
    lines.extend(f"- {model_name}" for model_name in model_names)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_manifest(path: Path, rows: list[dict[str, str]], model_names: list[str]) -> None:
    manifest = {
        "pilot_name": PILOT_NAME,
        "created_at": utc_now(),
        "scenario_count": len(SCENARIO_ORDER),
        "scenario_ids": SCENARIO_ORDER,
        "model_identity_count": len(model_names),
        "model_names": model_names,
        "prompt_assignment_count": len(rows),
        "outputs": {
            "jsonl": "structured_prompt_pilot_v2.jsonl",
            "csv": "structured_prompt_pilot_v2.csv",
            "report": "STRUCTURED_PROMPT_PILOT_REPORT.md",
        },
    }
    path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", default=str(DEFAULT_DB))
    parser.add_argument("--output-dir", default=str(OUTPUT_DIR))
    args = parser.parse_args()

    db_path = Path(args.db)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    with connect(db_path) as con:
        scenarios = load_scenarios(con)
        gold_fields = load_gold_fields(con)
        model_names = load_model_names(con)

    rows = build_rows(scenarios, gold_fields, model_names)
    write_jsonl(output_dir / "structured_prompt_pilot_v2.jsonl", rows)
    write_csv(output_dir / "structured_prompt_pilot_v2.csv", rows)
    write_report(output_dir / "STRUCTURED_PROMPT_PILOT_REPORT.md", rows, model_names)
    write_manifest(output_dir / "manifest.json", rows, model_names)

    print(f"pilot_name={PILOT_NAME}")
    print(f"scenario_count={len(SCENARIO_ORDER)}")
    print(f"model_identity_count={len(model_names)}")
    print(f"prompt_assignment_count={len(rows)}")
    print(f"output_dir={output_dir}")


if __name__ == "__main__":
    main()
