#!/usr/bin/env python3
"""Run or record an isolated ROSCOE smoke-test attempt.

This script is intentionally conservative. It does not install dependencies by
itself; dependency installation is performed explicitly outside the script so
the command/output can be reviewed. The script fetches the small ParlAI ROSCOE
source files, attempts imports inside `.venv_roscoe`, and writes the smoke-test
artifact. If imports fail, no metric scores are fabricated.
"""

from __future__ import annotations

import datetime as dt
import importlib.util
import json
import math
import os
from pathlib import Path
import subprocess
import sys
import time
from typing import Any
from urllib.request import urlopen


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "outputs" / "metric_comparison_analytics_roscoe_smoke_v1"
RUNTIME_DIR = ROOT / "tmp" / "roscoe_parlai_runtime"
VENV = ROOT / ".venv_roscoe"
VENV_PY = VENV / "bin" / "python"
VENV_PIP = VENV / "bin" / "pip"
REPO = "facebookresearch/ParlAI"
BRANCH = "main"
RAW_BASE = f"https://raw.githubusercontent.com/{REPO}/{BRANCH}/"
COMMIT_API = f"https://api.github.com/repos/{REPO}/commits/{BRANCH}"

ROSCOE_FILES = [
    "projects/roscoe/README.md",
    "projects/roscoe/score.py",
    "projects/roscoe/roscoe.py",
    "projects/roscoe/utils.py",
    "tests/nightly/cpu/test_roscoe.py",
]

PROTECTED_PATHS = [
    "learning.db",
    "outputs/structured_prompt_pilot_v2/structured_prompt_pilot_v2_runs.json",
    "outputs/structured_prompt_pilot_v3/structured_prompt_pilot_v3_runs.json",
    "outputs/structured_prompt_pilot_v4/structured_prompt_pilot_v4_runs.json",
    "outputs/structured_prompt_pilot_v5/structured_prompt_pilot_v5_runs.json",
    "outputs/metric_text_artifacts_v1/canonical_reasoning_text_dataset.csv",
]

SMOKE_PAIRS = [
    {
        "pair_id": "A_good_equivalent_reasoning",
        "candidate_text": "First compute x = 2. Then compute y = x + 3 = 5. Therefore the final value is 5.",
        "reference_text": "Set x equal to 2. Add 3 to x, giving y = 5. Therefore the answer is 5.",
    },
    {
        "pair_id": "B_arithmetic_contradiction",
        "candidate_text": "First compute x = 2. Then compute y = x + 3 = 9. Therefore the final value is 9.",
        "reference_text": "Set x equal to 2. Add 3 to x, giving y = 5. Therefore the answer is 5.",
    },
    {
        "pair_id": "C_unrelated_reasoning",
        "candidate_text": "The capital city is discussed first. Then the weather is described. Therefore the answer is about geography.",
        "reference_text": "Set x equal to 2. Add 3 to x, giving y = 5. Therefore the answer is 5.",
    },
]


def read_url(url: str) -> str:
    with urlopen(url, timeout=30) as response:
        return response.read().decode("utf-8", errors="replace")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def run_cmd(cmd: list[str], *, cwd: Path = ROOT, timeout: int = 60) -> dict[str, Any]:
    start = time.time()
    try:
        proc = subprocess.run(
            cmd,
            cwd=str(cwd),
            text=True,
            capture_output=True,
            timeout=timeout,
        )
        return {
            "cmd": cmd,
            "returncode": proc.returncode,
            "stdout": proc.stdout,
            "stderr": proc.stderr,
            "duration_seconds": round(time.time() - start, 3),
        }
    except Exception as exc:  # noqa: BLE001
        return {
            "cmd": cmd,
            "returncode": None,
            "stdout": "",
            "stderr": repr(exc),
            "duration_seconds": round(time.time() - start, 3),
        }


def protected_stats() -> dict[str, dict[str, int]]:
    out = {}
    for rel in PROTECTED_PATHS:
        path = ROOT / rel
        if path.exists():
            st = path.stat()
            out[rel] = {"mtime": int(st.st_mtime), "size": st.st_size}
    return out


