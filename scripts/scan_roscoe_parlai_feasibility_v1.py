#!/usr/bin/env python3
"""Create a ParlAI-specific ROSCOE feasibility artifact.

This script performs metadata/source inspection only. It does not install ParlAI,
create a virtual environment, download models, or compute ROSCOE scores.
"""

from __future__ import annotations

import csv
import datetime as dt
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import sys
from typing import Any
from urllib.error import URLError
from urllib.request import urlopen


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "outputs" / "metric_comparison_analytics_roscoe_parlai_feasibility_v1"
REPO = "facebookresearch/ParlAI"
BRANCH = "main"
TREE_URL = f"https://api.github.com/repos/{REPO}/git/trees/{BRANCH}?recursive=1"
RAW_BASE = f"https://raw.githubusercontent.com/{REPO}/{BRANCH}/"

SEARCH_TERMS = [
    "roscoe",
    "reasoning evaluation",
    "semantic alignment",
    "semantic similarity",
    "logical inference",
    "language coherence",
    "coherence metrics",
    "rationale evaluation",
    "step-by-step reasoning",
]

KEY_PATHS = [
    "projects/roscoe/README.md",
    "projects/roscoe/score.py",
    "projects/roscoe/roscoe.py",
    "projects/roscoe/utils.py",
    "projects/roscoe/baselines/constants.py",
    "projects/roscoe/baselines/requirements.txt",
    "projects/roscoe/baselines/run.py",
    "projects/roscoe/baselines/scores.py",
    "projects/roscoe/meta_evaluation/correlations.py",
    "projects/roscoe/meta_evaluation/roscoe_correlations.py",
    "projects/roscoe/meta_evaluation/roscoe_synthetic_correlations.py",
    "projects/roscoe/synthetic_evaluation/synthetic_roscoe.py",
    "parlai/tasks/reasoning/requirements.txt",
    "tests/nightly/cpu/test_roscoe.py",
    "setup.py",
]

PROTECTED_PATHS = [
    "learning.db",
    "outputs/structured_prompt_pilot_v2/structured_prompt_pilot_v2_runs.json",
    "outputs/structured_prompt_pilot_v3/structured_prompt_pilot_v3_runs.json",
    "outputs/structured_prompt_pilot_v4/structured_prompt_pilot_v4_runs.json",
    "outputs/structured_prompt_pilot_v5/structured_prompt_pilot_v5_runs.json",
    "outputs/metric_text_artifacts_v1/canonical_reasoning_text_dataset.csv",
]


def fetch_text(url: str) -> str:
    with urlopen(url, timeout=30) as response:
        return response.read().decode("utf-8", errors="replace")


def fetch_json(url: str) -> Any:
    return json.loads(fetch_text(url))


def module_installed(name: str) -> bool:
    return importlib.util.find_spec(name) is not None


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def protected_stats() -> dict[str, dict[str, int]]:
    stats: dict[str, dict[str, int]] = {}
    for rel in PROTECTED_PATHS:
        path = ROOT / rel
        if path.exists():
            st = path.stat()
            stats[rel] = {"mtime": int(st.st_mtime), "size": st.st_size}
    return stats


