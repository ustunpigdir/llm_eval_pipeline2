#!/usr/bin/env python3
"""Build canonical reasoning-only text artifacts for future metric comparisons."""
from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from statistics import mean, median
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from extract_final_answers import select_final_block
from run_bertscore_structured_all32_phase1_hardened import parse_references

OUTPUT_DIR = ROOT / "outputs" / "metric_text_artifacts_v1"
METRIC_ANALYTICS_DIR = ROOT / "outputs" / "metric_comparison_analytics_v1"
FULL_BERT_DIR = ROOT / "outputs" / "bertscore_structured_all32_phase1_hardened_v1"
NO_FINAL_BERT_DIR = ROOT / "outputs" / "bertscore_structured_all32_phase1_hardened_no_final_block_v1"
REFERENCE_DIR = Path("/Users/upigdir/Desktop/Pipeline/Scenarios to Run")
SUMMARY_DIR = ROOT / "outputs" / "structured_prompt_all32_summary_phase1_hardened"

EXPECTED_ROWS = 252
EXPECTED_PASS = 117
EXPECTED_FAIL = 135
EXPECTED_SCENARIOS = 32
EXPECTED_MODELS = 8


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def batch_dir(batch: str) -> Path:
    return ROOT / "outputs" / f"structured_prompt_pilot_v{batch[1:]}"


def load_runs() -> dict[str, dict[str, Any]]:
    runs: dict[str, dict[str, Any]] = {}
    for batch in ("V2", "V3", "V4", "V5"):
        path = batch_dir(batch) / f"structured_prompt_pilot_v{batch[1:]}_runs.json"
        for row in read_json(path):
            runs[str(row["run_id"])] = row
    return runs


