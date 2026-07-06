#!/usr/bin/env python3
"""Provision Python 3.11 for isolated ROSCOE smoke tests.

This script only provisions/validates a Python runtime. It does not install
ROSCOE, ParlAI, simcse, sentence-transformers, or any benchmark dependencies.
"""

from __future__ import annotations

import datetime as dt
import json
import shutil
import subprocess
import time
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "outputs" / "metric_comparison_analytics_roscoe_python311_provision_v1"
VALIDATION_VENV = ROOT / "tmp" / "roscoe_py311_venv_validation"

DISCOVERY_COMMANDS = [
    ["which", "python3.11"],
    ["python3.11", "--version"],
    ["/opt/homebrew/bin/python3.11", "--version"],
    ["/usr/local/bin/python3.11", "--version"],
    ["which", "brew"],
    ["brew", "--version"],
    ["which", "pyenv"],
    ["pyenv", "--version"],
]

PYTHON_CANDIDATES = [
    "python3.11",
    "/opt/homebrew/bin/python3.11",
    "/usr/local/bin/python3.11",
]

PROTECTED_PATHS = [
    "learning.db",
    "outputs/structured_prompt_pilot_v2/structured_prompt_pilot_v2_runs.json",
    "outputs/structured_prompt_pilot_v3/structured_prompt_pilot_v3_runs.json",
    "outputs/structured_prompt_pilot_v4/structured_prompt_pilot_v4_runs.json",
    "outputs/structured_prompt_pilot_v5/structured_prompt_pilot_v5_runs.json",
    "outputs/metric_text_artifacts_v1/canonical_reasoning_text_dataset.csv",
]


def run_cmd(cmd: list[str], timeout: int = 120) -> dict[str, Any]:
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


def protected_stats() -> dict[str, dict[str, int]]:
    stats = {}
    for rel in PROTECTED_PATHS:
        path = ROOT / rel
        if path.exists():
            st = path.stat()
            stats[rel] = {"mtime": int(st.st_mtime), "size": st.st_size}
    return stats


def discover() -> list[dict[str, Any]]:
    return [run_cmd(cmd) for cmd in DISCOVERY_COMMANDS]


def python_version(executable: str) -> str | None:
    result = run_cmd([executable, "--version"])
    text = result["stdout"] or result["stderr"]
    if result["returncode"] == 0 and text.startswith("Python 3.11"):
        return text
    return None


def find_python311() -> tuple[str | None, str | None]:
    for candidate in PYTHON_CANDIDATES:
        version = python_version(candidate)
        if version:
            return candidate, version
    return None, None


def command_exists(command: str) -> bool:
    result = run_cmd(["which", command])
    return result["returncode"] == 0 and bool(result["stdout"])


def validate_python(executable: str) -> tuple[bool, str, bool, bool]:
    lines = []
    validation_created = False
    validation_deleted = False
    checks = [
        run_cmd([executable, "--version"]),
        run_cmd([executable, "-m", "venv", "--help"]),
        run_cmd([executable, "-m", "pip", "--version"]),
    ]
    for check in checks:
        lines.append(f"$ {check['command']}")
        lines.append(f"returncode={check['returncode']}")
        if check["stdout"]:
            lines.append(check["stdout"])
        if check["stderr"]:
            lines.append(check["stderr"])
        lines.append("")

    if VALIDATION_VENV.exists():
        shutil.rmtree(VALIDATION_VENV)
    create = run_cmd([executable, "-m", "venv", str(VALIDATION_VENV)], timeout=240)
    validation_created = create["returncode"] == 0 and VALIDATION_VENV.exists()
    lines.append(f"$ {create['command']}")
    lines.append(f"returncode={create['returncode']}")
    if create["stdout"]:
        lines.append(create["stdout"])
    if create["stderr"]:
        lines.append(create["stderr"])
    lines.append("")

    venv_python = VALIDATION_VENV / "bin" / "python"
    if validation_created:
        vcheck = run_cmd([str(venv_python), "--version"])
        lines.append(f"$ {vcheck['command']}")
        lines.append(f"returncode={vcheck['returncode']}")
        lines.append(vcheck["stdout"] or vcheck["stderr"])
        lines.append("")
        shutil.rmtree(VALIDATION_VENV)
        validation_deleted = not VALIDATION_VENV.exists()

    ok = (
        checks[0]["returncode"] == 0
        and (checks[0]["stdout"] or checks[0]["stderr"]).startswith("Python 3.11")
        and checks[1]["returncode"] == 0
        and checks[2]["returncode"] == 0
        and validation_created
        and validation_deleted
    )
    return ok, "\n".join(lines), validation_created, validation_deleted