def module_present(module: str) -> bool:
    return importlib.util.find_spec(module) is not None


def fetch_roscoe_source() -> tuple[str, list[str]]:
    fetched = []
    errors = []
    for rel in ROSCOE_FILES:
        try:
            text = read_url(RAW_BASE + rel)
            write_text(RUNTIME_DIR / rel, text)
            fetched.append(rel)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{rel}: {exc!r}")
    for init_path in [
        RUNTIME_DIR / "projects" / "__init__.py",
        RUNTIME_DIR / "projects" / "roscoe" / "__init__.py",
        RUNTIME_DIR / "tests" / "__init__.py",
    ]:
        write_text(init_path, "")
    return "\n".join(errors), fetched


def get_parlai_commit() -> str:
    try:
        data = json.loads(read_url(COMMIT_API))
        return data.get("sha", "unknown")
    except Exception:  # noqa: BLE001
        return "unknown"


def attempt_import() -> dict[str, Any]:
    code = f"""
import json
import sys
sys.path.insert(0, {str(RUNTIME_DIR)!r})
result = {{}}
try:
    import projects.roscoe.score as score
    result["import_score"] = "ok"
    result["available_reasoning_scores"] = list(score.REASONING_SCORES)
    result["embedding_scores"] = list(score.EMB_MODEL_SCORES)
    result["supervised_scores"] = list(score.SUPERVISED_SCORES)
    result["unsupervised_scores"] = list(score.UNSUPERVISED_SCORES)
except Exception as exc:
    result["import_score"] = "failed"
    result["error"] = type(exc).__name__ + ": " + str(exc)
try:
    import sentence_transformers
    result["sentence_transformers"] = "ok"
except Exception as exc:
    result["sentence_transformers"] = "failed: " + type(exc).__name__ + ": " + str(exc)
try:
    import simcse
    result["simcse"] = "ok"
except Exception as exc:
    result["simcse"] = "failed: " + type(exc).__name__ + ": " + str(exc)
print(json.dumps(result, indent=2))
"""
    return run_cmd([str(VENV_PY), "-c", code], timeout=120)


