#!/usr/bin/env python3
"""Build a manual audit packet for large numeric failure gate candidates."""
from __future__ import annotations

import csv
import json
import math
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from statistics import median
from typing import Any

from run_soft_numeric_fail_layer_v1 import PROTECTED_PATHS, ROOT, fstr, path_state, read_csv, write_csv, write_json


SOURCE_DIR = ROOT / "outputs" / "large_numeric_failure_gt100pct_v1"
OUT_DIR = ROOT / "outputs" / "large_numeric_failure_manual_audit_packet_v1"

FIELD_PATH = SOURCE_DIR / "large_numeric_failure_field_level.csv"
ROW_PATH = SOURCE_DIR / "large_numeric_failure_row_level.csv"
PATTERN_PATH = SOURCE_DIR / "large_numeric_failure_by_failure_pattern.csv"
GATE_PATH = SOURCE_DIR / "large_numeric_failure_gate_candidates.csv"
EXTREME_PATH = SOURCE_DIR / "large_numeric_failure_extreme_examples.csv"

PLUS_ONE_PATH = ROOT / "outputs" / "plus_one_percentage_point_numeric_tolerance_layer_v1" / "plus_one_pp_numeric_row_labels.csv"

CARD_FIELDS = [
    "card_id",
    "suggested_gate",
    "source_run_id",
    "batch",
    "scenario_id",
    "category",
    "model_name",
    "field_name",
    "expected_value",
    "extracted_value",
    "abs_error",
    "rel_error",
    "rel_error_percent",
    "abs_extracted_over_expected_ratio",
    "signed_extracted_over_expected_ratio",
    "log10_abs_ratio",
    "original_rel_tolerance",
    "original_abs_tolerance",
    "sign_match",
    "preliminary_failure_pattern",
    "possible_factor_2_error",
    "possible_factor_pi_error",
    "possible_factor_10_error",
    "possible_factor_100_error",
    "possible_factor_1000_error",
    "possible_reciprocal_error",
    "possible_sign_flip",
    "possible_unit_scale_error",
    "possible_wrong_field_scale",
    "closest_wrong_field_if_available",
    "original_error_tags",
    "original_failed_fields",
    "plus_one_pp_secondary_category",
    "bertscore_reasoning_only_v2_f1",
    "rouge_l_f1",
    "chrf_score",
    "roscoe_reasoning_alignment",
    "plain_english_diagnosis",
    "audit_question",
    "recommended_manual_decision_options",
    "duplicate_cluster_note",
]

GATE_FILES = {
    "ORDER_OF_MAGNITUDE_GATE": "gate_examples_order_of_magnitude.md",
    "POWER_OF_TEN_SCALE_GATE": "gate_examples_power_of_ten.md",
    "SIGN_FLIP_GATE": "gate_examples_sign_flip.md",
    "WRONG_FIELD_SCALE_GATE": "gate_examples_wrong_field_scale.md",
    "EXTREME_EXPLOSION_GATE": "gate_examples_extreme_explosion.md",
    "UNCLASSIFIED_LARGE_GATE": "gate_examples_unclassified_large.md",
}

GATE_DESCRIPTIONS = {
    "ORDER_OF_MAGNITUDE_GATE": "The answer is at least 10 times too large or too small.",
    "EXTREME_EXPLOSION_GATE": "The answer is more than 1000% away from gold.",
    "POWER_OF_TEN_SCALE_GATE": "The answer looks shifted by decimal or scientific-notation scale.",
    "SIGN_FLIP_GATE": "The magnitude is similar but the sign is wrong.",
    "WRONG_FIELD_SCALE_GATE": "The answer looks closer to another field's expected value than to its own.",
    "UNCLASSIFIED_LARGE_GATE": "The answer is more than 100% wrong but did not match a simple ratio heuristic.",
}

DECISION_OPTIONS = "CONFIRM_GATE;REJECT_GATE_FALSE_POSITIVE;REASSIGN_TO_DIFFERENT_GATE;NEEDS_SCENARIO_CONTEXT;NEEDS_RAW_ANSWER_REVIEW"