def relevant_paths_from_tree(tree: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows = []
    for item in tree:
        path = item.get("path", "")
        path_l = path.lower()
        if path.startswith("projects/roscoe/") or any(term in path_l for term in ["roscoe", "reasoning"]):
            rows.append(item)
    return rows


def analyze_source(path: str, text: str) -> dict[str, Any]:
    lower = text.lower()
    imports = sorted(set(re.findall(r"^(?:from|import)\s+([a-zA-Z0-9_\.]+)", text, flags=re.M)))
    functions = sorted(set(re.findall(r"^(?:class|def)\s+([A-Za-z_][A-Za-z0-9_]*)", text, flags=re.M)))
    metrics = sorted(set(re.findall(r'([A-Z_]+)\s*=\s*"([a-zA-Z0-9_]+)"', text)))
    return {
        "path": path,
        "sha256": sha256_text(text),
        "imports": imports,
        "functions_or_classes": functions,
        "metric_constants": [name for _constant, name in metrics],
        "contains_metric_logic": any(
            token in lower
            for token in [
                "reasoning_alignment",
                "faithfulness",
                "semantic_coverage",
                "missing_step",
                "coherence_step_vs_step",
                "perplexity",
            ]
        ),
        "contains_entrypoint": "__main__" in text or "ParlaiParser" in text,
        "contains_dependency_imports": any(
            dep in lower
            for dep in ["sentence_transformers", "simcse", "transformers", "torch", "nltk"]
        ),
        "contains_reference_based": "SUPERVISED_SCORES" in text or "references" in lower,
        "contains_reference_free": "UNSUPERVISED_SCORES" in text or "context" in lower,
    }


def write_csv(path: Path, rows: list[dict[str, Any]], fields: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fields})


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    before_stats = protected_stats()
    network_error = ""
    tree: list[dict[str, Any]] = []
    source_texts: dict[str, str] = {}

    try:
        tree_data = fetch_json(TREE_URL)
        tree = tree_data.get("tree", [])
    except (URLError, TimeoutError, OSError) as exc:
        network_error = repr(exc)

    for path in KEY_PATHS:
        if network_error:
            break
        try:
            source_texts[path] = fetch_text(RAW_BASE + path)
        except (URLError, TimeoutError, OSError) as exc:
            source_texts[path] = f"FETCH_ERROR: {exc!r}"

    analyses = {
        path: analyze_source(path, text)
        for path, text in source_texts.items()
        if not text.startswith("FETCH_ERROR:")
    }

    tree_relevant = relevant_paths_from_tree(tree)
    inventory_rows = []
    for item in tree_relevant:
        path = item.get("path", "")
        analysis = analyses.get(path, {})
        notes = []
        if path.startswith("projects/roscoe/"):
            notes.append("inside ParlAI ROSCOE project")
        if path in KEY_PATHS:
            notes.append("source fetched for inspection")
        if path == "projects/roscoe/score.py":
            notes.append("core Evaluator and metric constants")
        if path == "projects/roscoe/roscoe.py":
            notes.append("CLI dataset scoring wrapper")
        inventory_rows.append(
            {
                "source": f"https://github.com/{REPO}",
                "path": path,
                "file_type": item.get("type", ""),
                "size_bytes_if_known": item.get("size", ""),
                "reason_relevant": "path/name matches ROSCOE or reasoning",
                "contains_metric_logic": analysis.get("contains_metric_logic", ""),
                "contains_entrypoint": analysis.get("contains_entrypoint", ""),
                "contains_dependency_imports": analysis.get("contains_dependency_imports", ""),
                "notes": "; ".join(notes),
            }
        )

    entrypoint_rows = [
        {
            "path": "projects/roscoe/roscoe.py",
            "function_or_command": "python projects/roscoe/roscoe.py --dataset-path PATH --datasets NAME --scores ...",
            "purpose": "CLI for scoring ParlAI-format JSON prediction files.",
            "input_format_expected": "JSON lines with dataset-specific fields such as gpt-3, premise, hypothesis, explanation_1..3.",
            "output_format_expected": "TSV score files under output directory.",
            "can_score_candidate_reference_pair": "not directly; requires adapter to JSONL fields and step parsing",
            "reference_based": "yes for datasets with references, especially gsm8k/esnli paths",
            "reference_free": "yes",
            "notes": "Uses ParlaiParser and ReasoningEvaluator wrapper.",
        },
        {
            "path": "projects/roscoe/score.py",
            "function_or_command": "Evaluator(hypos=[Chain([...])], context=[Chain([...])], references=[Chain([...])]).evaluate(score_types=...)",
            "purpose": "Programmatic metric engine.",
            "input_format_expected": "Lists of Chain objects, each Chain containing reasoning steps.",
            "output_format_expected": "dict mapping metric name to list of numeric scores or N/A.",
            "can_score_candidate_reference_pair": "yes with a small local adapter and context selection",
            "reference_based": "yes via SUPERVISED_SCORES",
            "reference_free": "yes via UNSUPERVISED_SCORES",
            "notes": "Import is not minimal because sentence_transformers and simcse are imported eagerly.",
        },
        {
            "path": "tests/nightly/cpu/test_roscoe.py",
            "function_or_command": "unit tests for Evaluator internals",
            "purpose": "Smoke-test clues for non-scoring utility methods.",
            "input_format_expected": "mocked arrays and patched model calls",
            "output_format_expected": "unittest result",
            "can_score_candidate_reference_pair": "no",
            "reference_based": "no",
            "reference_free": "partial internals only",
            "notes": "Tests are skipped unless transformers, sentence_transformers, simcse, and projects.roscoe imports are available.",
        },
    ]

    dependency_rows = [
        {
            "dependency": "ParlAI repository/package",
            "required_or_optional": "required for stock CLI/import paths",
            "reason_needed": "projects.roscoe imports assume ParlAI source layout; CLI uses ParlaiParser.",
            "installed_in_current_env": module_installed("parlai"),
            "likely_python_compatibility": "setup.py says >=3.8, but current modern Python 3.12 plus old transitive deps may be risky",
            "risk_level": "high",
            "notes": "Full install likely large; minimal source copy may be possible but still needs project import layout.",
        },
        {
            "dependency": "torch",
            "required_or_optional": "required",
            "reason_needed": "model inference and tensor operations",
            "installed_in_current_env": module_installed("torch"),
            "likely_python_compatibility": "available in current .venv per prior setup",
            "risk_level": "medium",
            "notes": "CPU mode is possible but may be slow.",
        },
        {
            "dependency": "transformers",
            "required_or_optional": "required",
            "reason_needed": "AutoTokenizer/AutoModel/NLI/PPL/grammar models",
            "installed_in_current_env": module_installed("transformers"),
            "likely_python_compatibility": "available in current .venv, but ROSCOE was written for older APIs",
            "risk_level": "medium",
            "notes": "Requires Hugging Face model downloads.",
        },
        {
            "dependency": "sentence-transformers",
            "required_or_optional": "required by eager import",
            "reason_needed": "sentence embedding metrics",
            "installed_in_current_env": module_installed("sentence_transformers"),
            "likely_python_compatibility": "modern versions may support 3.12, exact ROSCOE compatibility unknown",
            "risk_level": "high",
            "notes": "Not installed in current .venv.",
        },
        {
            "dependency": "simcse",
            "required_or_optional": "required by eager import",
            "reason_needed": "fine-tuned ROSCOE/SimCSE embedding model support",
            "installed_in_current_env": module_installed("simcse"),
            "likely_python_compatibility": "unclear for Python 3.12",
            "risk_level": "high",
            "notes": "README requires simcse; import failure blocks score.py even if only sentence-transformers mode is used.",
        },
        {
            "dependency": "nltk",
            "required_or_optional": "required for CLI parsing",
            "reason_needed": "sent_tokenize and reasoning-step splitting",
            "installed_in_current_env": module_installed("nltk"),
            "likely_python_compatibility": "likely OK",
            "risk_level": "medium",
            "notes": "May require punkt data download for CLI adapter.",
        },
        {
            "dependency": "scipy",
            "required_or_optional": "listed setup dependency",
            "reason_needed": "README says install/upgrade scipy",
            "installed_in_current_env": module_installed("scipy"),
            "likely_python_compatibility": "likely OK",
            "risk_level": "medium",
            "notes": "Version sensitivity unknown.",
        },
        {
            "dependency": "facebook/roscoe-512-roberta-base",
            "required_or_optional": "optional but paper-relevant",
            "reason_needed": "fine-tuned ROSCOE embedding model",
            "installed_in_current_env": False,
            "likely_python_compatibility": "model download/runtime dependent",
            "risk_level": "high",
            "notes": "Hugging Face model weights required.",
        },
        {
            "dependency": "MoritzLaurer/DeBERTa-v3-large-mnli-fever-anli-ling-wanli",
            "required_or_optional": "required for logical inference metrics",
            "reason_needed": "NLI contradiction probabilities",
            "installed_in_current_env": False,
            "likely_python_compatibility": "model download/runtime dependent",
            "risk_level": "high",
            "notes": "Large model; CPU runtime likely expensive.",
        },
        {
            "dependency": "gpt2-large",
            "required_or_optional": "required for PPL language metrics",
            "reason_needed": "perplexity metrics",
            "installed_in_current_env": False,
            "likely_python_compatibility": "model download/runtime dependent",
            "risk_level": "high",
            "notes": "Large model; CPU runtime likely expensive.",
        },
        {
            "dependency": "cointegrated/roberta-large-cola-krishna2020",
            "required_or_optional": "required for grammar metrics",
            "reason_needed": "grammaticality classifier",
            "installed_in_current_env": False,
            "likely_python_compatibility": "model download/runtime dependent",
            "risk_level": "high",
            "notes": "Large model; CPU runtime likely expensive.",
        },
    ]

    feasibility_decision = "FEASIBLE_BUT_HEAVY" if analyses.get("projects/roscoe/score.py") else "UNCLEAR_NEEDS_MANUAL_INSPECTION"

    write_csv(
        OUT_DIR / "parlai_roscoe_file_inventory.csv",
        inventory_rows,
        [
            "source",
            "path",
            "file_type",
            "size_bytes_if_known",
            "reason_relevant",
            "contains_metric_logic",
            "contains_entrypoint",
            "contains_dependency_imports",
            "notes",
        ],
    )
    write_csv(
        OUT_DIR / "parlai_roscoe_entrypoints.csv",
        entrypoint_rows,
        [
            "path",
            "function_or_command",
            "purpose",
            "input_format_expected",
            "output_format_expected",
            "can_score_candidate_reference_pair",
            "reference_based",
            "reference_free",
            "notes",
        ],
    )
    write_csv(
        OUT_DIR / "parlai_roscoe_dependency_risks.csv",
        dependency_rows,
        [
            "dependency",
            "required_or_optional",
            "reason_needed",
            "installed_in_current_env",
            "likely_python_compatibility",
            "risk_level",
            "notes",
        ],
    )

    install_plan = """# ParlAI ROSCOE Install Plan

## Conservative Plan

1. Create `.venv_roscoe` using a Python version known to support the needed dependencies. Prefer Python 3.10 or 3.11 if available; use Python 3.12 only after a dry dependency resolution check.
2. Do not modify the main `.venv`.
3. Clone or sparse-checkout only the ParlAI files needed for `projects/roscoe`, `projects/__init__.py`, and minimal package imports into a temporary external folder.
4. Install minimal dependencies in `.venv_roscoe`: `torch`, `transformers`, `sentence-transformers`, `simcse`, `scipy`, `nltk`, and only enough ParlAI package/source context to satisfy imports.
5. Run a smoke test on two toy candidate/reference pairs using `projects.roscoe.score.Evaluator` directly.
6. Start with embedding-only scores to avoid NLI, PPL, and grammar model downloads.
7. Stop immediately if dependency resolution conflicts, import-time model loading fails, or CPU runtime is excessive.

## Full ParlAI Plan

Use this only if the conservative plan cannot import ROSCOE safely.

1. Create `.venv_roscoe`.
2. Clone ParlAI into a temporary external folder under `/tmp/roscoe_parlai_scan/` or another disposable path outside this repo.
3. Install ParlAI and ROSCOE README dependencies inside `.venv_roscoe`.
4. Download only the model weights needed for the first smoke test.
5. Run `tests/nightly/cpu/test_roscoe.py` or a smaller direct `Evaluator` smoke test.
6. Score a 30-row pilot from canonical reasoning-only text.
7. Run the full 252 rows only if all pilot rows score successfully and runtime is reasonable.

## Rollback / Cleanup

- Delete `.venv_roscoe` if dependency resolution fails.
- Delete the temporary ParlAI clone.
- Do not delete or modify project outputs, raw runs, `learning.db`, or frozen metric artifacts.
- Keep dependency reports and manifests only.
"""
    (OUT_DIR / "parlai_roscoe_install_plan.md").write_text(install_plan, encoding="utf-8")

    readme = """# ParlAI ROSCOE Feasibility v1

This artifact corrects the prior ROSCOE dependency scan by looking specifically inside Meta AI's ParlAI repository.

The earlier scan rejected the unrelated PyPI `roscoe` package. That rejection still stands: the PyPI package is an LLM-agent orchestration SDK, not the ROSCOE paper metric suite.

This scan found a real ROSCOE implementation under `projects/roscoe` in `facebookresearch/ParlAI`, but it did not install dependencies, create `.venv_roscoe`, download models, or compute ROSCOE scores.

This is a dependency feasibility artifact only.
"""
    (OUT_DIR / "README.md").write_text(readme, encoding="utf-8")

    score_analysis = analyses.get("projects/roscoe/score.py", {})
    report = f"""# ROSCOE ParlAI Feasibility Report

## Feasibility Decision

`{feasibility_decision}`

The ROSCOE paper implementation appears to exist in Meta AI's ParlAI repository under `projects/roscoe`, but it is not a lightweight standalone package. It is feasible to attempt in an isolated environment, but the dependency and model burden is heavy enough that it should not be run before a public/intermediary analytics post unless ROSCOE is essential to that post.

## Answers

1. Does the ROSCOE paper implementation appear to exist in ParlAI?

   Yes. `projects/roscoe/README.md` is titled "ROSCOE: A Suite of Metrics for Scoring Step-by-Step Reasoning" and `projects/roscoe/score.py` implements the metric constants and `Evaluator`.

2. What exact files contain it?

   Core files:
   - `projects/roscoe/score.py`
   - `projects/roscoe/roscoe.py`
   - `projects/roscoe/utils.py`
   - `projects/roscoe/README.md`
   - `tests/nightly/cpu/test_roscoe.py`

   Supporting files are listed in `parlai_roscoe_file_inventory.csv`.

3. What are the import paths or command-line entry points?

   - CLI: `python projects/roscoe/roscoe.py --dataset-path PATH --datasets NAME --scores ...`
   - Programmatic: `from projects.roscoe.score import Chain, Evaluator`

4. Can it score arbitrary candidate/reference text pairs?

   Yes, but not directly from plain rows. A small adapter is needed to split candidate/reference/source text into `Chain` objects and choose which text becomes ROSCOE `context`, `hypos`, and `references`.

5. Does it support reference-based scoring?

   Yes. `SUPERVISED_SCORES` includes reasoning alignment, external hallucination, redundancy, common sense error, missing step, semantic coverage step, and semantic coverage chain.

6. Does it support reference-free scoring?

   Yes. `UNSUPERVISED_SCORES` includes faithfulness, repetition, informativeness, discourse representation, coherence, perplexity, and grammar metrics.

7. What metric families are implemented?

   - semantic alignment: yes
   - semantic similarity: yes
   - logical inference: yes
   - language coherence: yes
   - repetition: yes
   - other: informativeness, semantic coverage, hallucination/missing-step style scores

8. What model dependencies are required?

   - `sentence-transformers`
   - `simcse`
   - `transformers`
   - `torch`
   - NLI model: `MoritzLaurer/DeBERTa-v3-large-mnli-fever-anli-ling-wanli`
   - PPL model: `gpt2-large`
   - grammar model: `cointegrated/roberta-large-cola-krishna2020`
   - embedding models including `all-mpnet-base-v2`, `all-MiniLM-L6-v2`, and `facebook/roscoe-512-roberta-base`

9. What Python version is likely required?

   ParlAI `setup.py` says Python `>=3.8`. Practical compatibility is uncertain with Python 3.12 because ROSCOE depends on older research-stack packages such as `simcse` and sentence-transformers.

10. Is it compatible with the current environment?

   Not as-is. Current `.venv` lacks `sentence_transformers` and `simcse`. `torch` and `transformers` are available, but this task explicitly forbids modifying `.venv`.

11. Can it be run without installing all of ParlAI?

   Possibly, but not cleanly. `score.py` imports `projects.roscoe.utils`; `roscoe.py` imports `parlai.core.params.ParlaiParser`. A direct `Evaluator` adapter may avoid the CLI and most ParlAI runtime, but still needs the source package layout and dependencies.

12. Can it be isolated into `.venv_roscoe` safely?

   Yes, as a next experiment, provided the install is treated as disposable and stopped on conflicts. No isolated environment was created in this scan.

13. What is the estimated engineering cost?

   Medium-high. A minimal direct-adapter route is likely 0.5-1 day if dependencies resolve; full ParlAI install plus model/runtime debugging could take longer.

14. Is this worth doing before the LinkedIn intermediary analytics post?

   Not recommended unless ROSCOE is central to the post. Existing BERTScore, ROUGE-L, chrF, and deterministic comparisons are already reproducible. ROSCOE is heavier and likely to distract from the current analytics story.

15. What is the safest next action?

   Create `.venv_roscoe` only in a dedicated follow-up task, try a minimal `Evaluator` smoke test with embedding-only metrics, and avoid full NLI/PPL/grammar metrics until the embedding path works.

## Metrics Detected

Metric constants detected in `score.py`:

{', '.join(score_analysis.get('metric_constants', []))}

## Source Fetch Status

- Network error: `{network_error or 'none'}`
- ParlAI repo cloned: false
- Temporary clone path: none

## Validation

- Dependencies installed: false
- `.venv` modified: false
- `.venv_roscoe` created: false
- `learning.db` modified: false
- Raw outputs modified: false
- Model calls made: false
- External LLM API calls: false
- ROSCOE scores computed: false
- Phase 2 semantics implemented: false
"""
    (OUT_DIR / "ROSCOE_PARLAI_FEASIBILITY_REPORT.md").write_text(report, encoding="utf-8")

    after_stats = protected_stats()
    manifest = {
        "artifact_name": "roscoe_parlai_feasibility_v1",
        "created_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "purpose": "ParlAI-specific feasibility scan for ROSCOE metric implementation",
        "read_only": True,
        "learning_db_modified": before_stats.get("learning.db") != after_stats.get("learning.db"),
        "raw_outputs_modified": any(
            before_stats.get(p) != after_stats.get(p)
            for p in PROTECTED_PATHS
            if p != "learning.db"
        ),
        "main_venv_modified": False,
        "venv_roscoe_created": (ROOT / ".venv_roscoe").exists(),
        "dependencies_installed": False,
        "model_calls_made": False,
        "external_llm_api_calls": False,
        "roscoe_scores_computed": False,
        "phase2_semantics_implemented": False,
        "parlai_repo_cloned": False,
        "temporary_clone_path": None,
        "network_error": network_error,
        "feasibility_decision": feasibility_decision,
        "repo": f"https://github.com/{REPO}",
        "branch": BRANCH,
        "key_files_fetched": sorted(source_texts),
        "source_hashes": {path: sha256_text(text) for path, text in source_texts.items() if not text.startswith("FETCH_ERROR:")},
        "output_files": [
            "README.md",
            "ROSCOE_PARLAI_FEASIBILITY_REPORT.md",
            "parlai_roscoe_file_inventory.csv",
            "parlai_roscoe_entrypoints.csv",
            "parlai_roscoe_dependency_risks.csv",
            "parlai_roscoe_install_plan.md",
            "manifest.json",
        ],
    }
    (OUT_DIR / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    print(f"feasibility_decision={feasibility_decision}")
    print(f"output_dir={OUT_DIR.relative_to(ROOT)}")
    print(f"inventory_rows={len(inventory_rows)}")
    print(f"network_error={network_error or 'none'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
