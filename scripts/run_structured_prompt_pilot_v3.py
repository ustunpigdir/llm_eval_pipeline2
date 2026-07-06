#!/usr/bin/env python3
"""Run structured-prompt pilot v3 through an OpenAI-compatible chat endpoint."""
from __future__ import annotations

import json
import os
import sys
import time
import urllib.error
import urllib.request
import uuid
import importlib.util
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PILOT_NAME = "structured_prompt_pilot_v3"
OUT_DIR = ROOT / "outputs" / PILOT_NAME
RUN_PLAN_PATH = OUT_DIR / "structured_prompt_pilot_v3_run_plan.json"
RUNS_PATH = OUT_DIR / "structured_prompt_pilot_v3_runs.json"
PROGRESS_PATH = OUT_DIR / "structured_prompt_pilot_v3_run_progress.json"
DEFAULT_BASE_URL = "https://openrouter.ai/api/v1"
DEFAULT_WORKERS = 4
MAX_TOKENS = 12288
TEMPERATURE = 0.0
EVAL_PIPELINE_RUNNER = ROOT.parent / "Pipeline" / "Pipelines" / "eval_pipeline_v2" / "run_plan_runner.py"


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def load_dotenv(path: Path = ROOT / ".env") -> None:
    """Load simple KEY=VALUE pairs without printing or overriding env vars."""
    if not path.exists():
        return
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()
        if not key or key in os.environ:
            continue
        if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
            value = value[1:-1]
        os.environ[key] = value


def api_key() -> str:
    load_dotenv()
    key = os.environ.get("OPENROUTER_API_KEY") or os.environ.get("OPENAI_API_KEY")
    if not key:
        raise SystemExit("Missing API key names: OPENROUTER_API_KEY, OPENAI_API_KEY")
    return key


def base_url() -> str:
    load_dotenv()
    return (os.environ.get("OPENROUTER_BASE_URL") or os.environ.get("OPENAI_BASE_URL") or DEFAULT_BASE_URL).rstrip("/")


def selected_provider_name() -> str:
    load_dotenv()
    if os.environ.get("OPENROUTER_API_KEY"):
        return "OPENROUTER"
    if os.environ.get("OPENAI_API_KEY"):
        return "OPENAI"
    return "none"


def credential_status() -> dict[str, Any]:
    load_dotenv()
    return {
        "selected_provider": selected_provider_name(),
        "OPENROUTER_API_KEY_present": bool(os.environ.get("OPENROUTER_API_KEY")),
        "OPENAI_API_KEY_present": bool(os.environ.get("OPENAI_API_KEY")),
        "base_url_configured": bool(os.environ.get("OPENROUTER_BASE_URL") or os.environ.get("OPENAI_BASE_URL")),
    }


def load_plan() -> dict[str, Any]:
    return json.loads(RUN_PLAN_PATH.read_text(encoding="utf-8"))


def validate_plan(plan: dict[str, Any]) -> list[dict[str, Any]]:
    items = plan.get("items", [])
    if len(items) != 64:
        raise SystemExit(f"Expected 64 planned assignments, found {len(items)}")
    if any("Nemotron" in item.get("model_label", "") for item in items):
        raise SystemExit("Nemotron assignment detected; refusing to run v3")
    return items


def print_credential_check() -> int:
    plan = load_plan()
    items = validate_plan(plan)
    status = credential_status()
    print(f"selected_provider={status['selected_provider']}")
    print(f"OPENROUTER_API_KEY_present={'yes' if status['OPENROUTER_API_KEY_present'] else 'no'}")
    print(f"OPENAI_API_KEY_present={'yes' if status['OPENAI_API_KEY_present'] else 'no'}")
    print(f"base_url_configured={'yes' if status['base_url_configured'] else 'no'}")
    print(f"assignments_ready={len(items)}")
    print(f"prompt_mode={plan.get('prompt_mode')}")
    return 0 if (status["OPENROUTER_API_KEY_present"] or status["OPENAI_API_KEY_present"]) else 1


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
            # The external v3 plan is an explicit experiment pack; do not let
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