def safe_float(value: Any) -> float | None:
    try:
        out = float(value)
    except (TypeError, ValueError):
        return None
    return out if math.isfinite(out) else None


def load_metric_context() -> dict[str, dict[str, str]]:
    specs = [
        (
            ROOT / "outputs" / "bertscore_reasoning_only_canonical_v2" / "bertscore_reasoning_only_canonical_v2.csv",
            {"bert_f1": "bertscore_reasoning_only_v2_f1"},
        ),
        (
            ROOT / "outputs" / "metric_comparison_analytics_rouge_l_v1" / "rouge_l_row_scores.csv",
            {"rouge_l_f1": "rouge_l_f1"},
        ),
        (
            ROOT / "outputs" / "metric_comparison_analytics_chrf_v1" / "chrf_row_scores.csv",
            {"chrf_score": "chrf_score"},
        ),
        (
            ROOT / "outputs" / "metric_comparison_analytics_roscoe_full_v1" / "roscoe_full_row_scores.csv",
            {"reasoning_alignment": "roscoe_reasoning_alignment"},
        ),
    ]
    context: dict[str, dict[str, str]] = defaultdict(dict)
    for path, mapping in specs:
        if not path.exists():
            continue
        for row in read_csv(path):
            run_id = row.get("source_run_id", "")
            if not run_id:
                continue
            for src, dst in mapping.items():
                context[run_id][dst] = row.get(src, "")
    return dict(context)


def load_plus_one_context() -> dict[str, str]:
    if not PLUS_ONE_PATH.exists():
        return {}
    return {row["source_run_id"]: row.get("secondary_numeric_category", "") for row in read_csv(PLUS_ONE_PATH)}


def as_ratio_text(row: dict[str, str]) -> str:
    ratio = safe_float(row.get("abs_extracted_over_expected_ratio"))
    if ratio is None:
        return "an unavailable ratio"
    if ratio >= 1000:
        return f"about {ratio:.1f} times"
    if ratio >= 10:
        return f"about {ratio:.2f} times"
    return f"about {ratio:.3f} times"


def diagnosis(row: dict[str, str], gate: str) -> str:
    ratio_text = as_ratio_text(row)
    rel_pct = safe_float(row.get("rel_error_percent"))
    rel_text = f"{rel_pct:.2f}%" if rel_pct is not None else "more than 100%"
    if gate == "SIGN_FLIP_GATE":
        return f"The model value has the opposite sign while the magnitude is close, producing {rel_text} relative error."
    if gate == "POWER_OF_TEN_SCALE_GATE":
        return f"The model value is {ratio_text} the gold value, consistent with a decimal or power-of-ten scale mistake."
    if gate == "WRONG_FIELD_SCALE_GATE":
        closest = row.get("wrong_field_scale_closest_field") or "another field"
        return f"The extracted value is closer to {closest} than to this field's gold value, suggesting a field-scale mixup."
    if gate == "EXTREME_EXPLOSION_GATE":
        return f"The numeric distance is extreme: relative error is {rel_text}, so this is not a tolerance-boundary error."
    if gate == "ORDER_OF_MAGNITUDE_GATE":
        return f"The model value is {ratio_text} the gold value, indicating an order-of-magnitude scale error."
    return f"The field is more than 100% away from gold but did not match a simple gate heuristic."


def audit_question(gate: str) -> str:
    if gate == "WRONG_FIELD_SCALE_GATE":
        return "Does this value genuinely correspond to another field, or is the ratio match accidental?"
    if gate == "SIGN_FLIP_GATE":
        return "Is this a genuine sign-convention mistake, or did the prompt allow the opposite convention?"
    if gate == "POWER_OF_TEN_SCALE_GATE":
        return "Does this look like a decimal/scientific-notation scale mistake, or a different conceptual error?"
    if gate == "EXTREME_EXPLOSION_GATE":
        return "Is this an extreme magnitude failure suitable for a generic gate, or does it need scenario context?"
    if gate == "ORDER_OF_MAGNITUDE_GATE":
        return "Does this look like a genuine order-of-magnitude mistake, or does the value correspond to another field/unit?"
    return "What is the simplest human-readable explanation for this large numeric miss?"


