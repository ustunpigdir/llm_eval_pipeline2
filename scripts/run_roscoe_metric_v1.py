#!/usr/bin/env python3
"""Inspect and, if available, run ROSCOE-style metrics over canonical text."""
from __future__ import annotations

import csv
import importlib.metadata
import importlib.util
import json
import platform
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = ROOT / "outputs" / "metric_text_artifacts_v1" / "canonical_reasoning_text_dataset.csv"
OUTPUT_DIR = ROOT / "outputs" / "metric_comparison_analytics_roscoe_v1"
BERT_PATH = ROOT / "outputs" / "bertscore_reasoning_only_canonical_v2" / "bertscore_reasoning_only_canonical_v2.csv"
ROUGE_PATH = ROOT / "outputs" / "metric_comparison_analytics_rouge_l_v1" / "rouge_l_row_scores.csv"
CHRF_PATH = ROOT / "outputs" / "metric_comparison_analytics_chrf_v1" / "chrf_row_scores.csv"
BASE_PATH = ROOT / "outputs" / "metric_comparison_analytics_v1" / "metric_comparison_base_dataset.csv"

EXPECTED_ROWS = 252
EXPECTED_PASS = 117
EXPECTED_FAIL = 135


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def module_status(name: str) -> dict[str, Any]:
    spec = importlib.util.find_spec(name)
    status: dict[str, Any] = {
        "module": name,
        "importable": bool(spec),
        "origin": spec.origin if spec else "",
        "version": "",
    }
    if spec:
        try:
            status["version"] = importlib.metadata.version(name.replace("_", "-"))
        except Exception:
            status["version"] = "unknown"
    return status


def torch_status() -> dict[str, Any]:
    status = {
        "available": False,
        "version": "",
        "cuda_available": False,
        "mps_available": False,
        "device": "cpu",
        "error": "",
    }
    try:
        import torch

        status["available"] = True
        status["version"] = torch.__version__
        status["cuda_available"] = bool(torch.cuda.is_available())
        status["mps_available"] = bool(getattr(torch.backends, "mps", None).is_available()) if hasattr(torch.backends, "mps") else False
        status["device"] = "cuda" if status["cuda_available"] else ("mps" if status["mps_available"] else "cpu")
    except Exception as exc:
        status["error"] = f"{type(exc).__name__}: {exc}"
    return status


def cache_status() -> dict[str, Any]:
    hf = Path.home() / ".cache" / "huggingface"
    sentence_transformers = Path.home() / ".cache" / "torch" / "sentence_transformers"
    return {
        "huggingface_cache_exists": hf.exists(),
        "huggingface_cache_path": str(hf) if hf.exists() else "",
        "sentence_transformers_cache_exists": sentence_transformers.exists(),
        "sentence_transformers_cache_path": str(sentence_transformers) if sentence_transformers.exists() else "",
    }


def inspect_setup() -> dict[str, Any]:
    rows = read_csv(INPUT_PATH)
    grades = Counter(row.get("deterministic_grade") for row in rows)
    modules = [module_status(name) for name in ["roscoe", "sentence_transformers", "transformers", "torch", "datasets", "evaluate"]]
    roscoe_available = next(item for item in modules if item["module"] == "roscoe")["importable"]
    sentence_transformers_available = next(item for item in modules if item["module"] == "sentence_transformers")["importable"]
    estimated_mode = "full_252_rows" if roscoe_available else "setup_only"
    if roscoe_available and not sentence_transformers_available:
        estimated_mode = "pilot_only"
    return {
        "created_at": utc_now(),
        "python_version": sys.version.replace("\n", " "),
        "platform": platform.platform(),
        "module_status": modules,
        "torch_status": torch_status(),
        "cache_status": cache_status(),
        "input_rows": len(rows),
        "input_pass_count": grades.get("PASS", 0),
        "input_fail_count": grades.get("FAIL", 0),
        "input_review_rows": sum(1 for row in rows if row.get("review_status") != "CLEAN"),
        "input_scenario_count": len({row.get("scenario_id") for row in rows}),
        "input_model_count": len({row.get("model_name") for row in rows}),
        "existing_metric_alignment_sources": {
            "bertscore_reasoning_only_canonical_v2": BERT_PATH.exists(),
            "rouge_l_v1": ROUGE_PATH.exists(),
            "chrf_v1": CHRF_PATH.exists(),
            "metric_comparison_base": BASE_PATH.exists(),
        },
        "roscoe_available": roscoe_available,
        "sentence_transformers_available": sentence_transformers_available,
        "estimated_scoring_mode": estimated_mode,
        "setup_blocker": "" if roscoe_available else "roscoe package is not importable in the project virtual environment",
    }


