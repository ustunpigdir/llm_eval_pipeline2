#!/usr/bin/env python3
"""Run structured-prompt pilot v5 through the sibling eval-pipeline provider stack."""
from __future__ import annotations

import json
import sys
import importlib.util
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PILOT_NAME = "structured_prompt_pilot_v5"
OUT_DIR = ROOT / "outputs" / PILOT_NAME
RUN_PLAN_PATH = OUT_DIR / "structured_prompt_pilot_v5_run_plan.json"
RUNS_PATH = OUT_DIR / "structured_prompt_pilot_v5_runs.json"
PROGRESS_PATH = OUT_DIR / "structured_prompt_pilot_v5_run_progress.json"
DEFAULT_WORKERS = 4
EVAL_PIPELINE_RUNNER = ROOT.parent / "Pipeline" / "Pipelines" / "eval_pipeline_v2" / "run_plan_runner.py"


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def load_plan() -> dict[str, Any]:
    return json.loads(RUN_PLAN_PATH.read_text(encoding="utf-8"))


def validate_plan(plan: dict[str, Any]) -> list[dict[str, Any]]:
    items = plan.get("items", [])
    if len(items) != 64:
        raise SystemExit(f"Expected 64 planned assignments, found {len(items)}")
    if any("Nemotron" in item.get("model_label", "") for item in items):
        raise SystemExit("Nemotron assignment detected; refusing to run v5")
    return items


def print_credential_check() -> int:
    plan = load_plan()
    items = validate_plan(plan)
    runner = load_eval_pipeline_runner()
    runner.load_local_env()
    configured = 0
    missing = []
    for item in items:
        env_name, api_key = runner.api_key_for(item)
        if api_key:
            configured += 1
        else:
            missing.append(env_name or item.get("model_id", ""))
    print("credential_source=eval_pipeline_v2")
    print(f"assignments_with_key={configured}/{len(items)}")
    print("missing_key_names=" + json.dumps(sorted(set(missing))))
    print(f"assignments_ready={len(items)}")
    print(f"prompt_mode={plan.get('prompt_mode')}")
    return 0 if configured == len(items) else 1


def load_eval_pipeline_runner():
    if not EVAL_PIPELINE_RUNNER.exists():
        raise SystemExit(f"Missing eval pipeline runner: {EVAL_PIPELINE_RUNNER}")
    spec = importlib.util.spec_from_file_location("eval_pipeline_v2_run_plan_runner", EVAL_PIPELINE_RUNNER)
    if spec is None or spec.loader is None:
        raise SystemExit(f"Cannot import eval pipeline runner: {EVAL_PIPELINE_RUNNER}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_with_eval_pipeline_runner() -> None:
    """Use the sibling eval_pipeline_v2 runner/provider stack that executed v2."""
    plan = load_plan()
    items = validate_plan(plan)
    runner = load_eval_pipeline_runner()
    runner.load_local_env()

    original_model_config_for = runner.model_config_for

    def model_config_for_external_plan(item: dict[str, Any]) -> dict[str, Any]:
        config = dict(original_model_config_for(item))
        if config:
            # The external v5 plan is an explicit experiment pack; do not let
            # the sibling UI's current enabled/disabled checkbox state skip rows.
            config["enabled"] = True
        return config

    runner.model_config_for = model_config_for_external_plan
    records = runner.run_plan(
        plan,
        dry_run=False,
        progress_path=PROGRESS_PATH,
        workers=int(plan.get("workers") or DEFAULT_WORKERS),
    )
    runner.write_json(RUNS_PATH, records)
    ok = sum(1 for row in records if row.get("status") == "OK")
    errors = len(records) - ok
    empty = sum(1 for row in records if row.get("status") == "OK" and not (row.get("response") or "").strip())
    print(f"started_runs={len(items)}")
    print(f"completed_runs={ok}")
    print(f"failed_runs={errors}")
    print(f"model_errors={errors}")
    print(f"empty_responses={empty}")
    print(f"new_output_location={RUNS_PATH}")


def main() -> None:
    if "--check-credentials" in sys.argv or "--dry-run" in sys.argv:
        raise SystemExit(print_credential_check())

    if "--standalone" in sys.argv:
        raise SystemExit("V5 must run through eval_pipeline_v2; standalone execution is disabled.")
    run_with_eval_pipeline_runner()


if __name__ == "__main__":
    main()