def source_key(row: dict[str, str], gate: str) -> tuple[str, str, str]:
    return (row["source_run_id"], row["field_name"], gate)


def select_cards(field_rows: list[dict[str, str]]) -> list[tuple[str, dict[str, str]]]:
    selected: list[tuple[str, dict[str, str]]] = []
    used: set[tuple[str, str, str]] = set()

    def add(gate: str, rows: list[dict[str, str]], limit: int | None = None) -> None:
        count = 0
        cluster_seen: set[tuple[str, str]] = set()
        for row in rows:
            cluster = (row["source_run_id"], row.get("preliminary_failure_pattern", ""))
            # Keep one representative for same-row/same-pattern clusters unless the field is a named repeated gate target.
            if cluster in cluster_seen and gate not in {"EXTREME_EXPLOSION_GATE"}:
                continue
            key = source_key(row, gate)
            if key in used:
                continue
            selected.append((gate, row))
            used.add(key)
            cluster_seen.add(cluster)
            count += 1
            if limit is not None and count >= limit:
                break

    by_rel = sorted(field_rows, key=lambda r: safe_float(r.get("rel_error")) or -1, reverse=True)
    order_rows = [r for r in field_rows if r.get("preliminary_failure_pattern") == "ORDER_OF_MAGNITUDE_GT10X"]
    top_order = sorted(order_rows, key=lambda r: safe_float(r.get("rel_error")) or -1, reverse=True)[:8]
    moderate_order = [r for r in sorted(order_rows, key=lambda r: safe_float(r.get("rel_error")) or 0) if (safe_float(r.get("rel_error")) or 0) <= 100][:5]
    add("ORDER_OF_MAGNITUDE_GATE", top_order + moderate_order, 13)
    add("EXTREME_EXPLOSION_GATE", [r for r in by_rel if (safe_float(r.get("rel_error")) or 0) > 10], 10)
    add("POWER_OF_TEN_SCALE_GATE", [r for r in field_rows if r.get("preliminary_failure_pattern") == "DECIMAL_OR_POWER_OF_TEN_SCALE"], 10)
    add("SIGN_FLIP_GATE", [r for r in field_rows if r.get("preliminary_failure_pattern") == "SIGN_FLIP"], 10)
    add("WRONG_FIELD_SCALE_GATE", [r for r in field_rows if r.get("preliminary_failure_pattern") == "WRONG_FIELD_SCALE" or r.get("possible_wrong_field_scale") == "true"], 10)
    add("UNCLASSIFIED_LARGE_GATE", sorted([r for r in field_rows if r.get("preliminary_failure_pattern") == "LARGE_NUMERIC_GT100PCT_UNCLASSIFIED"], key=lambda r: safe_float(r.get("rel_error")) or -1, reverse=True), 10)
    return selected


