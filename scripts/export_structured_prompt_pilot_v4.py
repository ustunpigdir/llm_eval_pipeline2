#!/usr/bin/env python3
"""Export and preflight structured-prompt pilot v4."""
from __future__ import annotations

import csv
import hashlib
import json
import re
import sqlite3
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "learning.db"
OUTPUT_DIR = ROOT / "outputs" / "structured_prompt_pilot_v4"
WORKED_DIR = ROOT / "outputs" / "structured_prompt_pilot_v2" / "pdf_review_source" / "worked_solutions"
PILOT_NAME = "structured_prompt_pilot_v4"
BENCHMARK_ID = "scientific_reasoning_32_v1"

SCENARIO_ORDER = [
    "CM_KAPITZA_001",
    "COS_DESITTER_001",
    "GR_PERI_001",
    "QFT_UNRUH_001",
    "QI_HOLEVO_001",
    "QM_AB_001",
    "SR_TWIN_001",
    "STAT_LANDAUER_001",
]

USED_SCENARIOS = {
    "CM_FOUCAULT_001",
    "COS_CMB_001",
    "GR_ISCO_001",
    "QFT_G2_001",
    "QI_TELEPORT_001",
    "QM_BERRY_001",
    "SR_ROCKET_001",
    "STAT_ISING_001",
    "CM_APSIDAL_001",
    "COS_DL_001",
    "GR_GPS_001",
    "QFT_CASIMIR_001",
    "QI_WERNER_001",
    "QM_TUNNEL_001",
    "SR_BELL_001",
    "STAT_BEC_001",
}

MODEL_IDENTITIES = [
    {
        "model_id": "model_gemma3_12b",
        "model_label": "Gemma 3 12B IT",
        "provider": "OpenAI-compatible",
        "model": "google/gemma-3-12b-it",
    },
    {
        "model_id": "model_gemma3_27b",
        "model_label": "Gemma 3 27B IT",
        "provider": "OpenAI-compatible",
        "model": "google/gemma-3-27b-it",
    },
    {
        "model_id": "model_gemma4_31b",
        "model_label": "Gemma 4 31B IT",
        "provider": "OpenAI-compatible",
        "model": "google/gemma-4-31b-it",
    },
    {
        "model_id": "model_granite_41_8b",
        "model_label": "Granite 4.1 8B",
        "provider": "OpenAI-compatible",
        "model": "ibm-granite/granite-4.1-8b",
    },
    {
        "model_id": "model_llama_31_8b",
        "model_label": "Llama 3.1 8B Instruct",
        "provider": "OpenAI-compatible",
        "model": "meta-llama/llama-3.1-8b-instruct",
    },
    {
        "model_id": "model_ministral_8b",
        "model_label": "Ministral 3 8B",
        "provider": "OpenAI-compatible",
        "model": "mistralai/ministral-8b-2512",
    },
    {
        "model_id": "model_mistral_nemo_12b",
        "model_label": "Mistral NeMo 12B",
        "provider": "OpenAI-compatible",
        "model": "mistralai/mistral-nemo",
    },
    {
        "model_id": "model_mistral_small_32",
        "model_label": "Mistral Small 3.2 24B Instruct",
        "provider": "OpenAI-compatible",
        "model": "mistral-small-2506",
    },
]

BENCHMARK_INSTRUCTION_MARKER = "\nYou are solving a scientific reasoning benchmark."
FINAL_ANSWER_RE = re.compile(r"\*\*FINAL ANSWER\*\*", re.IGNORECASE)
SECTION_RE = re.compile(r"^##\s+([A-Z0-9_]+)\b.*?(?=^##\s+|\Z)", re.MULTILINE | re.DOTALL)


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def connect_ro() -> sqlite3.Connection:
    con = sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)
    con.row_factory = sqlite3.Row
    return con


def latex_field_name(field_name: str) -> str:
    return field_name.replace("_", r"\_")