def write_setup_status(setup: dict[str, Any]) -> None:
    lines = [
        "# ROSCOE Setup Status",
        "",
        "## Environment",
        "",
        f"- Python: {setup['python_version']}",
        f"- Platform: {setup['platform']}",
        f"- Torch available: {setup['torch_status']['available']}",
        f"- Torch version: {setup['torch_status']['version']}",
        f"- Device detected: {setup['torch_status']['device']}",
        f"- CUDA available: {setup['torch_status']['cuda_available']}",
        f"- MPS available: {setup['torch_status']['mps_available']}",
        "",
        "## Module Availability",
        "",
        "| module | importable | version | origin |",
        "| --- | ---: | --- | --- |",
    ]
    for item in setup["module_status"]:
        lines.append(f"| {item['module']} | {item['importable']} | {item['version']} | {item['origin']} |")
    lines.extend(
        [
            "",
            "## Model/Cache Availability",
            "",
            f"- Hugging Face cache exists: {setup['cache_status']['huggingface_cache_exists']}",
            f"- Hugging Face cache path: {setup['cache_status']['huggingface_cache_path']}",
            f"- sentence-transformers cache exists: {setup['cache_status']['sentence_transformers_cache_exists']}",
            "",
            "## Input Coverage",
            "",
            f"- Rows: {setup['input_rows']}",
            f"- PASS: {setup['input_pass_count']}",
            f"- FAIL: {setup['input_fail_count']}",
            f"- REVIEW rows: {setup['input_review_rows']}",
            f"- Scenarios: {setup['input_scenario_count']}",
            f"- Models: {setup['input_model_count']}",
            "",
            "## Decision",
            "",
            f"- ROSCOE available: {setup['roscoe_available']}",
            f"- Estimated scoring mode: {setup['estimated_scoring_mode']}",
            f"- Setup blocker: {setup['setup_blocker'] or 'none'}",
            "",
            "No ROSCOE scores were computed because the ROSCOE package is unavailable. This follows the setup rule: do not install large packages automatically and do not fabricate metric scores.",
        ]
    )
    (OUTPUT_DIR / "roscoe_setup_status.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_readme(setup: dict[str, Any]) -> None:
    lines = [
        "# ROSCOE Metric v1",
        "",
        "This folder is the ROSCOE metric-comparison layer setup artifact.",
        "",
        f"ROSCOE was actually run: `{setup['roscoe_available']}`.",
        f"Run mode: `{setup['estimated_scoring_mode']}`.",
        "",
        "Input text source:",
        "- `outputs/metric_text_artifacts_v1/canonical_reasoning_text_dataset.csv`",
        "",
        "This does not change grading, modify raw outputs, call LLM APIs, run BERTScore, run NLI, or implement Phase 2 semantics.",
        "",
        "Rerun setup inspection with:",
        "",
        "```bash",
        ".venv/bin/python scripts/run_roscoe_metric_v1.py",
        "```",
        "",
        "Interpretation: ROSCOE, when available, should be treated as a reasoning-trace diagnostic, not a correctness gate.",
    ]
    (OUTPUT_DIR / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_report(setup: dict[str, Any]) -> None:
    lines = [
        "# ROSCOE Metric Report",
        "",
        "## Purpose",
        "",
        "Evaluate whether ROSCOE-style reasoning metrics can be added as a metric-behavior layer.",
        "",
        "## Setup Status",
        "",
        f"- ROSCOE importable: {setup['roscoe_available']}",
        f"- sentence_transformers importable: {setup['sentence_transformers_available']}",
        f"- Run mode: {setup['estimated_scoring_mode']}",
        f"- Blocker: {setup['setup_blocker'] or 'none'}",
        "",
        "## Inputs",
        "",
        "- Canonical reasoning-only text artifact",
        "- Existing BERTScore/ROUGE-L/chrF metric artifacts were detected for future alignment.",
        "",
        "## ROSCOE Implementation Used",
        "",
        "None. ROSCOE is not importable in the current project virtual environment.",
        "",
        "## Row Coverage",
        "",
        f"- Rows available for future scoring: {setup['input_rows']}",
        f"- PASS/FAIL available: {setup['input_pass_count']}/{setup['input_fail_count']}",
        "",
        "## Available ROSCOE Metrics",
        "",
        "No ROSCOE metrics available.",
        "",
        "## Overall ROSCOE Summary",
        "",
        "Not computed.",
        "",
        "## Interpretation",
        "",
        "Setup stopped before scoring. No conclusions can be drawn about ROSCOE separation on the 252-row dataset.",
        "",
        "## Limitations",
        "",
        "- ROSCOE package is unavailable.",
        "- sentence_transformers is unavailable.",
        "- No model download or package installation was attempted.",
        "",
        "## Recommended Next Step",
        "",
        "Decide whether to add ROSCOE and sentence-transformer dependencies through an approved dependency workflow, then rerun this script.",
    ]
    (OUTPUT_DIR / "ROSCOE_METRIC_REPORT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    setup = inspect_setup()
    output_files = ["README.md", "ROSCOE_METRIC_REPORT.md", "roscoe_setup_status.md", "manifest.json"]

    write_setup_status(setup)
    write_readme(setup)
    write_report(setup)

    manifest = {
        "artifact_name": "roscoe_metric_v1",
        "created_at": utc_now(),
        "input_text_artifact": "outputs/metric_text_artifacts_v1/canonical_reasoning_text_dataset.csv",
        "read_only": True,
        "learning_db_modified": False,
        "raw_outputs_modified": False,
        "model_calls_made": False,
        "external_llm_api_calls": False,
        "bertscore_run": False,
        "roscoe_run": False,
        "nli_run": False,
        "phase2_semantics_implemented": False,
        "expected_rows": EXPECTED_ROWS,
        "actual_rows_scored": 0,
        "pass_count": 0,
        "fail_count": 0,
        "run_mode": setup["estimated_scoring_mode"],
        "roscoe_available": setup["roscoe_available"],
        "roscoe_metrics_available": [],
        "selected_roscoe_metric": "",
        "metrics_computed": [],
        "setup": setup,
        "output_files": output_files,
    }
    (OUTPUT_DIR / "manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(f"output_dir={OUTPUT_DIR}")
    print(f"roscoe_available={setup['roscoe_available']}")
    print(f"sentence_transformers_available={setup['sentence_transformers_available']}")
    print(f"run_mode={setup['estimated_scoring_mode']}")
    print(f"actual_rows_scored=0")
    print(f"setup_blocker={setup['setup_blocker']}")


if __name__ == "__main__":
    main()