def call_chat_completion(item: dict[str, Any], key: str, url: str) -> dict[str, Any]:
    payload = {
        "model": item["model"],
        "messages": [{"role": "user", "content": item["prompt"]}],
        "temperature": TEMPERATURE,
        "max_tokens": MAX_TOKENS,
    }
    if item.get("system_prompt"):
        payload["messages"].insert(0, {"role": "system", "content": item["system_prompt"]})

    request = urllib.request.Request(
        f"{url}/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/ustunpigdir/llm_eval_pipeline2",
            "X-Title": "llm_eval_pipeline2 structured prompt pilot v3",
        },
        method="POST",
    )
    started = time.time()
    try:
        with urllib.request.urlopen(request, timeout=300) as response:
            data = json.loads(response.read().decode("utf-8"))
        choice = data.get("choices", [{}])[0]
        message = choice.get("message") or {}
        usage = data.get("usage") or {}
        return {
            "status": "OK",
            "response": message.get("content") or "",
            "finish_reason": choice.get("finish_reason") or "",
            "input_tokens": usage.get("prompt_tokens"),
            "output_tokens": usage.get("completion_tokens"),
            "error": "",
            "latency_seconds": round(time.time() - started, 3),
        }
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        return {
            "status": "ERROR",
            "response": "",
            "finish_reason": "",
            "input_tokens": None,
            "output_tokens": None,
            "error": f"HTTP {exc.code}: {body[:1000]}",
            "latency_seconds": round(time.time() - started, 3),
        }
    except Exception as exc:
        return {
            "status": "ERROR",
            "response": "",
            "finish_reason": "",
            "input_tokens": None,
            "output_tokens": None,
            "error": f"{type(exc).__name__}: {exc}",
            "latency_seconds": round(time.time() - started, 3),
        }


def run_item(item: dict[str, Any], key: str, url: str) -> dict[str, Any]:
    result = call_chat_completion(item, key, url)
    return {
        "run_id": str(uuid.uuid4()),
        "parent_run_id": None,
        "parent_question_id": None,
        "question_id": item["scenario_id"],
        "question_title": item["scenario_title"],
        "question_kind": "main",
        "model_id": item["model_id"],
        "model_label": item["model_label"],
        "provider": item["provider"],
        "model": item["model"],
        "trial": int(item.get("trial") or 1),
        "timestamp": utc_now(),
        "prompt": item["prompt"],
        "messages": [{"role": "user", "content": item["prompt"]}],
        "response": result["response"],
        "finish_reason": result["finish_reason"],
        "input_tokens": result["input_tokens"],
        "output_tokens": result["output_tokens"],
        "latency_seconds": result["latency_seconds"],
        "status": result["status"],
        "error": result["error"],
        "temperature": TEMPERATURE,
        "max_tokens": MAX_TOKENS,
        "attempts": 1,
        "response_quality_labels": [],
        "artifact_labels": [],
        "numeric_labels": [],
        "conceptual_labels": [],
        "critical_failure_labels": [],
        "error_labels": [],
        "review_status": "",
        "verdict": "",
        "score": None,
        "evaluator_notes": "",
        "human_reviewed_at": None,
    }


def write_progress(results: list[dict[str, Any]], total: int) -> None:
    completed = sum(1 for row in results if row["status"] == "OK")
    failed = sum(1 for row in results if row["status"] != "OK")
    progress = {
        "prompt_mode": PILOT_NAME,
        "updated_at": utc_now(),
        "started_runs": len(results),
        "completed_runs": completed,
        "failed_runs": failed,
        "total_assignments": total,
        "output_file": str(RUNS_PATH),
    }
    PROGRESS_PATH.write_text(json.dumps(progress, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    if "--check-credentials" in sys.argv or "--dry-run" in sys.argv:
        raise SystemExit(print_credential_check())

    if "--standalone" not in sys.argv:
        run_with_eval_pipeline_runner()
        return

    plan = load_plan()
    items = validate_plan(plan)

    key = api_key()
    url = base_url()
    workers = int(os.environ.get("STRUCTURED_PROMPT_WORKERS") or plan.get("workers") or 4)
    results: list[dict[str, Any]] = []
    with ThreadPoolExecutor(max_workers=workers) as executor:
        future_to_item = {executor.submit(run_item, item, key, url): item for item in items}
        for future in as_completed(future_to_item):
            results.append(future.result())
            results.sort(key=lambda row: (row["question_id"], row["model_label"], row["trial"]))
            RUNS_PATH.write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            write_progress(results, len(items))

    completed = sum(1 for row in results if row["status"] == "OK")
    failed = len(results) - completed
    empty = sum(1 for row in results if row["status"] == "OK" and not (row.get("response") or "").strip())
    print(f"started_runs={len(results)}")
    print(f"completed_runs={completed}")
    print(f"failed_runs={failed}")
    print(f"model_errors={failed}")
    print(f"empty_responses={empty}")
    print(f"new_output_location={RUNS_PATH}")


if __name__ == "__main__":
    main()