def build_cards() -> list[dict[str, Any]]:
    field_rows = read_csv(FIELD_PATH)
    plus_one = load_plus_one_context()
    metrics = load_metric_context()
    selected = select_cards(field_rows)
    duplicate_counts = Counter((row["source_run_id"], row["preliminary_failure_pattern"]) for _, row in selected)
    cards = []
    for index, (gate, row) in enumerate(selected, start=1):
        run_id = row["source_run_id"]
        metric_context = metrics.get(run_id, {})
        card = {
            "card_id": f"Card {index:03d}",
            "suggested_gate": gate,
            "source_run_id": run_id,
            "batch": row.get("batch", ""),
            "scenario_id": row.get("scenario_id", ""),
            "category": row.get("category", ""),
            "model_name": row.get("model_name", ""),
            "field_name": row.get("field_name", ""),
            "expected_value": row.get("expected_value", ""),
            "extracted_value": row.get("extracted_value", ""),
            "abs_error": row.get("abs_error", ""),
            "rel_error": row.get("rel_error", ""),
            "rel_error_percent": row.get("rel_error_percent", ""),
            "abs_extracted_over_expected_ratio": row.get("abs_extracted_over_expected_ratio", ""),
            "signed_extracted_over_expected_ratio": row.get("signed_extracted_over_expected_ratio", ""),
            "log10_abs_ratio": row.get("log10_abs_ratio", ""),
            "original_rel_tolerance": row.get("original_rel_tolerance", ""),
            "original_abs_tolerance": row.get("original_abs_tolerance", ""),
            "sign_match": row.get("sign_match", ""),
            "preliminary_failure_pattern": row.get("preliminary_failure_pattern", ""),
            "possible_factor_2_error": row.get("possible_factor_2_error", ""),
            "possible_factor_pi_error": row.get("possible_factor_pi_error", ""),
            "possible_factor_10_error": row.get("possible_factor_10_error", ""),
            "possible_factor_100_error": row.get("possible_factor_100_error", ""),
            "possible_factor_1000_error": row.get("possible_factor_1000_error", ""),
            "possible_reciprocal_error": row.get("possible_reciprocal_error", ""),
            "possible_sign_flip": row.get("possible_sign_flip", ""),
            "possible_unit_scale_error": row.get("possible_unit_scale_error", ""),
            "possible_wrong_field_scale": row.get("possible_wrong_field_scale", ""),
            "closest_wrong_field_if_available": row.get("wrong_field_scale_closest_field", ""),
            "original_error_tags": row.get("original_error_tags", ""),
            "original_failed_fields": row.get("original_failed_fields", ""),
            "plus_one_pp_secondary_category": plus_one.get(run_id, ""),
            "bertscore_reasoning_only_v2_f1": metric_context.get("bertscore_reasoning_only_v2_f1", ""),
            "rouge_l_f1": metric_context.get("rouge_l_f1", ""),
            "chrf_score": metric_context.get("chrf_score", ""),
            "roscoe_reasoning_alignment": metric_context.get("roscoe_reasoning_alignment", ""),
            "plain_english_diagnosis": diagnosis(row, gate),
            "audit_question": audit_question(gate),
            "recommended_manual_decision_options": DECISION_OPTIONS,
            "duplicate_cluster_note": "same-row pattern cluster" if duplicate_counts[(run_id, row["preliminary_failure_pattern"])] > 1 else "",
        }
        cards.append(card)
    return cards


def summarize_gate_easy(cards: list[dict[str, Any]]) -> list[dict[str, Any]]:
    field_rows = read_csv(FIELD_PATH)
    gates = read_csv(GATE_PATH)
    out = []
    for gate in gates:
        name = gate["gate_name"]
        if name not in GATE_DESCRIPTIONS:
            continue
        detected = []
        if name == "ORDER_OF_MAGNITUDE_GATE":
            detected = [r for r in field_rows if safe_float(r.get("log10_abs_ratio")) is not None and abs(float(r["log10_abs_ratio"])) >= 1]
        elif name == "EXTREME_EXPLOSION_GATE":
            detected = [r for r in field_rows if (safe_float(r.get("rel_error")) or 0) > 10]
        elif name == "POWER_OF_TEN_SCALE_GATE":
            detected = [r for r in field_rows if r.get("possible_factor_10_error") == "true" or r.get("possible_factor_100_error") == "true" or r.get("possible_factor_1000_error") == "true"]
        elif name == "SIGN_FLIP_GATE":
            detected = [r for r in field_rows if r.get("possible_sign_flip") == "true"]
        elif name == "WRONG_FIELD_SCALE_GATE":
            detected = [r for r in field_rows if r.get("possible_wrong_field_scale") == "true"]
        rels = [safe_float(r.get("rel_error")) for r in detected]
        rels = [r for r in rels if r is not None]
        out.append(
            {
                "gate_name": name,
                "fields_detected": gate.get("fields_detected_count", "0"),
                "rows_detected": gate.get("rows_detected_count", "0"),
                "scenarios_affected": len({r["scenario_id"] for r in detected}),
                "models_affected": len({r["model_name"] for r in detected}),
                "median_rel_error": fstr(median(rels)) if rels else "",
                "max_rel_error": fstr(max(rels)) if rels else "",
                "easy_description": GATE_DESCRIPTIONS[name],
                "why_it_might_be_useful": "Large numeric misses are often easier to review with this gate-specific cue.",
                "false_positive_risk": gate.get("likely_false_positive_risk", ""),
                "recommended_next_action": "manual_audit_before_formalizing" if int(gate.get("fields_detected_count", "0")) else "ignore_until_observed",
            }
        )
    # Add unclassified pseudo-gate for packet completeness.
    unclassified = [r for r in field_rows if r.get("preliminary_failure_pattern") == "LARGE_NUMERIC_GT100PCT_UNCLASSIFIED"]
    rels = [safe_float(r.get("rel_error")) for r in unclassified]
    rels = [r for r in rels if r is not None]
    out.append(
        {
            "gate_name": "UNCLASSIFIED_LARGE_GATE",
            "fields_detected": len(unclassified),
            "rows_detected": len({r["source_run_id"] for r in unclassified}),
            "scenarios_affected": len({r["scenario_id"] for r in unclassified}),
            "models_affected": len({r["model_name"] for r in unclassified}),
            "median_rel_error": fstr(median(rels)) if rels else "",
            "max_rel_error": fstr(max(rels)) if rels else "",
            "easy_description": GATE_DESCRIPTIONS["UNCLASSIFIED_LARGE_GATE"],
            "why_it_might_be_useful": "This bucket catches large misses that need human inspection before a gate exists.",
            "false_positive_risk": "medium",
            "recommended_next_action": "inspect_for_new_gate_patterns",
        }
    )
    return out