def original_question_text(db_prompt: str) -> str:
    prompt = db_prompt.strip()
    marker_index = prompt.find(BENCHMARK_INSTRUCTION_MARKER)
    if marker_index >= 0:
        return prompt[:marker_index].strip()
    return prompt


def load_scenarios(con: sqlite3.Connection) -> dict[str, sqlite3.Row]:
    if set(SCENARIO_ORDER) & USED_SCENARIOS:
        reused = sorted(set(SCENARIO_ORDER) & USED_SCENARIOS)
        raise SystemExit("v4 scenario set reuses prior scenario(s): " + ", ".join(reused))
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
        SELECT scenario_id, field_index, field_name, expected_value_raw, expected_value_num
        FROM gold_fields
        WHERE benchmark_id = ? AND scenario_id IN ({placeholders})
        ORDER BY scenario_id, field_index
        """,
        (BENCHMARK_ID, *SCENARIO_ORDER),
    ).fetchall()
    by_scenario: dict[str, list[sqlite3.Row]] = {scenario_id: [] for scenario_id in SCENARIO_ORDER}
    for row in rows:
        by_scenario[row["scenario_id"]].append(row)
    missing = [scenario_id for scenario_id, fields in by_scenario.items() if not fields]
    if missing:
        raise SystemExit("Missing gold field(s) in DB: " + ", ".join(missing))
    return by_scenario


def load_worked_sections() -> dict[str, str]:
    sections: dict[str, str] = {}
    for path in sorted(WORKED_DIR.glob("worked_solutions_batch*.md")):
        text = path.read_text(encoding="utf-8")
        for match in SECTION_RE.finditer(text):
            sections[match.group(1)] = match.group(0).strip()
    missing = [scenario_id for scenario_id in SCENARIO_ORDER if scenario_id not in sections]
    if missing:
        raise SystemExit("Missing worked-solution section(s): " + ", ".join(missing))
    return sections


def derivation_from_worked_section(section: str) -> str:
    derivation_start = section.find("**Derivation**")
    final_match = FINAL_ANSWER_RE.search(section)
    if derivation_start < 0 or final_match is None:
        raise SystemExit("Worked solution is missing Derivation or FINAL ANSWER marker")
    return section[derivation_start:final_match.start()].strip()


def protected_tokens(text: str) -> tuple[str, dict[str, str]]:
    protected = [
        "2GM/c²",
        "3GM/c²",
        "6GM/c²",
        "a²ω² > 2gL",
        "2gL",
        "6π",
        "1/(1−e²)",
        "1/(1-e²)",
        "T = ℏH/(2πk_B)",
        "ℏH/(2πk_B)",
        "ℏa/(2πck_B)",
        "h/e",
        "kBT ln 2",
        "k_B T ln 2",
        "log₂",
        "log2",
        "2π",
        "1/2π",
        "1/d⁴",
        "α/(2π)",
        "2/3",
        "1/2",
        "ζ(3/2)",
        "ζ^{2/3}",
    ]
    replacements = {}
    for idx, value in enumerate(protected):
        token = f"@@PROTECTED_{idx}@@"
        text = text.replace(value, token)
        replacements[token] = value
    return text, replacements


def restore_tokens(text: str, replacements: dict[str, str]) -> str:
    for token, value in replacements.items():
        text = text.replace(token, value)
    return text


def expected_value_variants(value: str) -> set[str]:
    variants = {value.strip()}
    try:
        number = float(value)
    except (TypeError, ValueError):
        return {item for item in variants if item}
    variants.update(
        {
            f"{number}",
            f"{number:.1f}",
            f"{number:.2f}",
            f"{number:.3f}",
            f"{number:.4f}",
            f"{number:.5f}",
            f"{number:.6f}",
        }
    )
    if abs(number - round(number)) < 1e-12:
        variants.add(str(int(round(number))))
    return {item for item in variants if item}


def sanitize_derivation(derivation: str, fields: list[sqlite3.Row]) -> str:
    text, replacements = protected_tokens(derivation)
    for row in fields:
        for value in sorted(expected_value_variants(str(row["expected_value_raw"] or "")), key=len, reverse=True):
            text = re.sub(rf"(?<![\w.]){re.escape(value)}(?![\w.])", "____", text)

    # Blank explicit bold computed results and common evaluated RHS fragments while
    # leaving conceptual formulas and constants intact.
    text = re.sub(r"\*\*([+\-−]?\d[\d.,]*(?:\s*[×x]\s*10[⁻−-]?\d+)?(?:\s*[A-Za-zμ/²³⁴^._-]+)?)\*\*", "**____**", text)
    text = re.sub(r"=\s*\*\*p\s*>\s*([^*]+)\*\*", "= **p > ____**", text)
    text = re.sub(r"=\s*\*\*([^*]*\d[^*]*)\*\*", "= **____**", text)
    text = re.sub(r"⟹\s*\*\*([^*]*\d[^*]*)\*\*", "⟹ **____**", text)
    text = re.sub(r"→\s*\*\*([^*]*\d[^*]*)\*\*", "→ **____**", text)
    text = re.sub(r"≈\s*\*\*([^*]*\d[^*]*)\*\*", "≈ **____**", text)
    text = re.sub(r"\b\d+\.\d{3,}\b", "____", text)
    return restore_tokens(text, replacements)


def final_answer_block(fields: list[sqlite3.Row]) -> str:
    max_field_len = max(len(latex_field_name(row["field_name"])) for row in fields)
    lines = ["**FINAL ANSWER**", "", r"\[", r"\begin{aligned}"]
    for row in fields:
        field = latex_field_name(row["field_name"])
        padding = " " * (max_field_len - len(field) + 1)
        lines.append(rf"\mathrm{{{field}}}{padding}&=  \\")
    lines.extend([r"\end{aligned}", r"\]"])
    return "\n".join(lines)


def build_prompt(original_question: str, worked_section: str, fields: list[sqlite3.Row]) -> str:
    derivation = sanitize_derivation(derivation_from_worked_section(worked_section), fields)
    parts = [
        "Solve the following scenario.",
        original_question_text(original_question),
        "Use the following answer structure. Keep the same sections and step order. Fill in the missing values by doing the calculation.",
        "Do not copy the placeholders.",
        "Do not add extra final-answer fields.",
        "Do not include more than one FINAL ANSWER block.",
        "Keep the final answer field names exactly as shown.",
        "Keep the final answer row order exactly as shown.",
        derivation,
        final_answer_block(fields),
    ]
    return "\n".join(parts)


def final_answer_field_order(prompt: str) -> list[str]:
    match = re.search(r"\\begin\{aligned\}(.*?)\\end\{aligned\}", prompt, flags=re.DOTALL)
    if not match:
        return []
    fields = []
    for line in match.group(1).splitlines():
        field_match = re.search(r"\\mathrm\{([^}]+)\}", line)
        if field_match:
            fields.append(field_match.group(1).replace(r"\_", "_"))
    return fields


def leaked_gold_values(prompt: str, fields: list[sqlite3.Row]) -> list[str]:
    leaks = []
    question_start = prompt.find("Use the following answer structure.")
    scaffold = prompt[question_start:] if question_start >= 0 else prompt
    for row in fields:
        raw = str(row["expected_value_raw"] or "").strip()
        if raw and re.search(rf"(?<![\w.]){re.escape(raw)}(?![\w.])", scaffold):
            leaks.append(raw)
    return leaks


def build_rows(
    scenarios: dict[str, sqlite3.Row],
    gold_fields: dict[str, list[sqlite3.Row]],
    worked_sections: dict[str, str],
) -> list[dict[str, str]]:
    rows = []
    sequence = 1
    for scenario_id in SCENARIO_ORDER:
        scenario = scenarios[scenario_id]
        prompt = build_prompt(scenario["prompt"] or "", worked_sections[scenario_id], gold_fields[scenario_id])
        for model in MODEL_IDENTITIES:
            rows.append(
                {
                    "pilot_name": PILOT_NAME,
                    "prompt_mode": PILOT_NAME,
                    "prompt_sequence": str(sequence),
                    "scenario_id": scenario_id,
                    "scenario_title": scenario["title"] or "",
                    "category": scenario["category"] or "",
                    "model_id": model["model_id"],
                    "model_label": model["model_label"],
                    "provider": model["provider"],
                    "model": model["model"],
                    "trial": "1",
                    "prompt": prompt,
                    "prompt_sha256": sha256_text(prompt),
                }
            )
            sequence += 1
    return rows


def preflight(rows: list[dict[str, str]], scenarios: dict[str, sqlite3.Row], gold_fields: dict[str, list[sqlite3.Row]]) -> dict[str, Any]:
    scenario_summary: dict[str, dict[str, Any]] = defaultdict(
        lambda: {
            "assignment_count": 0,
            "original_question_present_count": 0,
            "final_answer_block_count_ok": 0,
            "final_answer_field_order_matches_db": True,
            "leaked_final_gold_values_detected": False,
            "placeholder_count": 0,
        }
    )
    row_results = []
    for row in rows:
        sid = row["scenario_id"]
        prompt = row["prompt"]
        question = original_question_text(scenarios[sid]["prompt"] or "")
        expected_order = [field["field_name"] for field in gold_fields[sid]]
        actual_order = final_answer_field_order(prompt)
        leaks = leaked_gold_values(prompt, gold_fields[sid])
        final_blocks = len(FINAL_ANSWER_RE.findall(prompt))
        placeholder_count = prompt.count("____")
        question_present = question in prompt
        prompt_begins_ok = not prompt.lstrip().startswith("**Derivation**")
        result = {
            "scenario_id": sid,
            "model_id": row["model_id"],
            "prompt_mode": row["prompt_mode"],
            "final_answer_field_count": len(actual_order),
            "leaked_gold_values_detected": bool(leaks),
            "original_question_present": question_present,
            "exactly_one_final_answer_block": final_blocks == 1,
            "field_order_matches_db": actual_order == expected_order,
            "placeholder_count": placeholder_count,
            "prompt_does_not_begin_with_derivation": prompt_begins_ok,
            "leaked_values": leaks,
        }
        row_results.append(result)
        summary = scenario_summary[sid]
        summary["assignment_count"] += 1
        summary["original_question_present_count"] += int(question_present)
        summary["final_answer_block_count_ok"] += int(final_blocks == 1)
        summary["final_answer_field_order_matches_db"] = summary["final_answer_field_order_matches_db"] and actual_order == expected_order
        summary["leaked_final_gold_values_detected"] = summary["leaked_final_gold_values_detected"] or bool(leaks)
        summary["placeholder_count"] = min(summary["placeholder_count"] or placeholder_count, placeholder_count)

    total = len(rows)
    validation = {
        "total_assignments": total,
        "scenario_count": len({row["scenario_id"] for row in rows}),
        "model_count": len({row["model_label"] for row in rows}),
        "nemotron_assignments": sum(1 for row in rows if "Nemotron" in row["model_label"]),
        "original_question_present": f"{sum(r['original_question_present'] for r in row_results)}/{total}",
        "exactly_one_final_answer_block": f"{sum(r['exactly_one_final_answer_block'] for r in row_results)}/{total}",
        "field_order_matches_db": f"{sum(r['field_order_matches_db'] for r in row_results)}/{total}",
        "leaked_final_gold_values": sum(len(r["leaked_values"]) for r in row_results),
        "placeholder_count_gt_zero": f"{sum(r['placeholder_count'] > 0 for r in row_results)}/{total}",
        "prompt_does_not_begin_with_derivation": all(r["prompt_does_not_begin_with_derivation"] for r in row_results),
        "scenario_summary": {sid: dict(scenario_summary[sid]) for sid in SCENARIO_ORDER},
        "row_results": row_results,
    }
    failures = []
    if validation["total_assignments"] != 64:
        failures.append("total_assignments")
    if validation["scenario_count"] != 8:
        failures.append("scenario_count")
    if validation["model_count"] != 8:
        failures.append("model_count")
    if validation["nemotron_assignments"] != 0:
        failures.append("nemotron_assignments")
    if validation["original_question_present"] != "64/64":
        failures.append("original_question_present")
    if validation["exactly_one_final_answer_block"] != "64/64":
        failures.append("exactly_one_final_answer_block")
    if validation["field_order_matches_db"] != "64/64":
        failures.append("field_order_matches_db")
    if validation["leaked_final_gold_values"] != 0:
        failures.append("leaked_final_gold_values")
    if validation["placeholder_count_gt_zero"] != "64/64":
        failures.append("placeholder_count_gt_zero")
    if not validation["prompt_does_not_begin_with_derivation"]:
        failures.append("prompt_does_not_begin_with_derivation")
    validation["passed"] = not failures
    validation["failures"] = failures
    return validation


def write_jsonl(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_run_plan(path: Path, rows: list[dict[str, str]]) -> None:
    items = []
    for row in rows:
        items.append(
            {
                "scenario_id": row["scenario_id"],
                "scenario_title": row["scenario_title"],
                "scenario_category": row["category"],
                "model_id": row["model_id"],
                "model_label": row["model_label"],
                "provider": row["provider"],
                "model": row["model"],
                "trial": 1,
                "prompt": row["prompt"],
                "system_prompt": "",
                "status": "PLANNED",
                "prompt_mode": PILOT_NAME,
                "prompt_sequence": int(row["prompt_sequence"]),
            }
        )
    plan = {
        "run_name": "Structured prompt pilot v4 single-trial",
        "prompt_mode": PILOT_NAME,
        "created_at": utc_now(),
        "input_pack": str((OUTPUT_DIR / "structured_prompt_pilot_v4.jsonl").resolve()),
        "output_filename": "structured_prompt_pilot_v4_runs.json",
        "workers": 4,
        "items": items,
    }
    path.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_report(path: Path, rows: list[dict[str, str]], validation: dict[str, Any]) -> None:
    lines = [
        "# Structured Prompt Pilot v4",
        "",
        f"- Created at: {utc_now()}",
        f"- Prompt mode: {PILOT_NAME}",
        f"- Scenarios: {validation['scenario_count']}",
        f"- Model identities: {validation['model_count']}",
        f"- Prompt assignments: {validation['total_assignments']}",
        "- Original question source: scenarios.prompt",
        "- Scaffold source: locked worked_solutions_batch1.md through worked_solutions_batch7.md",
        "- Final-answer field order source: gold_fields.field_index",
        "- Nemotron excluded: yes",
        "",
        "## Preflight Validation",
        "",
    ]
    for key in [
        "total_assignments",
        "scenario_count",
        "model_count",
        "nemotron_assignments",
        "original_question_present",
        "exactly_one_final_answer_block",
        "field_order_matches_db",
        "leaked_final_gold_values",
        "placeholder_count_gt_zero",
        "prompt_does_not_begin_with_derivation",
        "passed",
    ]:
        lines.append(f"- {key}: {validation[key]}")
    lines.extend(
        [
            "",
            "## Scenario Preflight Table",
            "",
            "| scenario_id | assignment_count | original_question_present_count | final_answer_block_count_ok | final_answer_field_order_matches_db | leaked_final_gold_values_detected | placeholder_count |",
            "|---|---:|---:|---:|---|---|---:|",
        ]
    )
    for sid in SCENARIO_ORDER:
        row = validation["scenario_summary"][sid]
        lines.append(
            f"| {sid} | {row['assignment_count']} | {row['original_question_present_count']} | "
            f"{row['final_answer_block_count_ok']} | {row['final_answer_field_order_matches_db']} | "
            f"{row['leaked_final_gold_values_detected']} | {row['placeholder_count']} |"
        )
    lines.extend(["", "## Model Identities", ""])
    lines.extend(f"- {model['model_label']}" for model in MODEL_IDENTITIES)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_manifest(path: Path, rows: list[dict[str, str]], validation: dict[str, Any]) -> None:
    manifest = {
        "pilot_name": PILOT_NAME,
        "created_at": utc_now(),
        "scenario_count": len(SCENARIO_ORDER),
        "scenario_ids": SCENARIO_ORDER,
        "excluded_scenario_ids": sorted(USED_SCENARIOS),
        "model_identity_count": len(MODEL_IDENTITIES),
        "model_names": [model["model_label"] for model in MODEL_IDENTITIES],
        "excluded_model_names": ["NVIDIA Nemotron 3 Nano 30B-A3B"],
        "prompt_assignment_count": len(rows),
        "preflight_validation": {k: v for k, v in validation.items() if k != "row_results"},
        "outputs": {
            "jsonl": "structured_prompt_pilot_v4.jsonl",
            "csv": "structured_prompt_pilot_v4.csv",
            "report": "STRUCTURED_PROMPT_PILOT_V4_REPORT.md",
            "run_plan": "structured_prompt_pilot_v4_run_plan.json",
        },
    }
    path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> None:
    before_mtime = DB_PATH.stat().st_mtime_ns
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with connect_ro() as con:
        scenarios = load_scenarios(con)
        gold_fields = load_gold_fields(con)
    worked_sections = load_worked_sections()
    rows = build_rows(scenarios, gold_fields, worked_sections)
    validation = preflight(rows, scenarios, gold_fields)
    if not validation["passed"]:
        raise SystemExit("Preflight failed: " + ", ".join(validation["failures"]))

    write_jsonl(OUTPUT_DIR / "structured_prompt_pilot_v4.jsonl", rows)
    write_csv(OUTPUT_DIR / "structured_prompt_pilot_v4.csv", rows)
    write_run_plan(OUTPUT_DIR / "structured_prompt_pilot_v4_run_plan.json", rows)
    write_report(OUTPUT_DIR / "STRUCTURED_PROMPT_PILOT_V4_REPORT.md", rows, validation)
    write_manifest(OUTPUT_DIR / "manifest.json", rows, validation)

    print(f"prompt_mode={PILOT_NAME}")
    print(f"total_assignments={validation['total_assignments']}")
    print(f"scenario_count={validation['scenario_count']}")
    print(f"model_count={validation['model_count']}")
    print(f"nemotron_assignments={validation['nemotron_assignments']}")
    print(f"original_question_present={validation['original_question_present']}")
    print(f"exactly_one_final_answer_block={validation['exactly_one_final_answer_block']}")
    print(f"field_order_matches_db={validation['field_order_matches_db']}")
    print(f"leaked_final_gold_values={validation['leaked_final_gold_values']}")
    print(f"placeholder_count_gt_zero={validation['placeholder_count_gt_zero']}")
    print(f"prompt_does_not_begin_with_derivation={validation['prompt_does_not_begin_with_derivation']}")
    print("scenario_id,assignment_count,original_question_present_count,final_answer_block_count_ok,final_answer_field_order_matches_db,leaked_final_gold_values_detected,placeholder_count")
    for sid in SCENARIO_ORDER:
        row = validation["scenario_summary"][sid]
        print(
            f"{sid},{row['assignment_count']},{row['original_question_present_count']},"
            f"{row['final_answer_block_count_ok']},{row['final_answer_field_order_matches_db']},"
            f"{row['leaked_final_gold_values_detected']},{row['placeholder_count']}"
        )
    print(f"learning.db modified={'yes' if DB_PATH.stat().st_mtime_ns != before_mtime else 'no'}")
    print(f"output_dir={OUTPUT_DIR}")


if __name__ == "__main__":
    main()