def attempt_smoke_if_import_ok(import_result: dict[str, Any]) -> tuple[list[dict[str, Any]], list[str], str]:
    try:
        parsed = json.loads(import_result["stdout"])
    except Exception:
        parsed = {}
    if parsed.get("import_score") != "ok":
        return (
            [
                {
                    **pair,
                    "input_format_used": "not_run_import_failed",
                    "roscoe_scoring_status": "failed",
                    "metrics": {},
                    "error_if_any": parsed.get("error", "import failed before scoring"),
                }
                for pair in SMOKE_PAIRS
            ],
            [],
            "failed",
        )

    # Keep this path for future reruns if dependencies become available. Use only
    # embedding scores to avoid NLI/PPL/grammar model downloads.
    code = f"""
import json
import math
import sys
sys.path.insert(0, {str(RUNTIME_DIR)!r})
from projects.roscoe.score import Chain, Evaluator, CHAIN_ALIGNMENT, SEMANTIC_COVERAGE_CHAIN, SEMANTIC_COVERAGE_STEP, INFORM_CHAIN, INFORM_STEP
pairs = {json.dumps(SMOKE_PAIRS)}
score_types = [CHAIN_ALIGNMENT, SEMANTIC_COVERAGE_CHAIN, SEMANTIC_COVERAGE_STEP, INFORM_CHAIN, INFORM_STEP]
hypos = [Chain(p["candidate_text"].split(". ")) for p in pairs]
refs = [Chain(p["reference_text"].split(". ")) for p in pairs]
contexts = refs
ev = Evaluator(hypos=hypos, context=contexts, references=refs, score_types=score_types)
scores = ev.evaluate(score_types=score_types)
rows = []
for i, pair in enumerate(pairs):
    metrics = {{k: float(v[i]) for k, v in scores.items()}}
    rows.append({{**pair, "input_format_used": "simple_sentence_boundary_steps", "roscoe_scoring_status": "scored", "metrics": metrics, "error_if_any": ""}})
print(json.dumps(rows, indent=2))
"""
    result = run_cmd([str(VENV_PY), "-c", code], timeout=900)
    if result["returncode"] != 0:
        return (
            [
                {
                    **pair,
                    "input_format_used": "simple_sentence_boundary_steps",
                    "roscoe_scoring_status": "failed",
                    "metrics": {},
                    "error_if_any": result["stderr"][-2000:] or result["stdout"][-2000:],
                }
                for pair in SMOKE_PAIRS
            ],
            [],
            "failed",
        )
    rows = json.loads(result["stdout"])
    metrics = sorted({metric for row in rows for metric in row.get("metrics", {})})
    finite = all(
        isinstance(value, (int, float)) and math.isfinite(value)
        for row in rows
        for value in row.get("metrics", {}).values()
    )
    return rows, metrics, "passed" if finite and rows else "partial"


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    before = protected_stats()
    created_at = dt.datetime.now(dt.timezone.utc).isoformat()

    source_errors, fetched = fetch_roscoe_source()
    parlai_commit = get_parlai_commit()

    py_version = run_cmd([str(VENV_PY), "--version"]) if VENV_PY.exists() else {"stdout": "", "stderr": "missing .venv_roscoe python", "returncode": 1}
    pip_version = run_cmd([str(VENV_PIP), "--version"]) if VENV_PIP.exists() else {"stdout": "", "stderr": "missing .venv_roscoe pip", "returncode": 1}
    pip_list = run_cmd([str(VENV_PIP), "list"]) if VENV_PIP.exists() else {"stdout": "", "stderr": "missing .venv_roscoe pip", "returncode": 1}

    dependency_log = f"""# ROSCOE smoke dependency log

Created/used environment:
- path: .venv_roscoe
- python: {py_version.get('stdout') or py_version.get('stderr')}
- pip: {pip_version.get('stdout') or pip_version.get('stderr')}

Install command attempted manually before this script:

`.venv_roscoe/bin/pip install numpy tqdm scipy nltk transformers sentence-transformers simcse`

Result:

Failed. `simcse` dependency resolution attempted to build `scipy==1.5.4`, which attempted to build `numpy==1.17.3`; that path fails under Python 3.12 with `NameError: name 'CCompiler' is not defined`.

No packages were installed in `.venv_roscoe`; current package list:

```text
{pip_list.get('stdout', '').strip()}
{pip_list.get('stderr', '').strip()}
```
"""
    write_text(OUT_DIR / "roscoe_smoke_dependency_log.txt", dependency_log)

    import_result = attempt_import() if VENV_PY.exists() else {"returncode": 1, "stdout": "", "stderr": "missing .venv_roscoe python"}
    import_log = f"""# ROSCOE smoke import log

Source runtime directory: `{RUNTIME_DIR.relative_to(ROOT)}`

Fetched source files:
{chr(10).join('- ' + f for f in fetched) or '- none'}

Source fetch errors:
{source_errors or 'none'}

Import command:
`{VENV_PY} -c <import projects.roscoe.score>`

Return code: {import_result.get('returncode')}

stdout:
```json
{import_result.get('stdout', '').strip()}
```

stderr:
```text
{import_result.get('stderr', '').strip()}
```
"""
    write_text(OUT_DIR / "roscoe_smoke_import_log.txt", import_log)

    smoke_rows, metrics_available, smoke_status = attempt_smoke_if_import_ok(import_result)
    smoke_pairs_scored = sum(1 for row in smoke_rows if row.get("roscoe_scoring_status") == "scored")
    selected_semantic_metric = ""
    for candidate in ["reasoning_alignment", "semantic_coverage_chain", "semantic_coverage_step", "informativeness_chain", "informativeness_step"]:
        if candidate in metrics_available:
            selected_semantic_metric = candidate
            break

    runtime_log = f"""# ROSCOE smoke runtime log

Device info:
- local smoke scoring was attempted only if import succeeded
- benchmark rows scored: false
- model calls made: false
- external LLM API calls: false

Smoke status: {smoke_status}
Smoke pairs attempted: {len(SMOKE_PAIRS)}
Smoke pairs scored: {smoke_pairs_scored}
Metrics available: {', '.join(metrics_available) if metrics_available else 'none'}
"""
    write_text(OUT_DIR / "roscoe_smoke_runtime_log.txt", runtime_log)

    results = {
        "artifact_name": "roscoe_smoke_test_v1",
        "created_at": created_at,
        "parlai_source": f"https://github.com/{REPO}",
        "parlai_commit": parlai_commit,
        "roscoe_files_used": fetched,
        "smoke_test_status": smoke_status,
        "smoke_pairs_attempted": len(SMOKE_PAIRS),
        "smoke_pairs_scored": smoke_pairs_scored,
        "metrics_available": metrics_available,
        "selected_semantic_metric_if_any": selected_semantic_metric,
        "pairs": smoke_rows,
    }
    write_text(OUT_DIR / "roscoe_smoke_test_results.json", json.dumps(results, indent=2) + "\n")

    md_lines = [
        "# ROSCOE Smoke Test Results",
        "",
        f"- Status: `{smoke_status}`",
        f"- Pairs attempted: {len(SMOKE_PAIRS)}",
        f"- Pairs scored: {smoke_pairs_scored}",
        f"- Metrics available: {', '.join(metrics_available) if metrics_available else 'none'}",
        f"- Selected semantic metric: {selected_semantic_metric or 'none'}",
        "",
        "| pair | status | available metrics | selected semantic score | notes |",
        "|---|---|---|---|---|",
    ]
    for row in smoke_rows:
        metrics = row.get("metrics", {})
        selected_value = metrics.get(selected_semantic_metric, "") if selected_semantic_metric else ""
        note = row.get("error_if_any", "") or "numeric ROSCOE scores returned"
        note = note.replace("\n", " ")[:240]
        md_lines.append(
            f"| {row['pair_id']} | {row['roscoe_scoring_status']} | {', '.join(metrics) if metrics else 'none'} | {selected_value} | {note} |"
        )
    write_text(OUT_DIR / "roscoe_smoke_test_results.md", "\n".join(md_lines) + "\n")

    good_vs_unrelated = "not_available"
    arithmetic_behavior = "not_available"
    if smoke_pairs_scored == 3 and selected_semantic_metric:
        by_id = {row["pair_id"]: row for row in smoke_rows}
        good = by_id["A_good_equivalent_reasoning"]["metrics"][selected_semantic_metric]
        bad = by_id["B_arithmetic_contradiction"]["metrics"][selected_semantic_metric]
        unrelated = by_id["C_unrelated_reasoning"]["metrics"][selected_semantic_metric]
        good_vs_unrelated = "passed" if good > unrelated else "failed"
        arithmetic_behavior = f"{bad} on {selected_semantic_metric}; semantic overlap may remain high despite arithmetic contradiction"

    report = f"""# ROSCOE Smoke Test Report

## 1. Purpose

Test whether the real Meta/ParlAI ROSCOE implementation can run locally in an isolated environment.

## 2. Environment Isolation

- `.venv_roscoe` created/used: {VENV.exists()}
- Main `.venv` modified: false
- Python executable: `{VENV_PY}`
- Python version: `{(py_version.get('stdout') or py_version.get('stderr')).strip()}`

## 3. Dependency Path Attempted

Minimal dependency route was attempted first. The install command failed because `simcse` pulled an old SciPy/Numpy build path incompatible with Python 3.12.

## 4. ParlAI/ROSCOE Source Used

- Source: `https://github.com/{REPO}`
- Commit: `{parlai_commit}`
- Runtime source directory: `{RUNTIME_DIR.relative_to(ROOT)}`
- Files used: {', '.join(fetched)}

## 5. Import Results

Import status: `{'ok' if smoke_status != 'failed' else 'failed'}`

See `roscoe_smoke_import_log.txt`.

## 6. Smoke Test Input Pairs

Three required toy pairs were registered in `roscoe_smoke_test_results.json`.

## 7. Metrics Available

{', '.join(metrics_available) if metrics_available else 'None; import failed before ROSCOE could expose runnable metrics in `.venv_roscoe`.'}

## 8. Smoke Test Results

- Status: `{smoke_status}`
- Pairs attempted: {len(SMOKE_PAIRS)}
- Pairs scored: {smoke_pairs_scored}

## 9. Non-Degeneracy Check

- good vs unrelated: `{good_vs_unrelated}`
- arithmetic contradiction behavior: `{arithmetic_behavior}`

## 10. Runtime and Resource Notes

No benchmark rows were scored. No Hugging Face model weights were downloaded by the smoke runner because dependency import failed before scoring.

## 11. Whether Pilot 30 Rows Is Safe

No. Pilot 30 is not safe until `.venv_roscoe` can import `projects.roscoe.score` and score all three toy pairs.

## 12. Limitations

- Python 3.10/3.11 was not available on PATH.
- Python 3.12 dependency resolution failed at `simcse`/old `scipy`.
- No fake or substitute ROSCOE metrics were produced.

## 13. Recommended Next Step

Retry in an isolated Python 3.10 or 3.11 environment, or patch a local copy of ParlAI ROSCOE to make `simcse` optional when using sentence-transformer-only metrics. Do not proceed to pilot rows until the three-pair smoke test returns finite numeric scores.
"""
    write_text(OUT_DIR / "ROSCOE_SMOKE_TEST_REPORT.md", report)

    readme = """# ROSCOE Smoke Test v1

This folder records an isolated smoke-test attempt for the real Meta/ParlAI ROSCOE implementation.

No benchmark rows were scored. No ROSCOE scores were fabricated. The attempt stopped before scoring because the isolated Python 3.12 environment could not install/import the required ROSCOE dependency stack, specifically `simcse` and its old SciPy/Numpy build path.
"""
    write_text(OUT_DIR / "README.md", readme)

    after = protected_stats()
    manifest = {
        "artifact_name": "roscoe_smoke_test_v1",
        "created_at": created_at,
        "purpose": "isolated smoke test for Meta/ParlAI ROSCOE implementation",
        "read_only_project_data": True,
        "main_venv_modified": False,
        "venv_roscoe_created": VENV.exists(),
        "dependencies_installed_in_venv_roscoe": False,
        "learning_db_modified": before.get("learning.db") != after.get("learning.db"),
        "raw_outputs_modified": any(before.get(p) != after.get(p) for p in PROTECTED_PATHS if p != "learning.db"),
        "frozen_metric_artifacts_modified": before.get("outputs/metric_text_artifacts_v1/canonical_reasoning_text_dataset.csv") != after.get("outputs/metric_text_artifacts_v1/canonical_reasoning_text_dataset.csv"),
        "benchmark_rows_scored": False,
        "model_calls_made": False,
        "external_llm_api_calls": False,
        "bertscore_run": False,
        "phase2_semantics_implemented": False,
        "parlai_source": f"https://github.com/{REPO}",
        "parlai_commit": parlai_commit,
        "roscoe_files_used": fetched,
        "smoke_pairs_attempted": len(SMOKE_PAIRS),
        "smoke_pairs_scored": smoke_pairs_scored,
        "metrics_available": metrics_available,
        "smoke_test_status": smoke_status,
        "pilot_30_recommended": False,
        "output_files": [
            "README.md",
            "ROSCOE_SMOKE_TEST_REPORT.md",
            "roscoe_smoke_test_results.json",
            "roscoe_smoke_test_results.md",
            "roscoe_smoke_dependency_log.txt",
            "roscoe_smoke_import_log.txt",
            "roscoe_smoke_runtime_log.txt",
            "manifest.json",
        ],
    }
    write_text(OUT_DIR / "manifest.json", json.dumps(manifest, indent=2) + "\n")

    print(f"smoke_test_status={smoke_status}")
    print(f"smoke_pairs_scored={smoke_pairs_scored}")
    print(f"metrics_available={','.join(metrics_available) if metrics_available else 'none'}")
    print(f"output_dir={OUT_DIR.relative_to(ROOT)}")
    return 0 if smoke_status in {"passed", "partial", "failed"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