def card_markdown(card: dict[str, Any]) -> str:
    ratio = card.get("abs_extracted_over_expected_ratio") or "unavailable"
    log_ratio = card.get("log10_abs_ratio") or "unavailable"
    return "\n".join(
        [
            f"### {card['card_id']} - {card['suggested_gate']}",
            "",
            f"**Scenario:** {card['scenario_id']}  ",
            f"**Model:** {card['model_name']}  ",
            f"**Batch:** {card['batch']}  ",
            f"**Field:** {card['field_name']}  ",
            "",
            "| Item | Value |",
            "|---|---:|",
            f"| Gold value | {card['expected_value']} |",
            f"| Model value | {card['extracted_value']} |",
            f"| Relative error | {card['rel_error']} |",
            f"| Relative error percent | {card['rel_error_percent']} |",
            f"| Model / gold ratio | {ratio} |",
            f"| log10 ratio | {log_ratio} |",
            f"| Original tolerance | rel={card['original_rel_tolerance']}; abs={card['original_abs_tolerance']} |",
            f"| Original field pass? | false |",
            f"| Preliminary pattern | {card['preliminary_failure_pattern']} |",
            "",
            "**Plain-English diagnosis:**  ",
            card["plain_english_diagnosis"],
            "",
            "**Possible gate:**  ",
            card["suggested_gate"],
            "",
            "**Audit question:**  ",
            card["audit_question"],
            "",
            "**Recommended manual decision options:**  ",
            card["recommended_manual_decision_options"],
            "",
            "**Notes:**  ",
            card.get("duplicate_cluster_note") or "No raw final-answer block included; normalized extracted value is shown.",
            "",
        ]
    )


def write_cards_md(cards: list[dict[str, Any]]) -> None:
    lines = ["# Gate Audit Cards", ""]
    for card in cards:
        lines.append(card_markdown(card))
    (OUT_DIR / "gate_audit_cards.md").write_text("\n".join(lines), encoding="utf-8")


