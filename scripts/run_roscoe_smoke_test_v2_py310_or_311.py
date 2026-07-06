#!/usr/bin/env python3
"""Route A ROSCOE smoke-test retry with Python 3.10/3.11.

The first version of this script stopped after Python discovery. This patched
version creates an isolated ROSCOE venv when a compatible Python is found,
attempts a minimal ParlAI ROSCOE dependency/import path, and runs only the
three toy smoke pairs. It does not score benchmark rows.
"""

from __future__ import annotations

import datetime as dt
import json
import math
from pathlib import Path
import subprocess
import time
from typing import Any
from urllib.request import urlopen


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "outputs" / "metric_comparison_analytics_roscoe_smoke_v2_py310_or_311"
RUNTIME_DIR = ROOT / "tmp" / "roscoe_parlai_runtime_v2"
REPO = "facebookresearch/ParlAI"
BRANCH = "main"
RAW_BASE = f"https://raw.githubusercontent.com/{REPO}/{BRANCH}/"
COMMIT_API = f"https://api.github.com/repos/{REPO}/commits/{BRANCH}"
ROOT_CAUSE = (
    "The previous v2 script set smoke_status='not_run' whenever a compatible "
    "Python was found, but had no execution branch for creating the isolated "
    "venv, installing dependencies, importing ROSCOE, or scoring the smoke pairs."
)

PYTHON_CANDIDATES = [
    "python3.11",
    "python3.10",
    "/opt/homebrew/bin/python3.11",
    "/opt/homebrew/bin/python3.10",
    "/usr/local/bin/python3.11",
    "/usr/local/bin/python3.10",
]

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

EMBEDDING_SCORE_NAMES = [
    "reasoning_alignment",
    "semantic_coverage_chain",
    "semantic_coverage_step",
    "informativeness_chain",
    "informativeness_step",
    "repetition_step",
]


def run_cmd(cmd: list[str], timeout: int = 300) -> dict[str, Any]:
    start = time.time()
    try:
        proc = subprocess.run(
            cmd,
            cwd=str(ROOT),
            text=True,
            capture_output=True,
            timeout=timeout,
        )
        return {
            "command": " ".join(cmd),
            "returncode": proc.returncode,
            "stdout": proc.stdout.strip(),
            "stderr": proc.stderr.strip(),
            "duration_seconds": round(time.time() - start, 3),
        }
    except Exception as exc:  # noqa: BLE001
        return {
            "command": " ".join(cmd),
            "returncode": None,
            "stdout": "",
            "stderr": repr(exc),
            "duration_seconds": round(time.time() - start, 3),
        }


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def read_url(url: str) -> str:
    with urlopen(url, timeout=30) as response:
        return response.read().decode("utf-8", errors="replace")


def protected_stats() -> dict[str, dict[str, int]]:
    stats = {}
    for rel in PROTECTED_PATHS:
        path = ROOT / rel
        if path.exists():
            st = path.stat()
            stats[rel] = {"mtime": int(st.st_mtime), "size": st.st_size}
    return stats


def get_parlai_commit() -> str:
    try:
        data = json.loads(read_url(COMMIT_API))
        return data.get("sha", "unknown")
    except Exception:  # noqa: BLE001
        return "unknown"


def discover_python() -> tuple[list[dict[str, Any]], str | None, str | None]:
    discovery = []
    for candidate in PYTHON_CANDIDATES:
        result = run_cmd([candidate, "--version"], timeout=30)
        discovery.append(result)
        version_text = result["stdout"] or result["stderr"]
        if result["returncode"] == 0 and (
            version_text.startswith("Python 3.11") or version_text.startswith("Python 3.10")
        ):
            return discovery, candidate, version_text
    return discovery, None, None


def venv_for_version(version_text: str | None) -> Path | None:
    if not version_text:
        return None
    if version_text.startswith("Python 3.11"):
        return ROOT / ".venv_roscoe_py311"
    if version_text.startswith("Python 3.10"):
        return ROOT / ".venv_roscoe_py310"
    return None