def unique_by_run_id(rows: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    out: dict[str, dict[str, str]] = {}
    for row in rows:
        run_id = row["source_run_id"]
        if run_id in out:
            raise SystemExit(f"Duplicate source_run_id in BERTScore CSV: {run_id}")
        out[run_id] = row
    return out


def remove_span(text: str, start: int, end: int) -> str:
    return (text[:start].rstrip() + "\n" + text[end:].lstrip()).strip()


def reference_contains_final_marker(text: str) -> bool:
    return bool(re.search(r"final\s+answer", text or "", re.IGNORECASE))


def reference_contains_aligned_block(text: str) -> bool:
    return "\\begin{aligned}" in (text or "") and "\\end{aligned}" in (text or "")


def build_reference_validation(references: dict[str, str], categories: dict[str, str]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for scenario_id in sorted(references):
        text = references[scenario_id]
        contains_marker = reference_contains_final_marker(text)
        contains_block = reference_contains_aligned_block(text)
        warning = []
        if contains_marker:
            warning.append("contains_final_answer_marker")
        if contains_block:
            warning.append("contains_aligned_block")
        rows.append(
            {
                "scenario_id": scenario_id,
                "category": categories.get(scenario_id, ""),
                "reference_source": "worked_solutions_batch1.md through worked_solutions_batch7.md",
                "reference_resolution_status": "OK",
                "reference_reasoning_text_length_chars": len(text),
                "reference_reasoning_text_sha256": sha256_text(text),
                "reference_contains_final_answer_marker": contains_marker,
                "reference_contains_aligned_final_block": contains_block,
                "warning": ";".join(warning),
            }
        )
    return rows


def build_dataset() -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]], dict[str, Any]]:
    base_rows = read_csv(METRIC_ANALYTICS_DIR / "metric_comparison_base_dataset.csv")
    runs = load_runs()
    references, _ = parse_references(REFERENCE_DIR)
    full_bert = unique_by_run_id(read_csv(FULL_BERT_DIR / "bertscore_structured_all32_phase1_hardened.csv"))
    no_final_bert = unique_by_run_id(read_csv(NO_FINAL_BERT_DIR / "bertscore_structured_all32_phase1_hardened_no_final_block.csv"))
    categories = {row["scenario_id"]: row["category"] for row in base_rows}

    dataset: list[dict[str, Any]] = []
    span_validation: list[dict[str, Any]] = []
    failures: list[dict[str, Any]] = []
    text_hashes: list[dict[str, Any]] = []

    for base in base_rows:
        run_id = base["source_run_id"]
        run = runs.get(run_id)
        if not run:
            raise SystemExit(f"Missing raw run for {run_id}")
        candidate_full = run.get("response") or ""
        final_block, block_status = select_final_block(candidate_full)
        extractor_found = final_block is not None
        if extractor_found:
            start = int(final_block["start_char"])
            end = int(final_block["end_char"])
            candidate_reasoning = remove_span(candidate_full, start, end)
            warning = ""
        else:
            start = end = ""
            candidate_reasoning = candidate_full
            warning = f"extractor_no_final_block_status={block_status}"
            failures.append(
                {
                    "source_run_id": run_id,
                    "batch": base["batch"],
                    "scenario_id": base["scenario_id"],
                    "model_name": base["model_name"],
                    "extractor_final_block_status": block_status,
                    "final_block_removal_warning": warning,
                }
            )
        reference_text = references.get(base["scenario_id"], "")
        reference_status = "OK" if reference_text else "MISSING"
        full = full_bert.get(run_id, {})
        no_final = no_final_bert.get(run_id, {})
        bert_removed = no_final.get("final_block_removed_candidate", "")
        bert_removed_bool = str(bert_removed).lower() == "true"
        removal_agrees = bool(extractor_found) == bert_removed_bool
        likely_reason = ""
        if not removal_agrees and extractor_found and not bert_removed_bool:
            likely_reason = "bertscore_v1_regex_failed_but_extractor_span_found_block"
        elif not removal_agrees:
            likely_reason = "extractor_and_bertscore_v1_disagree"
        candidate_removed_chars = len(candidate_full) - len(candidate_reasoning)
        row = {
            "row_key": base["row_key"],
            "source_run_id": run_id,
            "batch": base["batch"],
            "scenario_id": base["scenario_id"],
            "category": base["category"],
            "model_name": base["model_name"],
            "deterministic_grade": base["deterministic_grade"],
            "deterministic_pass_binary": base["deterministic_pass_binary"],
            "extraction_status": base["extraction_status"],
            "helper_status": base["helper_status"],
            "review_status": base["review_status"],
            "error_tags": base["error_tags"],
            "failed_fields": base["failed_fields"],
            "candidate_full_text": candidate_full,
            "candidate_reasoning_text": candidate_reasoning,
            "candidate_full_text_length_chars": len(candidate_full),
            "candidate_reasoning_text_length_chars": len(candidate_reasoning),
            "candidate_removed_chars": candidate_removed_chars,
            "candidate_full_text_sha256": sha256_text(candidate_full),
            "candidate_reasoning_text_sha256": sha256_text(candidate_reasoning),
            "extractor_final_block_found": extractor_found,
            "extractor_final_block_start_char": start,
            "extractor_final_block_end_char": end,
            "extractor_final_block_length_chars": (int(end) - int(start)) if extractor_found else "",
            "extractor_final_block_status": block_status,
            "final_block_removed_by_extractor_span": extractor_found,
            "final_block_removal_warning": warning,
            "reference_reasoning_text": reference_text,
            "reference_reasoning_text_length_chars": len(reference_text),
            "reference_reasoning_text_sha256": sha256_text(reference_text),
            "reference_source": "worked_solutions_batch1.md through worked_solutions_batch7.md",
            "reference_resolution_status": reference_status,
            "bertscore_full_f1": full.get("bert_f1", ""),
            "bertscore_no_final_f1": no_final.get("bert_f1", ""),
            "bertscore_no_final_v1_removed_candidate": bert_removed,
            "bertscore_no_final_v1_candidate_removed_chars": no_final.get("candidate_removed_chars", ""),
            "bertscore_no_final_v1_removal_agrees_with_extractor_span": removal_agrees,
        }
        dataset.append(row)
        span_validation.append(
            {
                "source_run_id": run_id,
                "batch": base["batch"],
                "scenario_id": base["scenario_id"],
                "model_name": base["model_name"],
                "extractor_found_block": extractor_found,
                "extractor_start_char": start,
                "extractor_end_char": end,
                "extractor_removed_chars": candidate_removed_chars,
                "bertscore_v1_removed_candidate": bert_removed,
                "bertscore_v1_removed_chars": no_final.get("candidate_removed_chars", ""),
                "removal_agrees": removal_agrees,
                "likely_reason_for_disagreement": likely_reason,
            }
        )
        text_hashes.append(
            {
                "source_run_id": run_id,
                "candidate_full_text_sha256": row["candidate_full_text_sha256"],
                "candidate_reasoning_text_sha256": row["candidate_reasoning_text_sha256"],
                "reference_reasoning_text_sha256": row["reference_reasoning_text_sha256"],
            }
        )

    reference_validation = build_reference_validation(references, categories)
    diagnostics = {
        "references": references,
        "reference_validation": reference_validation,
    }
    return dataset, span_validation, failures, reference_validation, text_hashes, diagnostics