def write_gate_files(cards: list[dict[str, Any]], summary: list[dict[str, Any]]) -> None:
    summary_by_gate = {row["gate_name"]: row for row in summary}
    for gate, filename in GATE_FILES.items():
        gate_cards = [card for card in cards if card["suggested_gate"] == gate]
        lines = [
            f"# {gate}",
            "",
            GATE_DESCRIPTIONS[gate],
            "",
            "## Count Summary",
            "",
        ]
        gate_summary = summary_by_gate.get(gate, {})
        if gate_summary:
            lines.extend(
                [
                    f"- fields_detected: {gate_summary.get('fields_detected', 0)}",
                    f"- rows_detected: {gate_summary.get('rows_detected', 0)}",
                    f"- false_positive_risk: {gate_summary.get('false_positive_risk', '')}",
                    "",
                ]
            )
        lines.extend(
            [
                "## Suggested Manual Decision Checklist",
                "",
                "- Does the ratio heuristic match the actual scientific mistake?",
                "- Could this be a field swap or unit/context issue instead?",
                "- Should this gate become a formal diagnostic flag?",
                "",
                "## Selected Audit Cards",
                "",
            ]
        )
        if gate_cards:
            for card in gate_cards:
                lines.append(card_markdown(card))
        else:
            lines.append("No examples selected for this gate.")
        (OUT_DIR / filename).write_text("\n".join(lines), encoding="utf-8")


