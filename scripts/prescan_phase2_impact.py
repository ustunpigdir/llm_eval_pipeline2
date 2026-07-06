#!/usr/bin/env python3
"""Read-only Phase 2 impact pre-scan for structured-prompt Phase-1 artifacts."""
from __future__ import annotations

import csv
import json
import re
import sqlite3
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "learning.db"
OUTPUT_DIR = ROOT / "outputs" / "phase2_prescan_v1"
SUMMARY_DIR = ROOT / "outputs" / "structured_prompt_all32_summary_phase1_hardened"
BERT_NO_FINAL_DIR = ROOT / "outputs" / "bertscore_structured_all32_phase1_hardened_no_final_block_v1"

EXPECTED_TOTAL_RUNS = 264
EXPECTED_CLEAN = 252
EXPECTED_REVIEW = 12
EXPECTED_PASS = 117
EXPECTED_FAIL = 135
EXPECTED_SCENARIOS = 32

PHASE2_NOT_GRADEABLE_MARKERS = ("NOT_FOUND", "UNPARSEABLE", "FIELD_SET_MISMATCH", "GOLD_DATA_ERROR")
GOLD_ISSUE_MARKERS = ("GOLD_NON_NUMERIC", "GOLD_DATA_ERROR")
LOG_PATTERNS = ("log_{10}", "log_10", "log10", "log_{2}", "log_2", "log2")

FINAL_BLOCK_RE = re.compile(
    r"(?:^|\n)[ \t]*(?:#{1,6}[ \t]*)?(?:\*\*)?[ \t]*final[ \t]+answer[ \t]*(?:\*\*)?[ \t]*:?[ \t]*\n+"
    r"(?P<body>.*?)(?=(?:\n[ \t]*(?:#{1,6}[ \t]*)?(?:\*\*)?[ \t]*final[ \t]+answer)|\Z)",
    re.IGNORECASE | re.DOTALL,
)
ALIGNED_RE = re.compile(r"\\begin\{aligned\}(.*?)\\end\{aligned\}", re.DOTALL)
FIELD_LINE_RE = re.compile(r"\\mathrm\{([^}]+)\}\s*&?=\s*(.*?)(?:\\\\|$)")


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def load_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def batch_dir(batch_num: int) -> Path:
    return ROOT / "outputs" / f"structured_prompt_pilot_v{batch_num}"


def load_batch(batch_num: int) -> tuple[list[dict[str, Any]], list[dict[str, Any]], dict[str, dict[str, Any]]]:
    base = batch_dir(batch_num)
    autograde = read_json(base / "autograde_no_bert_v1" / f"structured_prompt_v{batch_num}_clean_autograde.json")
    review = read_json(base / "review_layer_v1" / "review_layer_v1.json")
    runs = {
        str(row["run_id"]): row
        for row in read_json(base / f"structured_prompt_pilot_v{batch_num}_runs.json")
    }
    return autograde, review, runs


def load_all_rows() -> tuple[list[dict[str, Any]], list[dict[str, Any]], dict[str, dict[str, Any]]]:
    clean_rows: list[dict[str, Any]] = []
    review_rows: list[dict[str, Any]] = []
    runs: dict[str, dict[str, Any]] = {}
    for batch_num in (2, 3, 4, 5):
        batch = f"V{batch_num}"
        autograde, review, batch_runs = load_batch(batch_num)
        runs.update(batch_runs)
        for row in autograde:
            clean_rows.append({**row, "batch": batch})
        for row in review:
            tagged = {**row, "batch": batch}
            if row.get("review_status") == "REVIEW":
                review_rows.append(tagged)
    return clean_rows, review_rows, runs


def split_tags(error_tags: str) -> list[str]:
    return [tag.strip() for tag in (error_tags or "").split(";") if tag.strip()]


def tag_contains(tags: list[str], marker: str) -> bool:
    return any(marker in tag for tag in tags)