def write_readme(output_files: list[str]) -> None:
    lines = [
        "# Metric Text Artifacts v1",
        "",
        "This folder contains the canonical text-bearing input layer for future non-correctness metric comparisons.",
        "",
        "It differs from BERTScore outputs by storing the actual candidate full text, extractor-span reasoning-only text, and reference reasoning text, plus hashes and span metadata.",
        "",
        "It does not change grading, compute correctness, rerun models, call APIs, modify raw outputs, or modify `learning.db`.",
        "",
        "Future metrics should use `canonical_reasoning_text_dataset.csv` or `.json` and verify text hashes via `text_hashes.csv`.",
        "",
        "Candidate reasoning text is derived only by removing the extractor-selected final-answer aligned block span from the saved raw model answer.",
        "",
        "Rerun with:",
        "",
        "```bash",
        ".venv/bin/python scripts/build_metric_text_artifacts_v1.py",
        "```",
        "",
        "Files:",
    ]
    lines.extend(f"- `{name}`" for name in output_files)
    (OUTPUT_DIR / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_report(dataset: list[dict[str, Any]], span_validation: list[dict[str, Any]], failures: list[dict[str, Any]], reference_validation: list[dict[str, Any]], manifest: dict[str, Any]) -> None:
    grades = Counter(row["deterministic_grade"] for row in dataset)
    full_lengths = [int(row["candidate_full_text_length_chars"]) for row in dataset]
    reasoning_lengths = [int(row["candidate_reasoning_text_length_chars"]) for row in dataset]
    ref_lengths = [int(row["reference_reasoning_text_length_chars"]) for row in dataset]
    disagreements = [row for row in span_validation if not row["removal_agrees"]]
    lines = [
        "# Canonical Reasoning Text Report",
        "",
        "## Purpose",
        "",
        "Create a canonical text-bearing artifact for future non-correctness text metrics.",
        "",
        "## Inputs Used",
        "",
        "- Structured prompt V2-V5 saved raw outputs",
        "- Metric comparison analytics v1 base dataset",
        "- Existing BERTScore full/no-final outputs for alignment metadata",
        "- Existing BERTScore reference parser over worked solution Markdown files",
        "",
        "## Row Counts",
        "",
        f"- Rows: {len(dataset)}",
        f"- Scenarios: {len({row['scenario_id'] for row in dataset})}",
        f"- Models: {len({row['model_name'] for row in dataset})}",
        f"- Batches: {', '.join(sorted({row['batch'] for row in dataset}))}",
        "",
        "## PASS/FAIL Distribution",
        "",
        f"- PASS: {grades['PASS']}",
        f"- FAIL: {grades['FAIL']}",
        "",
        "## Final-Answer Block Removal Result",
        "",
        f"- Extractor span removal success: {manifest['extractor_span_removal_success_count']}",
        f"- Extractor span removal failure: {manifest['extractor_span_removal_failure_count']}",
        "",
        "## Comparison To BERTScore No-Final v1 Removal",
        "",
        f"- Disagreements: {len(disagreements)}",
        "- The disagreements are expected to be the 5 rows where BERTScore v1 regex removal missed a block but extractor-span removal succeeds.",
        "",
        "## Reference Text Validation",
        "",
        f"- References resolved: {manifest['references_resolved']}/{manifest['reference_count']}",
        f"- References with final-answer marker warning: {sum(1 for row in reference_validation if row['reference_contains_final_answer_marker'])}",
        f"- References with aligned final block warning: {sum(1 for row in reference_validation if row['reference_contains_aligned_final_block'])}",
        "",
        "## Text Length Summary",
        "",
        f"- Candidate full text mean/median chars: {mean(full_lengths):.1f} / {median(full_lengths):.1f}",
        f"- Candidate reasoning text mean/median chars: {mean(reasoning_lengths):.1f} / {median(reasoning_lengths):.1f}",
        f"- Reference reasoning text mean/median chars: {mean(ref_lengths):.1f} / {median(ref_lengths):.1f}",
        "",
        "## Hashing And Reproducibility",
        "",
        "Every row stores SHA-256 hashes for candidate full text, candidate reasoning text, and reference reasoning text.",
        "",
        "## Known Limitations",
        "",
        "- Candidate reasoning text removes the extractor-selected aligned block span, not surrounding heading text.",
        "- This artifact carries text for metric computation but does not decide correctness.",
        "- Reference text follows the existing BERTScore reference extraction logic.",
        "",
        "## Recommended Next Metrics",
        "",
        "- ROUGE-L and chrF from `candidate_reasoning_text` vs `reference_reasoning_text`.",
        "- Re-run BERTScore from this artifact if final-block removal needs to be fully canonical.",
        "- Add ROSCOE/NLI only after this text layer is treated as the frozen source.",
    ]
    (OUTPUT_DIR / "CANONICAL_REASONING_TEXT_REPORT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    dataset, span_validation, failures, reference_validation, text_hashes, _ = build_dataset()
    grades = Counter(row["deterministic_grade"] for row in dataset)
    success_count = sum(1 for row in dataset if row["final_block_removed_by_extractor_span"])
    failure_count = len(dataset) - success_count
    references_resolved = sum(1 for row in reference_validation if row["reference_resolution_status"] == "OK")

    if len(dataset) != EXPECTED_ROWS:
        raise SystemExit(f"Expected {EXPECTED_ROWS} rows, found {len(dataset)}")
    if grades["PASS"] != EXPECTED_PASS or grades["FAIL"] != EXPECTED_FAIL:
        raise SystemExit(f"Unexpected PASS/FAIL counts: {dict(grades)}")
    if len({row["scenario_id"] for row in dataset}) != EXPECTED_SCENARIOS:
        raise SystemExit("Expected 32 scenarios")
    if len({row["model_name"] for row in dataset}) != EXPECTED_MODELS:
        raise SystemExit("Expected 8 models")
    if any(row["review_status"] != "CLEAN" for row in dataset):
        raise SystemExit("Unexpected REVIEW row included")

    dataset_fields = [
        "row_key",
        "source_run_id",
        "batch",
        "scenario_id",
        "category",
        "model_name",
        "deterministic_grade",
        "deterministic_pass_binary",
        "extraction_status",
        "helper_status",
        "review_status",
        "error_tags",
        "failed_fields",
        "candidate_full_text",
        "candidate_reasoning_text",
        "candidate_full_text_length_chars",
        "candidate_reasoning_text_length_chars",
        "candidate_removed_chars",
        "candidate_full_text_sha256",
        "candidate_reasoning_text_sha256",
        "extractor_final_block_found",
        "extractor_final_block_start_char",
        "extractor_final_block_end_char",
        "extractor_final_block_length_chars",
        "extractor_final_block_status",
        "final_block_removed_by_extractor_span",
        "final_block_removal_warning",
        "reference_reasoning_text",
        "reference_reasoning_text_length_chars",
        "reference_reasoning_text_sha256",
        "reference_source",
        "reference_resolution_status",
        "bertscore_full_f1",
        "bertscore_no_final_f1",
        "bertscore_no_final_v1_removed_candidate",
        "bertscore_no_final_v1_candidate_removed_chars",
        "bertscore_no_final_v1_removal_agrees_with_extractor_span",
    ]
    write_csv(OUTPUT_DIR / "canonical_reasoning_text_dataset.csv", dataset, dataset_fields)
    (OUTPUT_DIR / "canonical_reasoning_text_dataset.json").write_text(json.dumps(dataset, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    write_csv(
        OUTPUT_DIR / "final_block_span_validation.csv",
        span_validation,
        [
            "source_run_id",
            "batch",
            "scenario_id",
            "model_name",
            "extractor_found_block",
            "extractor_start_char",
            "extractor_end_char",
            "extractor_removed_chars",
            "bertscore_v1_removed_candidate",
            "bertscore_v1_removed_chars",
            "removal_agrees",
            "likely_reason_for_disagreement",
        ],
    )
    write_csv(
        OUTPUT_DIR / "final_block_removal_failures.csv",
        failures,
        ["source_run_id", "batch", "scenario_id", "model_name", "extractor_final_block_status", "final_block_removal_warning"],
    )
    write_csv(
        OUTPUT_DIR / "reference_text_validation.csv",
        reference_validation,
        [
            "scenario_id",
            "category",
            "reference_source",
            "reference_resolution_status",
            "reference_reasoning_text_length_chars",
            "reference_reasoning_text_sha256",
            "reference_contains_final_answer_marker",
            "reference_contains_aligned_final_block",
            "warning",
        ],
    )
    write_csv(
        OUTPUT_DIR / "text_hashes.csv",
        text_hashes,
        ["source_run_id", "candidate_full_text_sha256", "candidate_reasoning_text_sha256", "reference_reasoning_text_sha256"],
    )

    output_files = [
        "README.md",
        "CANONICAL_REASONING_TEXT_REPORT.md",
        "canonical_reasoning_text_dataset.csv",
        "canonical_reasoning_text_dataset.json",
        "canonical_reasoning_text_manifest.json",
        "final_block_span_validation.csv",
        "final_block_removal_failures.csv",
        "reference_text_validation.csv",
        "text_hashes.csv",
    ]
    manifest = {
        "artifact_name": "metric_text_artifacts_v1",
        "created_at": utc_now(),
        "purpose": "canonical reasoning-only text source for future metric comparison",
        "read_only": True,
        "learning_db_modified": False,
        "raw_outputs_modified": False,
        "model_calls_made": False,
        "external_llm_api_calls": False,
        "phase2_semantics_implemented": False,
        "metrics_computed": False,
        "expected_rows": EXPECTED_ROWS,
        "actual_rows": len(dataset),
        "pass_count": grades["PASS"],
        "fail_count": grades["FAIL"],
        "review_rows_included": sum(1 for row in dataset if row["review_status"] != "CLEAN"),
        "extractor_span_removal_success_count": success_count,
        "extractor_span_removal_failure_count": failure_count,
        "bertscore_v1_removal_disagreement_count": sum(1 for row in span_validation if not row["removal_agrees"]),
        "reference_count": EXPECTED_SCENARIOS,
        "references_resolved": references_resolved,
        "input_folders": [
            "outputs/structured_prompt_pilot_v2/",
            "outputs/structured_prompt_pilot_v3/",
            "outputs/structured_prompt_pilot_v4/",
            "outputs/structured_prompt_pilot_v5/",
            str(SUMMARY_DIR.relative_to(ROOT)) + "/",
            str(METRIC_ANALYTICS_DIR.relative_to(ROOT)) + "/",
            str(FULL_BERT_DIR.relative_to(ROOT)) + "/",
            str(NO_FINAL_BERT_DIR.relative_to(ROOT)) + "/",
        ],
        "output_files": output_files,
    }
    (OUTPUT_DIR / "canonical_reasoning_text_manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    write_readme(output_files)
    write_report(dataset, span_validation, failures, reference_validation, manifest)

    print(f"output_dir={OUTPUT_DIR}")
    print(f"row_count={len(dataset)}")
    print(f"pass_count={grades['PASS']}")
    print(f"fail_count={grades['FAIL']}")
    print(f"scenario_count={len({row['scenario_id'] for row in dataset})}")
    print(f"model_count={len({row['model_name'] for row in dataset})}")
    print(f"extractor_span_removal_success_count={success_count}")
    print(f"extractor_span_removal_failure_count={failure_count}")
    print(f"bertscore_v1_removal_disagreement_count={manifest['bertscore_v1_removal_disagreement_count']}")
    print(f"references_resolved={references_resolved}")


if __name__ == "__main__":
    main()