def write_main_report(cards: list[dict[str, Any]], summary: list[dict[str, Any]]) -> None:
    cards_by_gate = Counter(card["suggested_gate"] for card in cards)
    lines = [
        "# Large Numeric Failure Manual Audit Packet v1",
        "",
        "## 1. Purpose",
        "",
        "Review candidate logical gates before formalizing them. This packet does not change deterministic labels.",
        "",
        "## 2. What This Packet Contains",
        "",
        "- One compact Markdown report",
        "- One audit-card file",
        "- One Markdown file per gate",
        "- CSV/JSON card data for later formal gate design",
        "",
        "## 3. One-Screen Summary",
        "",
        "- 98 fields above 100% relative error",
        "- 62 rows affected",
        "- 42 fields above 1000% relative error",
        "- strongest candidate gates: ORDER_OF_MAGNITUDE_GATE, EXTREME_EXPLOSION_GATE, POWER_OF_TEN_SCALE_GATE, SIGN_FLIP_GATE, WRONG_FIELD_SCALE_GATE",
        "",
        "## 4. Gate Candidates in Plain English",
        "",
    ]
    for gate in ["ORDER_OF_MAGNITUDE_GATE", "EXTREME_EXPLOSION_GATE", "POWER_OF_TEN_SCALE_GATE", "SIGN_FLIP_GATE", "WRONG_FIELD_SCALE_GATE"]:
        lines.append(f"- **{gate}:** {GATE_DESCRIPTIONS[gate]}")
    lines.extend(
        [
            "",
            "## 5. How to Read an Audit Card",
            "",
            "Start with the field, gold value, model value, relative error, ratio, and suggested gate. Then answer the audit question using the manual decision options.",
            "",
            "## 6. Recommended Audit Order",
            "",
            "1. ORDER_OF_MAGNITUDE_GATE",
            "2. EXTREME_EXPLOSION_GATE",
            "3. POWER_OF_TEN_SCALE_GATE",
            "4. SIGN_FLIP_GATE",
            "5. WRONG_FIELD_SCALE_GATE",
            "6. UNCLASSIFIED_LARGE_GATE",
            "",
            "## 7. Summary of Selected Examples",
            "",
            "| Gate | Cards |",
            "|---|---:|",
        ]
    )
    for gate, count in sorted(cards_by_gate.items()):
        lines.append(f"| {gate} | {count} |")
    lines.extend(
        [
            "",
            "## 8. Key Observations",
            "",
            "- Order-of-magnitude and extreme-explosion candidates are the broadest high-signal groups.",
            "- Sign-flip candidates are concentrated and easier to inspect manually.",
            "- Wrong-field-scale examples need scenario context before formalizing.",
            "",
            "## 9. Limitations",
            "",
            "- Raw final-answer blocks were not reconstructed; cards show normalized extracted values.",
            "- All gate labels are preliminary heuristic suggestions.",
            "- No labels or source artifacts were changed.",
            "",
            "## 10. Next Step After Manual Audit",
            "",
            "Mark each card with CONFIRM_GATE, REJECT_GATE_FALSE_POSITIVE, REASSIGN_TO_DIFFERENT_GATE, NEEDS_SCENARIO_CONTEXT, or NEEDS_RAW_ANSWER_REVIEW.",
        ]
    )
    (OUT_DIR / "LARGE_NUMERIC_FAILURE_MANUAL_AUDIT_PACKET.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_readme() -> None:
    lines = [
        "# Large Numeric Failure Manual Audit Packet v1",
        "",
        "This packet turns the large numeric failure report into human-readable audit cards for candidate logical gates.",
        "",
        "Source report: `outputs/large_numeric_failure_gt100pct_v1/`.",
        "",
        "Read `LARGE_NUMERIC_FAILURE_MANUAL_AUDIT_PACKET.md` first, then inspect individual gate files. Use `gate_audit_cards.csv` or `.json` if you want to record manual decisions programmatically.",
        "",
        "No deterministic labels were changed. No raw outputs, frozen metrics, or database contents were modified.",
        "",
        "Rerun with:",
        "",
        "```bash",
        ".venv/bin/python scripts/build_large_numeric_failure_manual_audit_packet_v1.py",
        "```",
    ]
    (OUT_DIR / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    before = {str(path.relative_to(ROOT)): path_state(path) for path in PROTECTED_PATHS}
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    cards = build_cards()
    summary = summarize_gate_easy(cards)
    write_csv(OUT_DIR / "gate_audit_cards.csv", cards, CARD_FIELDS)
    write_json(OUT_DIR / "gate_audit_cards.json", cards)
    write_csv(OUT_DIR / "gate_summary_easy_read.csv", summary, list(summary[0].keys()))
    write_cards_md(cards)
    write_gate_files(cards, summary)
    write_main_report(cards, summary)
    write_readme()
    after = {str(path.relative_to(ROOT)): path_state(path) for path in PROTECTED_PATHS}
    protected_unchanged = before == after
    output_files = [
        "README.md",
        "LARGE_NUMERIC_FAILURE_MANUAL_AUDIT_PACKET.md",
        "gate_audit_cards.md",
        "gate_audit_cards.csv",
        "gate_audit_cards.json",
        "gate_summary_easy_read.csv",
        "gate_examples_order_of_magnitude.md",
        "gate_examples_power_of_ten.md",
        "gate_examples_sign_flip.md",
        "gate_examples_wrong_field_scale.md",
        "gate_examples_extreme_explosion.md",
        "gate_examples_unclassified_large.md",
        "manual_audit_packet_manifest.json",
    ]
    manifest = {
        "artifact_name": "large_numeric_failure_manual_audit_packet_v1",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "input_artifacts": [
            str(FIELD_PATH.relative_to(ROOT)),
            str(ROW_PATH.relative_to(ROOT)),
            str(PATTERN_PATH.relative_to(ROOT)),
            str(GATE_PATH.relative_to(ROOT)),
            str(EXTREME_PATH.relative_to(ROOT)),
        ],
        "read_only": True,
        "learning_db_modified": False,
        "raw_outputs_modified": False,
        "frozen_metric_artifacts_modified": False,
        "model_calls_made": False,
        "external_llm_api_calls": False,
        "bertscore_run": False,
        "roscoe_run": False,
        "phase2_semantics_implemented": False,
        "source_gt100_field_count": 98,
        "source_rows_with_gt100_failure": 62,
        "source_gt1000_field_count": 42,
        "audit_cards_created": len(cards),
        "gates_covered": sorted(set(card["suggested_gate"] for card in cards)),
        "cards_by_gate": dict(sorted(Counter(card["suggested_gate"] for card in cards).items())),
        "raw_final_answer_blocks_included": False,
        "raw_answer_limitation": "Raw final-answer blocks were not reconstructed; normalized field values are used.",
        "protected_input_states_before": before,
        "protected_input_states_after": after,
        "protected_inputs_unchanged": protected_unchanged,
        "output_files": output_files,
    }
    write_json(OUT_DIR / "manual_audit_packet_manifest.json", manifest)
    print(f"audit_cards_created={len(cards)}")
    print(f"gates_covered={json.dumps(manifest['gates_covered'])}")
    print(f"cards_by_gate={json.dumps(manifest['cards_by_gate'], sort_keys=True)}")
    print(f"protected_inputs_unchanged={protected_unchanged}")
    print(f"output_dir={OUT_DIR.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