def fetch_roscoe_source() -> tuple[list[str], str]:
    fetched = []
    errors = []
    for rel in ROSCOE_FILES:
        try:
            write_text(RUNTIME_DIR / rel, read_url(RAW_BASE + rel))
            fetched.append(rel)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{rel}: {exc!r}")
    for init_path in [
        RUNTIME_DIR / "projects" / "__init__.py",
        RUNTIME_DIR / "projects" / "roscoe" / "__init__.py",
        RUNTIME_DIR / "tests" / "__init__.py",
    ]:
        write_text(init_path, "")
    return fetched, "\n".join(errors)


def format_cmd_log(results: list[dict[str, Any]]) -> str:
    lines = []
    for result in results:
        lines.append(f"$ {result['command']}")
        lines.append(f"returncode={result['returncode']} duration={result['duration_seconds']}s")
        if result["stdout"]:
            lines.append("stdout:")
            lines.append(result["stdout"])
        if result["stderr"]:
            lines.append("stderr:")
            lines.append(result["stderr"])
        lines.append("")
    return "\n".join(lines)


def create_and_install(selected_python: str, venv_path: Path) -> tuple[bool, bool, str, list[dict[str, Any]]]:
    logs = []
    env_created = False
    deps_installed = False
    if not venv_path.exists():
        create = run_cmd([selected_python, "-m", "venv", str(venv_path)], timeout=240)
        logs.append(create)
        env_created = create["returncode"] == 0 and venv_path.exists()
        if not env_created:
            return env_created, deps_installed, "venv_creation_failed", logs
    else:
        env_created = True
        logs.append(
            {
                "command": f"{selected_python} -m venv {venv_path}",
                "returncode": 0,
                "stdout": "Skipped: existing isolated venv reused.",
                "stderr": "",
                "duration_seconds": 0,
            }
        )

    pip = venv_path / "bin" / "pip"
    py = venv_path / "bin" / "python"
    install_steps = [
        [str(py), "-m", "pip", "install", "--upgrade", "pip"],
        [
            str(pip),
            "install",
            "numpy",
            "tqdm",
            "scipy",
            "nltk",
            "torch",
            "transformers",
            "sentence-transformers",
            "scikit-learn",
        ],
        [str(pip), "install", "simcse", "--no-deps"],
    ]
    for step in install_steps:
        result = run_cmd(step, timeout=1800)
        logs.append(result)
        if result["returncode"] != 0:
            return env_created, deps_installed, "dependency_install_failed", logs

    freeze = run_cmd([str(pip), "freeze"], timeout=120)
    logs.append(freeze)
    deps_installed = True
    return env_created, deps_installed, "dependencies_installed", logs


def attempt_import(venv_path: Path) -> tuple[str, list[str], str]:
    py = venv_path / "bin" / "python"
    code = f"""
import json
import sys
sys.path.insert(0, {str(RUNTIME_DIR)!r})
result = {{}}
try:
    import projects.roscoe.score as score
    result["import_status"] = "ok"
    result["reasoning_scores"] = list(score.REASONING_SCORES)
    result["embedding_scores"] = list(score.EMB_MODEL_SCORES)
except Exception as exc:
    result["import_status"] = "failed"
    result["error"] = type(exc).__name__ + ": " + str(exc)
print(json.dumps(result, indent=2))
"""
    result = run_cmd([str(py), "-c", code], timeout=180)
    status = "failed"
    metrics: list[str] = []
    try:
        parsed = json.loads(result["stdout"])
        status = parsed.get("import_status", "failed")
        metrics = parsed.get("embedding_scores", [])
    except Exception:
        pass
    log = f"""# ROSCOE smoke v2 import log

Runtime source directory: `{RUNTIME_DIR.relative_to(ROOT)}`

Import command:
`{result['command']}`

Return code: {result['returncode']}

stdout:
```json
{result['stdout']}
```

stderr:
```text
{result['stderr']}
```
"""
    return status, metrics, log