def phase2_not_gradeable_reason(tags: list[str]) -> str:
    reasons = [marker for marker in PHASE2_NOT_GRADEABLE_MARKERS if tag_contains(tags, marker)]
    return ";".join(reasons)


def field_from_tag(tag: str) -> str:
    return tag.split(":", 1)[0] if ":" in tag else ""


def extract_normalized_fields(row: dict[str, Any]) -> dict[str, str]:
    raw = row.get("normalized_final_answer") or "{}"
    try:
        parsed = json.loads(raw)
    except Exception:
        return {}
    return {str(k): str(v) for k, v in parsed.items()}


def scan_fail_error_tags(clean_rows: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]], Counter[str], list[dict[str, Any]], list[dict[str, Any]]]:
    fail_rows = [row for row in clean_rows if row.get("deterministic_grade") == "FAIL"]
    out: list[dict[str, Any]] = []
    ng: list[dict[str, Any]] = []
    tag_counts: Counter[str] = Counter()
    explicit_log: list[dict[str, Any]] = []
    percent_ellipsis: list[dict[str, Any]] = []
    for row in fail_rows:
        tags = split_tags(row.get("error_tags", ""))
        for tag in tags:
            parts = tag.split(":")
            for idx in range(1, len(parts) + 1):
                tag_counts[":".join(parts[1:idx])] += 1
            if len(parts) >= 2:
                tag_counts[parts[1]] += 1
        reason = phase2_not_gradeable_reason(tags)
        would_ng = bool(reason)
        item = {
            "batch": row["batch"],
            "scenario_id": row.get("scenario_id", ""),
            "model_name": row.get("model_name", ""),
            "deterministic_grade": row.get("deterministic_grade", ""),
            "error_tags": row.get("error_tags", ""),
            "failed_fields": row.get("failed_fields", ""),
            "contains_mismatch": tag_contains(tags, "MISMATCH"),
            "contains_not_found": tag_contains(tags, "NOT_FOUND"),
            "contains_unparseable": tag_contains(tags, "UNPARSEABLE"),
            "contains_gold_data_issue": any(tag_contains(tags, marker) for marker in GOLD_ISSUE_MARKERS),
            "would_be_not_gradeable_under_phase2_rule": would_ng,
            "reason": reason or "all_failed_fields_are_gradeable_mismatch",
        }
        out.append(item)
        if would_ng:
            ng.append(
                {
                    "batch": row["batch"],
                    "scenario_id": row.get("scenario_id", ""),
                    "model_name": row.get("model_name", ""),
                    "current_grade": "FAIL",
                    "proposed_grade": "NOT_GRADEABLE",
                    "error_tags": row.get("error_tags", ""),
                    "failed_fields": row.get("failed_fields", ""),
                    "reason": reason,
                    "source_run_id": row.get("output_path_or_run_id", ""),
                }
            )
        values = extract_normalized_fields(row)
        for tag in tags:
            field = field_from_tag(tag)
            raw_value = values.get(field, "")
            hay = f"{field} {raw_value} {tag}"
            if any(pattern.lower() in hay.lower() for pattern in LOG_PATTERNS):
                explicit_log.append(
                    {
                        "batch": row["batch"],
                        "scenario_id": row.get("scenario_id", ""),
                        "model_name": row.get("model_name", ""),
                        "field_name": field,
                        "raw_value": raw_value,
                        "current_error_tag": tag,
                        "likely_impact": "may_parse_after_log_support",
                    }
                )
            if "%" in raw_value or "percent" in raw_value.lower() or "..." in raw_value or "…" in raw_value or re.search(r"\.\.+$", raw_value.strip()):
                percent_ellipsis.append(
                    {
                        "batch": row["batch"],
                        "scenario_id": row.get("scenario_id", ""),
                        "model_name": row.get("model_name", ""),
                        "field_name": field,
                        "raw_value": raw_value,
                        "risk_type": ";".join(
                            marker
                            for marker, present in {
                                "percent_symbol": "%" in raw_value,
                                "percent_word": "percent" in raw_value.lower(),
                                "ellipsis": "..." in raw_value or "…" in raw_value or bool(re.search(r"\.\.+$", raw_value.strip())),
                            }.items()
                            if present
                        ),
                        "current_error_tag": tag,
                    }
                )
    return out, ng, tag_counts, explicit_log, percent_ellipsis