def format_command_log(results: list[dict[str, Any]]) -> str:
    lines = []
    for result in results:
        lines.append(f"$ {result['command']}")
        lines.append(f"returncode={result['returncode']}")
        if result["stdout"]:
            lines.append("stdout:")
            lines.append(result["stdout"])
        if result["stderr"]:
            lines.append("stderr:")
            lines.append(result["stderr"])
        lines.append("")
    return "\n".join(lines)


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    before = protected_stats()
    created_at = dt.datetime.now(dt.timezone.utc).isoformat()

    discovery_results = discover()
    write_text(OUT_DIR / "python311_discovery_log.txt", format_command_log(discovery_results))

    existing_python, existing_version = find_python311()
    python_found_before_install = existing_python is not None
    install_attempted = False
    install_method = "none" if python_found_before_install else "unavailable"
    install_lines = []

    selected_python = existing_python
    selected_version = existing_version

    if not selected_python:
        if command_exists("brew"):
            install_attempted = True
            install_method = "homebrew"
            install_lines.append("$ brew install python@3.11")
            install_result = run_cmd(["brew", "install", "python@3.11"], timeout=1800)
            install_lines.append(f"returncode={install_result['returncode']}")
            if install_result["stdout"]:
                install_lines.append("stdout:")
                install_lines.append(install_result["stdout"])
            if install_result["stderr"]:
                install_lines.append("stderr:")
                install_lines.append(install_result["stderr"])
            selected_python, selected_version = find_python311()
        elif command_exists("pyenv"):
            install_attempted = True
            install_method = "pyenv"
            install_lines.append("$ pyenv install 3.11.9")
            install_result = run_cmd(["pyenv", "install", "3.11.9"], timeout=3600)
            install_lines.append(f"returncode={install_result['returncode']}")
            if install_result["stdout"]:
                install_lines.append("stdout:")
                install_lines.append(install_result["stdout"])
            if install_result["stderr"]:
                install_lines.append("stderr:")
                install_lines.append(install_result["stderr"])
            selected_python, selected_version = find_python311()
        else:
            install_lines.append("No Python 3.11 found. Homebrew and pyenv are unavailable, so no install was attempted.")

    if not install_lines:
        install_lines.append("Python 3.11 already existed; no install attempted.")
    write_text(OUT_DIR / "python311_install_log.txt", "\n".join(install_lines) + "\n")

    validation_status = False
    validation_log = "Python 3.11 executable unavailable; validation not run.\n"
    validation_created = False
    validation_deleted = False
    if selected_python:
        validation_status, validation_log, validation_created, validation_deleted = validate_python(selected_python)
    write_text(OUT_DIR / "python311_validation_log.txt", validation_log)

    ready = bool(validation_status and selected_python and selected_version)
    recommended = ".venv/bin/python scripts/run_roscoe_smoke_test_v2_py310_or_311.py" if ready else "Provision Python 3.11, then rerun this script."

    report = f"""# Python 3.11 Provision Report

## 1. Purpose

Provide a Python 3.11 runtime for the isolated Meta/ParlAI ROSCOE smoke test.

## 2. Previous ROSCOE Blocker

ROSCOE smoke v2 could not run because no Python 3.10/3.11 runtime was available. Python 3.12 hit the `simcse`/old SciPy dependency path.

## 3. Discovery Results

See `python311_discovery_log.txt`.

## 4. Install Method Used

- Python 3.11 found before install: {python_found_before_install}
- Install attempted: {install_attempted}
- Install method: `{install_method}`

## 5. Python 3.11 Executable Selected

- Executable: `{selected_python or 'none'}`
- Version: `{selected_version or 'none'}`

## 6. Validation Results

- Validation status: {validation_status}
- Temporary venv created: {validation_created}
- Temporary venv deleted: {validation_deleted}

See `python311_validation_log.txt`.

## 7. Whether ROSCOE Smoke v2 Can Now Be Retried

{ready}

## 8. What Was Not Changed

- Main `.venv` modified: false
- ROSCOE dependencies installed: false
- `learning.db` modified: false
- Raw outputs modified: false
- Frozen metric artifacts modified: false
- Benchmark rows scored: false
- Model/API calls made: false
- BERTScore run: false
- Phase 2 semantics implemented: false

## 9. Recommended Next Command

```bash
{recommended}
```
"""
    write_text(OUT_DIR / "PYTHON311_PROVISION_REPORT.md", report)

    readme = """# Python 3.11 Provision for ROSCOE v1

This artifact records Python 3.11 discovery, optional local provisioning, and validation for a future isolated ROSCOE smoke test.

It does not install ROSCOE, ParlAI, simcse, sentence-transformers, or benchmark dependencies.
"""
    write_text(OUT_DIR / "README.md", readme)

    after = protected_stats()
    manifest = {
        "artifact_name": "python311_provision_for_roscoe_v1",
        "created_at": created_at,
        "purpose": "provide Python 3.11 runtime for isolated ROSCOE smoke test",
        "python311_found_before_install": python_found_before_install,
        "install_attempted": install_attempted,
        "install_method": install_method,
        "python311_executable": selected_python,
        "python311_version": selected_version,
        "validation_venv_created": validation_created,
        "validation_venv_deleted": validation_deleted,
        "main_venv_modified": False,
        "roscoe_dependencies_installed": False,
        "learning_db_modified": before.get("learning.db") != after.get("learning.db"),
        "raw_outputs_modified": any(before.get(p) != after.get(p) for p in PROTECTED_PATHS if p != "learning.db"),
        "frozen_metric_artifacts_modified": before.get("outputs/metric_text_artifacts_v1/canonical_reasoning_text_dataset.csv") != after.get("outputs/metric_text_artifacts_v1/canonical_reasoning_text_dataset.csv"),
        "benchmark_rows_scored": False,
        "model_calls_made": False,
        "external_llm_api_calls": False,
        "bertscore_run": False,
        "phase2_semantics_implemented": False,
        "ready_to_retry_roscoe_smoke_v2": ready,
        "output_files": [
            "README.md",
            "PYTHON311_PROVISION_REPORT.md",
            "python311_discovery_log.txt",
            "python311_install_log.txt",
            "python311_validation_log.txt",
            "manifest.json",
        ],
    }
    write_text(OUT_DIR / "manifest.json", json.dumps(manifest, indent=2) + "\n")

    print(f"python311_found_before_install={python_found_before_install}")
    print(f"install_attempted={install_attempted}")
    print(f"install_method={install_method}")
    print(f"python311_executable={selected_python or 'none'}")
    print(f"python311_version={selected_version or 'none'}")
    print(f"validation_status={validation_status}")
    print(f"ready_to_retry_roscoe_smoke_v2={ready}")
    print(f"output_dir={OUT_DIR.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