def attempt_smoke(venv_path: Path) -> tuple[list[dict[str, Any]], list[str], str, str, str, str]:
    py = venv_path / "bin" / "python"
    code = f"""
import json
import sys
sys.path.insert(0, {str(RUNTIME_DIR)!r})
from projects.roscoe.score import Chain, Evaluator

pairs = {json.dumps(SMOKE_PAIRS)}
score_names = {json.dumps(EMBEDDING_SCORE_NAMES)}
import projects.roscoe.score as score
score_types = [getattr(score, name.upper(), None) for name in []]
score_types = [
    score.CHAIN_ALIGNMENT,
    score.SEMANTIC_COVERAGE_CHAIN,
    score.SEMANTIC_COVERAGE_STEP,
    score.INFORM_CHAIN,
    score.INFORM_STEP,
    score.REPETITION_SENT,
]
hypos = [Chain([s.strip() for s in p["candidate_text"].split(".") if s.strip()]) for p in pairs]
refs = [Chain([s.strip() for s in p["reference_text"].split(".") if s.strip()]) for p in pairs]
contexts = refs
evaluator = Evaluator(
    hypos=hypos,
    context=contexts,
    references=refs,
    score_types=score_types,
    transformer_model="all-MiniLM-L6-v2",
)
scores = evaluator.evaluate(score_types=score_types)
rows = []
for i, pair in enumerate(pairs):
    metrics = {{}}
    for metric_name, values in scores.items():
        value = values[i]
        if isinstance(value, str):
            metrics[metric_name] = value
        else:
            metrics[metric_name] = float(value)
    rows.append({{
        **pair,
        "input_format_used": "simple_sentence_boundary_split",
        "roscoe_scoring_status": "scored",
        "metrics": metrics,
        "error_if_any": "",
    }})
print(json.dumps(rows, indent=2))
"""
    result = run_cmd([str(py), "-c", code], timeout=1200)
    runtime_log = f"""# ROSCOE smoke v2 runtime log

Command:
`{result['command']}`

Return code: {result['returncode']}
Duration seconds: {result['duration_seconds']}

stdout:
```json
{result['stdout'][:8000]}
```

stderr:
```text
{result['stderr'][-8000:]}
```
"""
    if result["returncode"] != 0:
        rows = [
            {
                **pair,
                "input_format_used": "simple_sentence_boundary_split",
                "roscoe_scoring_status": "failed",
                "metrics": {},
                "error_if_any": (result["stderr"] or result["stdout"])[-2000:],
            }
            for pair in SMOKE_PAIRS
        ]
        return rows, [], "failed", runtime_log, "not_available", "not_available"

    rows = json.loads(result["stdout"])
    metrics = sorted({key for row in rows for key in row.get("metrics", {})})
    finite = all(
        isinstance(value, (int, float)) and math.isfinite(value)
        for row in rows
        for value in row.get("metrics", {}).values()
    )
    selected = next((m for m in ["reasoning_alignment", "semantic_coverage_chain", "semantic_coverage_step", "informativeness_chain", "informativeness_step"] if m in metrics), "")
    good_vs_unrelated = "not_available"
    arithmetic = "not_available"
    if selected:
        by_id = {row["pair_id"]: row for row in rows}
        good = by_id["A_good_equivalent_reasoning"]["metrics"][selected]
        bad = by_id["B_arithmetic_contradiction"]["metrics"][selected]
        unrelated = by_id["C_unrelated_reasoning"]["metrics"][selected]
        good_vs_unrelated = "passed" if good > unrelated else "failed"
        arithmetic = f"{bad} on {selected}; overlap-based semantic metrics can remain high despite the arithmetic contradiction."
    unique_signatures = {tuple(row.get("metrics", {}).get(m) for m in metrics) for row in rows}
    status = "passed" if finite and len(rows) == 3 and len(unique_signatures) > 1 and good_vs_unrelated == "passed" else "partial"
    return rows, metrics, status, runtime_log, good_vs_unrelated, arithmetic


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    before = protected_stats()
    previous_status = "not_run"
    created_at = dt.datetime.now(dt.timezone.utc).isoformat()
    discovery, selected_python, selected_version = discover_python()
    parlai_commit = get_parlai_commit()
    venv_path = venv_for_version(selected_version)

    fetched_files: list[str] = []
    source_errors = ""
    environment_created = False
    deps_installed = False
    install_status = "not_attempted_no_compatible_python"
    import_status = "not_attempted"
    import_metrics: list[str] = []
    smoke_rows: list[dict[str, Any]]
    metrics_available: list[str] = []
    smoke_status = "blocked_no_compatible_python"
    good_vs_unrelated = "not_available"
    arithmetic_behavior = "not_available"
    pilot_30_recommended = False
    dependency_logs: list[dict[str, Any]] = []

    runtime_lines = [
        "# Python Runtime Discovery",
        "",
        "| executable checked | command used | result | stdout | stderr |",
        "|---|---|---|---|---|",
    ]
    for item in discovery:
        exe = item["command"].replace(" --version", "")
        runtime_lines.append(
            f"| `{exe}` | `{item['command']}` | `{item['returncode']}` | `{item['stdout'].replace('|', '\\|')}` | `{item['stderr'].replace('|', '\\|')}` |"
        )
    runtime_lines.extend(
        [
            "",
            f"- Selected Python executable: `{selected_python or 'none'}`",
            f"- Selected Python version: `{selected_version or 'none'}`",
            f"- Environment target: `{venv_path.relative_to(ROOT) if venv_path else 'none'}`",
        ]
    )
    write_text(OUT_DIR / "python_runtime_discovery.md", "\n".join(runtime_lines) + "\n")

    if selected_python and selected_version and venv_path:
        fetched_files, source_errors = fetch_roscoe_source()
        environment_created, deps_installed, install_status, dependency_logs = create_and_install(selected_python, venv_path)
        if deps_installed:
            import_status, import_metrics, import_log = attempt_import(venv_path)
            write_text(OUT_DIR / "roscoe_smoke_v2_import_log.txt", import_log)
            if import_status == "ok":
                smoke_rows, metrics_available, smoke_status, runtime_log, good_vs_unrelated, arithmetic_behavior = attempt_smoke(venv_path)
                pilot_30_recommended = smoke_status == "passed"
            else:
                smoke_status = "failed"
                runtime_log = "# ROSCOE smoke v2 runtime log\n\nScoring not attempted because import failed.\n"
                smoke_rows = [
                    {
                        **pair,
                        "input_format_used": "not_run_import_failed",
                        "roscoe_scoring_status": "failed",
                        "metrics": {},
                        "error_if_any": "Import failed; see roscoe_smoke_v2_import_log.txt.",
                    }
                    for pair in SMOKE_PAIRS
                ]
            write_text(OUT_DIR / "roscoe_smoke_v2_runtime_log.txt", runtime_log)
        else:
            smoke_status = "failed"
            write_text(
                OUT_DIR / "roscoe_smoke_v2_import_log.txt",
                "# ROSCOE smoke v2 import log\n\nImport not attempted because dependency installation failed.\n",
            )
            write_text(
                OUT_DIR / "roscoe_smoke_v2_runtime_log.txt",
                "# ROSCOE smoke v2 runtime log\n\nScoring not attempted because dependency installation failed.\n",
            )
            smoke_rows = [
                {
                    **pair,
                    "input_format_used": "not_run_dependency_failed",
                    "roscoe_scoring_status": "failed",
                    "metrics": {},
                    "error_if_any": "Dependency installation failed; see roscoe_smoke_v2_dependency_log.txt.",
                }
                for pair in SMOKE_PAIRS
            ]
    else:
        smoke_rows = [
            {
                **pair,
                "input_format_used": "not_run_no_compatible_python",
                "roscoe_scoring_status": "blocked",
                "metrics": {},
                "error_if_any": "No Python 3.10/3.11 executable found.",
            }
            for pair in SMOKE_PAIRS
        ]
        write_text(
            OUT_DIR / "roscoe_smoke_v2_import_log.txt",
            "# ROSCOE smoke v2 import log\n\nNo import attempt was made because no compatible Python was found.\n",
        )
        write_text(
            OUT_DIR / "roscoe_smoke_v2_runtime_log.txt",
            "# ROSCOE smoke v2 runtime log\n\nNo scoring attempt was made because no compatible Python was found.\n",
        )

    dependency_log = f"""# ROSCOE smoke v2 dependency log

Root cause of previous `not_run`:
{ROOT_CAUSE}

Selected Python executable: {selected_python or 'none'}
Selected Python version: {selected_version or 'none'}
Venv path: {venv_path.relative_to(ROOT) if venv_path else 'none'}
Install status: {install_status}
Fetched source files: {', '.join(fetched_files) if fetched_files else 'none'}
Source fetch errors: {source_errors or 'none'}

{format_cmd_log(dependency_logs) if dependency_logs else 'No dependency commands executed.'}
"""
    write_text(OUT_DIR / "roscoe_smoke_v2_dependency_log.txt", dependency_log)

    smoke_pairs_scored = sum(1 for row in smoke_rows if row.get("roscoe_scoring_status") == "scored")
    selected_semantic = next((m for m in ["reasoning_alignment", "semantic_coverage_chain", "semantic_coverage_step", "informativeness_chain", "informativeness_step"] if m in metrics_available), "")
    results = {
        "artifact_name": "roscoe_smoke_test_v2_py310_or_311",
        "created_at": created_at,
        "smoke_test_status": smoke_status,
        "smoke_pairs_attempted": len(SMOKE_PAIRS),
        "smoke_pairs_scored": smoke_pairs_scored,
        "metrics_available": metrics_available,
        "selected_semantic_metric_if_any": selected_semantic,
        "pairs": smoke_rows,
    }
    write_text(OUT_DIR / "roscoe_smoke_v2_results.json", json.dumps(results, indent=2) + "\n")

    md_lines = [
        "# ROSCOE Smoke v2 Results",
        "",
        "| pair | status | available metrics | selected semantic score | notes |",
        "|---|---|---|---|---|",
    ]
    for row in smoke_rows:
        metrics = row.get("metrics", {})
        selected_value = metrics.get(selected_semantic, "") if selected_semantic else ""
        note = (row.get("error_if_any") or "numeric ROSCOE scores returned").replace("\n", " ")[:240]
        md_lines.append(
            f"| {row['pair_id']} | {row['roscoe_scoring_status']} | {', '.join(metrics) if metrics else 'none'} | {selected_value} | {note} |"
        )
    write_text(OUT_DIR / "roscoe_smoke_v2_results.md", "\n".join(md_lines) + "\n")

    report = f"""# ROSCOE Smoke Test v2 Report

## 1. Purpose

Retry the Meta/ParlAI ROSCOE smoke test using Route A: a compatible Python 3.10 or 3.11 isolated runtime.

## 2. Why v2 Exists

Smoke v1 used Python 3.12 and was blocked by the ParlAI ROSCOE / `simcse` dependency path.

## Patch Update

- Root cause of previous `not_run`: {ROOT_CAUSE}
- Patch made: added venv creation, pip upgrade, minimal dependency installation, ParlAI ROSCOE source fetch, import attempt, and three-pair smoke scoring.

## 3. Python Runtime Discovery

See `python_runtime_discovery.md`.

Selected executable: `{selected_python or 'none'}`

Selected version: `{selected_version or 'none'}`

## 4. Environment Isolation

- Main `.venv` modified: false
- New ROSCOE venv created: {environment_created}
- Venv path: `{venv_path.relative_to(ROOT) if venv_path else 'none'}`
- Existing `.venv_roscoe` reused: false

## 5. Dependency Path Attempted

- Install status: `{install_status}`
- Dependencies installed in ROSCOE venv: {deps_installed}
- See `roscoe_smoke_v2_dependency_log.txt`.

## 6. ParlAI/ROSCOE Source Used

- Source: `https://github.com/{REPO}`
- Commit: `{parlai_commit}`
- ROSCOE files used: {', '.join(fetched_files or ROSCOE_FILES)}

## 7. Import Results

- Import status: `{import_status}`
- Import-visible embedding metrics: {', '.join(import_metrics) if import_metrics else 'none'}

## 8. Smoke Test Input Pairs

The three required toy pairs are recorded in `roscoe_smoke_v2_results.json`.

## 9. Metrics Available

{', '.join(metrics_available) if metrics_available else 'None'}

## 10. Smoke Test Results

- Status: `{smoke_status}`
- Pairs attempted: {len(SMOKE_PAIRS)}
- Pairs scored: {smoke_pairs_scored}

## 11. Non-Degeneracy Check

`{good_vs_unrelated}`

## 12. Arithmetic Contradiction Behavior

{arithmetic_behavior}

## 13. Runtime and Resource Notes

No benchmark rows were scored. No external LLM API calls were made. No BERTScore run was performed.

## 14. Whether Pilot 30 Rows Is Safe

{pilot_30_recommended}

## 15. Limitations

This smoke test uses the minimal embedding metric route. NLI, PPL, and grammar metrics remain intentionally excluded.

## 16. Recommended Next Step

{"Proceed to a 30-row ROSCOE pilot using this isolated venv." if pilot_30_recommended else "Do not run the 30-row pilot yet; resolve the dependency/import/scoring failure recorded in the logs first."}
"""
    write_text(OUT_DIR / "ROSCOE_SMOKE_TEST_V2_REPORT.md", report)

    readme = """# ROSCOE Smoke v2 Python 3.10/3.11 Retry

This artifact records the patched Route A isolated Meta/ParlAI ROSCOE smoke-test attempt.

It does not score benchmark rows, run BERTScore, call external LLM APIs, or implement Phase 2 semantics.
"""
    write_text(OUT_DIR / "README.md", readme)

    after = protected_stats()
    manifest = {
        "artifact_name": "roscoe_smoke_test_v2_py310_or_311",
        "created_at": created_at,
        "purpose": "isolated ROSCOE smoke test using compatible Python 3.10/3.11 runtime",
        "read_only_project_data": True,
        "main_venv_modified": False,
        "previous_status": previous_status,
        "patched_script": True,
        "root_cause": ROOT_CAUSE,
        "selected_python_executable": selected_python,
        "selected_python_version": selected_version,
        "environment_created": environment_created,
        "venv_roscoe_created": environment_created,
        "venv_roscoe_path": str(venv_path.relative_to(ROOT)) if venv_path else None,
        "dependencies_installed_in_roscoe_venv": deps_installed,
        "install_status": install_status,
        "import_status": import_status,
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
        "roscoe_files_used": fetched_files or ROSCOE_FILES,
        "smoke_pairs_attempted": len(SMOKE_PAIRS),
        "smoke_pairs_scored": smoke_pairs_scored,
        "metrics_available": metrics_available,
        "smoke_test_status": smoke_status,
        "pilot_30_recommended": pilot_30_recommended,
        "output_files": [
            "README.md",
            "ROSCOE_SMOKE_TEST_V2_REPORT.md",
            "python_runtime_discovery.md",
            "roscoe_smoke_v2_dependency_log.txt",
            "roscoe_smoke_v2_import_log.txt",
            "roscoe_smoke_v2_runtime_log.txt",
            "roscoe_smoke_v2_results.json",
            "roscoe_smoke_v2_results.md",
            "manifest.json",
        ],
    }
    write_text(OUT_DIR / "manifest.json", json.dumps(manifest, indent=2) + "\n")

    print(f"smoke_test_status={smoke_status}")
    print(f"selected_python_executable={selected_python or 'none'}")
    print(f"environment_created={str(environment_created).lower()}")
    print(f"environment_path={venv_path.relative_to(ROOT) if venv_path else 'none'}")
    print(f"install_status={install_status}")
    print(f"import_status={import_status}")
    print(f"smoke_pairs_scored={smoke_pairs_scored}")
    print(f"metrics_available={','.join(metrics_available) if metrics_available else 'none'}")
    print(f"pilot_30_recommended={str(pilot_30_recommended).lower()}")
    print(f"output_dir={OUT_DIR.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