def final_blocks(response: str) -> list[str]:
    return [match.group("body") for match in FINAL_BLOCK_RE.finditer(response or "")]


def fields_in_block(block: str) -> dict[str, list[str]]:
    aligned_match = ALIGNED_RE.search(block)
    text = aligned_match.group(1) if aligned_match else block
    fields: dict[str, list[str]] = defaultdict(list)
    for match in FIELD_LINE_RE.finditer(text):
        field = match.group(1).replace("\\_", "_").strip()
        value = match.group(2).strip()
        fields[field].append(value)
    return fields


def simple_reduce(value: str) -> str:
    return re.sub(r"\s+", "", value).strip().rstrip(".")


def scan_review_recovery(review_rows: list[dict[str, Any]], runs: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for row in review_rows:
        run = runs.get(str(row.get("output_path_or_run_id", "")), {})
        blocks = final_blocks(run.get("response", ""))
        helper = row.get("raw_helper_status", "")
        recovery_type = "unknown"
        evidence = f"final_answer_blocks={len(blocks)}"
        safe = False
        if helper == "ALL_BLANK":
            recovery_type = "all_blank"
        elif helper == "NO_VALID_BLOCK":
            recovery_type = "no_valid_block"
        elif helper == "CONFLICT":
            field_sets = [fields_in_block(block) for block in blocks]
            canonical = [json.dumps({k: [simple_reduce(v) for v in vals] for k, vals in sorted(fs.items())}, sort_keys=True) for fs in field_sets]
            if canonical and len(set(canonical)) == 1:
                recovery_type = "repeated_identical_block"
                safe = True
            else:
                recovery_type = "true_conflict"
            evidence = f"final_answer_blocks={len(blocks)};unique_canonical_blocks={len(set(canonical)) if canonical else 0}"
        elif len(blocks) > 1:
            recovery_type = "blank_template_after_filled_block"
            evidence = f"final_answer_blocks={len(blocks)}"
        out.append(
            {
                "batch": row["batch"],
                "scenario_id": row.get("scenario_id", ""),
                "model_name": row.get("model_name", ""),
                "helper_status": helper,
                "review_reason": row.get("review_reason", ""),
                "candidate_recovery_type": recovery_type,
                "evidence": evidence,
                "safe_to_recover_candidate": safe,
            }
        )
    return out


def scan_duplicate_fields(rows: list[dict[str, Any]], runs: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for row in rows:
        run_id = str(row.get("output_path_or_run_id", ""))
        run = runs.get(run_id, {})
        blocks = final_blocks(run.get("response", ""))
        for idx, block in enumerate(blocks, start=1):
            fields = fields_in_block(block)
            for field, values in fields.items():
                if len(values) <= 1:
                    continue
                reduced = [simple_reduce(value) for value in values]
                duplicate_type = "identical_values" if len(set(reduced)) == 1 else "conflicting_values"
                out.append(
                    {
                        "batch": row["batch"],
                        "scenario_id": row.get("scenario_id", ""),
                        "model_name": row.get("model_name", ""),
                        "helper_status": row.get("raw_helper_status", ""),
                        "block_index": idx,
                        "field_name": field,
                        "duplicate_count": len(values),
                        "raw_values": json.dumps(values, ensure_ascii=False),
                        "reduced_values_if_available": json.dumps(reduced, ensure_ascii=False),
                        "duplicate_type": duplicate_type,
                    }
                )
    return out


def scan_gold_data() -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    con = sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)
    con.row_factory = sqlite3.Row
    try:
        rows = [dict(row) for row in con.execute("SELECT scenario_id, field_name, expected_value_num, tolerance, tolerance_mode, field_index FROM gold_fields ORDER BY scenario_id, field_index")]
    finally:
        con.close()
    issues: list[dict[str, Any]] = []
    by_scenario: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        by_scenario[row["scenario_id"]].append(row)
        issue_bits = []
        if row["expected_value_num"] is None:
            issue_bits.append("expected_value_num_NULL")
        if row["tolerance"] is None:
            issue_bits.append("tolerance_NULL")
        if row["tolerance_mode"] in (None, ""):
            issue_bits.append("tolerance_mode_missing")
        elif row["tolerance_mode"] not in {"absolute", "relative"}:
            issue_bits.append("tolerance_mode_invalid")
        if issue_bits:
            issues.append({**row, "issue": ";".join(issue_bits)})
    for scenario_id, scenario_rows in by_scenario.items():
        field_indices = [row["field_index"] for row in scenario_rows]
        field_names = [row["field_name"] for row in scenario_rows]
        for dup_idx, count in Counter(field_indices).items():
            if count > 1:
                issues.append({"scenario_id": scenario_id, "field_name": "", "expected_value_num": "", "tolerance": "", "tolerance_mode": "", "field_index": dup_idx, "issue": "duplicate_field_index"})
        for dup_name, count in Counter(field_names).items():
            if count > 1:
                issues.append({"scenario_id": scenario_id, "field_name": dup_name, "expected_value_num": "", "tolerance": "", "tolerance_mode": "", "field_index": "", "issue": "duplicate_field_name"})
        expected = list(range(len(field_indices)))
        if sorted(field_indices) != expected:
            issues.append({"scenario_id": scenario_id, "field_name": "", "expected_value_num": "", "tolerance": "", "tolerance_mode": "", "field_index": json.dumps(field_indices), "issue": "non_contiguous_or_suspicious_field_index"})
    return issues, rows


def scan_bertscore_mismatches(clean_rows: list[dict[str, Any]], runs: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    warning_rows = load_csv(BERT_NO_FINAL_DIR / "final_block_removal_warnings.csv")
    clean_by_run = {str(row.get("output_path_or_run_id", "")): row for row in clean_rows}
    out: list[dict[str, Any]] = []
    for warning in warning_rows:
        if warning.get("final_block_removed_candidate") != "False":
            continue
        run_id = warning.get("source_run_id", "")
        clean = clean_by_run.get(run_id, {})
        run = runs.get(run_id, {})
        response = run.get("response", "")
        has_final = bool(re.search(r"final\s+answer", response, re.I))
        has_aligned = "\\begin{aligned}" in response
        reason = "final_heading_or_latex_shape_variant_not_matched"
        if has_final and not has_aligned:
            reason = "final_heading_without_aligned_latex_block"
        elif not has_final:
            reason = "no_literal_final_answer_heading_in_response"
        out.append(
            {
                "batch": warning.get("batch", ""),
                "scenario_id": warning.get("scenario_id", ""),
                "model_name": warning.get("model_name", ""),
                "source_run_id": run_id,
                "bertscore_final_block_removed_candidate": False,
                "extractor_helper_status": clean.get("raw_helper_status", ""),
                "extractor_block_found": bool(clean),
                "likely_reason_bertscore_removal_failed": reason,
                "recommended_fix": "reuse extractor final-answer block locator for BERTScore text transformation",
            }
        )
    return out


def version_skew_risks() -> list[str]:
    files = [
        ROOT / "extract_final_answers.py",
        ROOT / "scripts" / "create_structured_prompt_review_layer_v1.py",
        ROOT / "scripts" / "create_structured_prompt_v3_review_layer_v1.py",
        ROOT / "scripts" / "create_structured_prompt_v4_review_layer_v1.py",
        ROOT / "scripts" / "create_structured_prompt_v5_review_layer_v1.py",
        ROOT / "scripts" / "autograde_structured_prompt_v2_no_bert.py",
        ROOT / "scripts" / "autograde_structured_prompt_v3_no_bert.py",
        ROOT / "scripts" / "autograde_structured_prompt_v4_no_bert.py",
        ROOT / "scripts" / "autograde_structured_prompt_v5_no_bert.py",
        ROOT / "scripts" / "run_bertscore_structured_all32_phase1_hardened_no_final_block.py",
    ]
    risks = []
    for path in files:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        if "FINAL ANSWER" in text or "final answer" in text or "\\begin{aligned}" in text:
            risks.append(f"{path.relative_to(ROOT)} contains local final-answer/block regex or marker logic")
        if "FIELD_SET_MISMATCH" in text:
            risks.append(f"{path.relative_to(ROOT)} contains local FIELD_SET_MISMATCH handling")
    return sorted(set(risks))


def write_report(
    clean_rows: list[dict[str, Any]],
    review_rows: list[dict[str, Any]],
    fail_tag_counts: Counter[str],
    not_gradeable_rows: list[dict[str, Any]],
    explicit_log_rows: list[dict[str, Any]],
    review_recovery_rows: list[dict[str, Any]],
    duplicate_rows: list[dict[str, Any]],
    gold_issues: list[dict[str, Any]],
    percent_ellipsis_rows: list[dict[str, Any]],
    bert_mismatches: list[dict[str, Any]],
    risks: list[str],
    manifest: dict[str, Any],
) -> None:
    predicted_ng = len(not_gradeable_rows)
    predicted_fail = EXPECTED_FAIL - predicted_ng
    predicted_denominator = EXPECTED_PASS + predicted_fail
    predicted_rate = EXPECTED_PASS / predicted_denominator if predicted_denominator else 0.0
    duplicate_row_keys = {(row["batch"], row["scenario_id"], row["model_name"]) for row in duplicate_rows}
    conflicting_duplicate_keys = {(row["batch"], row["scenario_id"], row["model_name"]) for row in duplicate_rows if row["duplicate_type"] == "conflicting_values"}
    identical_duplicate_keys = {(row["batch"], row["scenario_id"], row["model_name"]) for row in duplicate_rows if row["duplicate_type"] == "identical_values"}
    lines = [
        "# Phase 2 Impact Pre-Scan",
        "",
        "## Executive Summary",
        "",
        f"- Current CLEAN rows: {len(clean_rows)}",
        f"- Current REVIEW rows: {len(review_rows)}",
        f"- Current PASS/FAIL: PASS={EXPECTED_PASS}, FAIL={EXPECTED_FAIL}",
        f"- Predicted NOT_GRADEABLE under scan-only rule: {predicted_ng}",
        f"- Predicted remaining FAIL after NOT_GRADEABLE split: {predicted_fail}",
        f"- Predicted gradeable denominator: {predicted_denominator}",
        f"- Predicted pass rate if only NOT_GRADEABLE semantics change: {predicted_rate:.6f}",
        "",
        "## Frozen Phase 1 Metrics",
        "",
        "- total_structured_runs: 264",
        "- CLEAN: 252",
        "- REVIEW: 12",
        "- PASS: 117",
        "- FAIL: 135",
        "- clean-row pass rate: 0.464286",
        "- extraction_status_distribution: {\"OK\": 252}",
        "- stability_decision: STABLE_NO_METRIC_CHANGE",
        "",
        "## FAIL Error-Tag Distribution",
        "",
        "| tag | count |",
        "| --- | ---: |",
    ]
    for tag, count in fail_tag_counts.most_common():
        if tag:
            lines.append(f"| {tag} | {count} |")
    lines.extend(
        [
            "",
            "## Predicted NOT_GRADEABLE Impact",
            "",
            f"- current_FAIL_count: {EXPECTED_FAIL}",
            f"- predicted_NOT_GRADEABLE_count: {predicted_ng}",
            f"- predicted_FAIL_count_after_phase2: {predicted_fail}",
            f"- predicted_PASS_count_after_phase2: {EXPECTED_PASS}",
            f"- predicted_gradeable_denominator: {predicted_denominator}",
            f"- predicted_phase2_pass_rate_if_only_NOT_GRADEABLE_semantics_change: {predicted_rate:.6f}",
            "",
            "## Explicit-Base Log Candidate Impact",
            "",
            f"- candidates: {len(explicit_log_rows)}",
            "",
            "## REVIEW Recovery Candidate Count",
            "",
            f"- REVIEW rows: {len(review_rows)}",
            f"- safe_to_recover_candidate: {sum(1 for row in review_recovery_rows if row['safe_to_recover_candidate'])}",
            f"- recovery types: {dict(Counter(row['candidate_recovery_type'] for row in review_recovery_rows))}",
            "",
            "## Duplicate-Field Scan",
            "",
            f"- duplicate field entries: {len(duplicate_rows)}",
            f"- rows_with_duplicate_fields: {len(duplicate_row_keys)}",
            f"- rows_with_conflicting_duplicate_fields: {len(conflicting_duplicate_keys)}",
            f"- rows_with_identical_duplicate_fields: {len(identical_duplicate_keys)}",
            "",
            "## Gold-Data Scan",
            "",
            f"- gold-data issue rows: {len(gold_issues)}",
            "",
            "## Percent/Ellipsis Risk Scan",
            "",
            f"- affected field entries: {len(percent_ellipsis_rows)}",
            f"- risk types: {dict(Counter(row['risk_type'] for row in percent_ellipsis_rows))}",
            "",
            "## BERTScore Block-Removal Mismatch Scan",
            "",
            f"- candidate removal mismatches: {len(bert_mismatches)}",
            "- Reference no-final warnings are expected because the reference parser already stops before final-answer sections.",
            "",
            "## Review/Autograder Version-Skew Risks",
            "",
        ]
    )
    if risks:
        lines.extend(f"- {risk}" for risk in risks)
    else:
        lines.append("- No obvious duplicated final-answer or FIELD_SET_MISMATCH logic found.")
    lines.extend(
        [
            "",
            "## Recommended Phase 2 Implementation Order",
            "",
            "1. Centralize final-answer block locating/extraction and reuse it for BERTScore text transforms.",
            "2. Add NOT_GRADEABLE semantics behind a reporting-only switch, using this pre-scan candidate list as a regression fixture.",
            "3. Add explicit-base log parsing, then re-run the pre-scan before changing grades.",
            "4. Add duplicate-field diagnostics before any numeric-aware conflict recovery.",
            "5. Validate gold-field metadata stays clean before changing tolerance semantics.",
            "",
            "## Phase 1 Freeze Recommendation",
            "",
            "- Phase 1 metrics should remain frozen. This scan does not justify rewriting Phase 1 artifacts.",
            "",
            "## Urgent Corrections Before Phase 2",
            "",
            "- The BERTScore no-final block transform should reuse extractor block logic before future metric runs.",
            "- No urgent DB or raw-output correction is indicated by this read-only scan.",
            "",
            "## Manifest",
            "",
            "```json",
            json.dumps(manifest, indent=2, sort_keys=True),
            "```",
        ]
    )
    (OUTPUT_DIR / "PHASE2_PRESCAN_REPORT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    clean_rows, review_rows, runs = load_all_rows()
    fail_error_rows, not_gradeable_rows, fail_tag_counts, explicit_log_rows, percent_ellipsis_rows = scan_fail_error_tags(clean_rows)
    review_recovery_rows = scan_review_recovery(review_rows, runs)
    duplicate_rows = scan_duplicate_fields(clean_rows + review_rows, runs)
    gold_issues, tolerance_rows = scan_gold_data()
    bert_mismatches = scan_bertscore_mismatches(clean_rows, runs)
    risks = version_skew_risks()

    fail_error_fields = [
        "batch",
        "scenario_id",
        "model_name",
        "deterministic_grade",
        "error_tags",
        "failed_fields",
        "contains_mismatch",
        "contains_not_found",
        "contains_unparseable",
        "contains_gold_data_issue",
        "would_be_not_gradeable_under_phase2_rule",
        "reason",
    ]
    write_csv(OUTPUT_DIR / "phase2_prescan_fail_error_tags.csv", fail_error_rows, fail_error_fields)
    write_csv(
        OUTPUT_DIR / "phase2_prescan_fail_to_not_gradeable_candidates.csv",
        not_gradeable_rows,
        ["batch", "scenario_id", "model_name", "current_grade", "proposed_grade", "error_tags", "failed_fields", "reason", "source_run_id"],
    )
    write_csv(
        OUTPUT_DIR / "phase2_prescan_review_recovery_candidates.csv",
        review_recovery_rows,
        ["batch", "scenario_id", "model_name", "helper_status", "review_reason", "candidate_recovery_type", "evidence", "safe_to_recover_candidate"],
    )
    write_csv(
        OUTPUT_DIR / "phase2_prescan_duplicate_field_candidates.csv",
        duplicate_rows,
        ["batch", "scenario_id", "model_name", "helper_status", "block_index", "field_name", "duplicate_count", "raw_values", "reduced_values_if_available", "duplicate_type"],
    )
    write_csv(
        OUTPUT_DIR / "phase2_prescan_gold_data_issues.csv",
        gold_issues,
        ["scenario_id", "field_name", "expected_value_num", "tolerance", "tolerance_mode", "field_index", "issue"],
    )
    write_csv(
        OUTPUT_DIR / "phase2_prescan_tolerance_modes.csv",
        tolerance_rows,
        ["scenario_id", "field_name", "expected_value_num", "tolerance", "tolerance_mode", "field_index"],
    )
    write_csv(
        OUTPUT_DIR / "phase2_prescan_bertscore_final_block_removal_mismatches.csv",
        bert_mismatches,
        [
            "batch",
            "scenario_id",
            "model_name",
            "source_run_id",
            "bertscore_final_block_removed_candidate",
            "extractor_helper_status",
            "extractor_block_found",
            "likely_reason_bertscore_removal_failed",
            "recommended_fix",
        ],
    )

    extra_prescan = {
        "explicit_base_log_candidates": explicit_log_rows,
        "percent_ellipsis_risks": percent_ellipsis_rows,
        "review_autograder_version_skew_risks": risks,
        "fail_error_tag_distribution": dict(fail_tag_counts),
    }
    (OUTPUT_DIR / "phase2_prescan_additional_findings.json").write_text(json.dumps(extra_prescan, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    grades = Counter(row.get("deterministic_grade") for row in clean_rows)
    review_statuses = Counter(row.get("review_status") for row in load_review_all())
    output_files = [
        "PHASE2_PRESCAN_REPORT.md",
        "phase2_prescan_fail_error_tags.csv",
        "phase2_prescan_fail_to_not_gradeable_candidates.csv",
        "phase2_prescan_review_recovery_candidates.csv",
        "phase2_prescan_duplicate_field_candidates.csv",
        "phase2_prescan_gold_data_issues.csv",
        "phase2_prescan_tolerance_modes.csv",
        "phase2_prescan_bertscore_final_block_removal_mismatches.csv",
        "phase2_prescan_manifest.json",
        "phase2_prescan_additional_findings.json",
    ]
    manifest = {
        "created_at": utc_now(),
        "script": "scripts/prescan_phase2_impact.py",
        "read_only": True,
        "learning_db_modified": False,
        "raw_outputs_modified": False,
        "external_api_calls": False,
        "bertscore_run": False,
        "phase2_semantics_implemented": False,
        "input_folders": [
            "outputs/structured_prompt_pilot_v2/",
            "outputs/structured_prompt_pilot_v3/",
            "outputs/structured_prompt_pilot_v4/",
            "outputs/structured_prompt_pilot_v5/",
            str(SUMMARY_DIR.relative_to(ROOT)) + "/",
            str(BERT_NO_FINAL_DIR.relative_to(ROOT)) + "/",
        ],
        "output_files": output_files,
        "total_structured_runs": sum(review_statuses.values()),
        "total_clean_rows": review_statuses.get("CLEAN", 0),
        "total_review_rows": review_statuses.get("REVIEW", 0),
        "pass_count": grades.get("PASS", 0),
        "fail_count": grades.get("FAIL", 0),
        "fail_error_tag_distribution": dict(fail_tag_counts),
        "predicted_not_gradeable_count": len(not_gradeable_rows),
        "predicted_fail_count_after_phase2": EXPECTED_FAIL - len(not_gradeable_rows),
        "predicted_pass_count_after_phase2": EXPECTED_PASS,
        "predicted_gradeable_denominator": EXPECTED_PASS + EXPECTED_FAIL - len(not_gradeable_rows),
        "predicted_phase2_pass_rate_if_only_NOT_GRADEABLE_semantics_change": EXPECTED_PASS / (EXPECTED_PASS + EXPECTED_FAIL - len(not_gradeable_rows)),
        "explicit_base_log_candidates": len(explicit_log_rows),
        "review_recovery_candidates_safe": sum(1 for row in review_recovery_rows if row["safe_to_recover_candidate"]),
        "duplicate_field_candidates": len(duplicate_rows),
        "gold_data_issues": len(gold_issues),
        "percent_ellipsis_risks": len(percent_ellipsis_rows),
        "bertscore_block_removal_mismatches": len(bert_mismatches),
        "counts_reconciled": {
            "total_structured_runs": sum(review_statuses.values()) == EXPECTED_TOTAL_RUNS,
            "CLEAN": review_statuses.get("CLEAN", 0) == EXPECTED_CLEAN,
            "REVIEW": review_statuses.get("REVIEW", 0) == EXPECTED_REVIEW,
            "PASS": grades.get("PASS", 0) == EXPECTED_PASS,
            "FAIL": grades.get("FAIL", 0) == EXPECTED_FAIL,
            "scenario_count": len({row["scenario_id"] for row in clean_rows + review_rows}) == EXPECTED_SCENARIOS,
        },
    }
    (OUTPUT_DIR / "phase2_prescan_manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    write_report(
        clean_rows,
        review_rows,
        fail_tag_counts,
        not_gradeable_rows,
        explicit_log_rows,
        review_recovery_rows,
        duplicate_rows,
        gold_issues,
        percent_ellipsis_rows,
        bert_mismatches,
        risks,
        manifest,
    )

    print(f"output_dir={OUTPUT_DIR}")
    print(f"total_structured_runs={manifest['total_structured_runs']}")
    print(f"clean_rows={manifest['total_clean_rows']}")
    print(f"review_rows={manifest['total_review_rows']}")
    print(f"pass_count={manifest['pass_count']}")
    print(f"fail_count={manifest['fail_count']}")
    print(f"predicted_not_gradeable_count={manifest['predicted_not_gradeable_count']}")
    print(f"predicted_phase2_pass_rate_if_only_NOT_GRADEABLE_semantics_change={manifest['predicted_phase2_pass_rate_if_only_NOT_GRADEABLE_semantics_change']:.6f}")
    print(f"explicit_base_log_candidates={manifest['explicit_base_log_candidates']}")
    print(f"review_recovery_candidates_safe={manifest['review_recovery_candidates_safe']}")
    print(f"duplicate_field_candidates={manifest['duplicate_field_candidates']}")
    print(f"gold_data_issues={manifest['gold_data_issues']}")
    print(f"percent_ellipsis_risks={manifest['percent_ellipsis_risks']}")
    print(f"bertscore_block_removal_mismatches={manifest['bertscore_block_removal_mismatches']}")


def load_review_all() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for batch_num in (2, 3, 4, 5):
        for row in read_json(batch_dir(batch_num) / "review_layer_v1" / "review_layer_v1.json"):
            rows.append({**row, "batch": f"V{batch_num}"})
    return rows


if __name__ == "__main__":
    main()
