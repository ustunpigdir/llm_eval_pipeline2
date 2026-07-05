#!/usr/bin/env python3
"""
Import the locked 32-scenario benchmark into learning.db and map runs to scenario_id.

This script is intentionally additive:
- it does not delete rows from questions/raw answers/extraction tables
- it records out-of-benchmark runs in run_exclusions
- it creates audit views for the official gradeable set

Example:
  python3 scripts/import_official_benchmark.py \
      --db learning.db \
      --scenarios "/path/to/Scenarios to Run" \
      --audit official_benchmark_audit.md
"""
from __future__ import annotations

import argparse
import datetime as dt
import glob
import hashlib
import json
import os
import re
import sqlite3
from collections import Counter, defaultdict
from typing import Any


DEFAULT_BENCHMARK_ID = "scientific_reasoning_32_v1"
METHOD_VERSION = "prompt_prefix_hash_v1"


def normalize_text(s: str) -> str:
    """Normalize prompt text enough to match scenario prompts embedded in DB questions."""
    s = s or ""
    s = s.replace("\r\n", "\n").replace("\r", "\n")
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip()


def prompt_hash(s: str) -> str:
    return hashlib.sha256(normalize_text(s).encode("utf-8")).hexdigest()


def json_dumps(obj: Any) -> str:
    return json.dumps(obj, ensure_ascii=False, sort_keys=True)


def iter_scenario_files(scenario_dir: str):
    for path in sorted(glob.glob(os.path.join(scenario_dir, "*.json"))):
        name = os.path.basename(path)
        if name.startswith("gold_normalized"):
            continue
        if name.startswith(".") or name.startswith("_"):
            continue
        yield path


def load_scenarios(scenario_dir: str) -> list[dict[str, Any]]:
    scenarios: list[dict[str, Any]] = []
    for path in iter_scenario_files(scenario_dir):
        try:
            data = json.load(open(path, "r", encoding="utf-8"))
        except Exception:
            continue
        if not isinstance(data, list):
            continue
        for s in data:
            if not isinstance(s, dict):
                continue
            if not s.get("enabled", False):
                continue
            if "id" not in s or "prompt" not in s:
                continue
            row = dict(s)
            row["_source_file"] = os.path.basename(path)
            scenarios.append(row)
    return scenarios


def load_gold_normalized(scenario_dir: str) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    for path in sorted(glob.glob(os.path.join(scenario_dir, "gold_normalized_batch*.json"))):
        try:
            data = json.load(open(path, "r", encoding="utf-8"))
        except Exception:
            continue
        if not isinstance(data, list):
            continue
        for item in data:
            if isinstance(item, dict) and item.get("id"):
                out[item["id"]] = item
    return out


def ensure_schema(con: sqlite3.Connection) -> None:
    con.executescript(
        """
        CREATE TABLE IF NOT EXISTS scenarios (
            scenario_id TEXT PRIMARY KEY,
            title TEXT,
            category TEXT,
            kind TEXT,
            enabled INTEGER NOT NULL DEFAULT 1,
            prompt TEXT NOT NULL,
            prompt_hash TEXT NOT NULL,
            source_file TEXT,
            gold_json TEXT,
            imported_at TEXT DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS benchmark_scenarios (
            benchmark_id TEXT NOT NULL,
            scenario_id TEXT NOT NULL,
            category TEXT,
            source_file TEXT,
            active INTEGER NOT NULL DEFAULT 1,
            imported_at TEXT DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (benchmark_id, scenario_id)
        );

        CREATE TABLE IF NOT EXISTS gold_fields (
            benchmark_id TEXT NOT NULL,
            scenario_id TEXT NOT NULL,
            field_index INTEGER NOT NULL,
            field_name TEXT NOT NULL,
            expected_value_raw TEXT,
            expected_value_num REAL,
            tolerance REAL NOT NULL DEFAULT 0.01,
            tolerance_mode TEXT NOT NULL DEFAULT 'relative',
            description TEXT,
            source TEXT NOT NULL,
            PRIMARY KEY (benchmark_id, scenario_id, field_name)
        );

        CREATE TABLE IF NOT EXISTS run_scenarios (
            run_id INTEGER PRIMARY KEY,
            scenario_id TEXT,
            match_method TEXT NOT NULL,
            confidence REAL NOT NULL,
            prompt_hash TEXT,
            evidence TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS run_exclusions (
            run_id INTEGER PRIMARY KEY,
            exclusion_reason TEXT NOT NULL,
            detail TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        );

        DROP VIEW IF EXISTS official_gradeable_runs;
        CREATE VIEW official_gradeable_runs AS
        SELECT
            q.run_id,
            q.model_name,
            rs.scenario_id
        FROM questions q
        JOIN run_scenarios rs
            ON q.run_id = rs.run_id
        JOIN benchmark_scenarios bs
            ON rs.scenario_id = bs.scenario_id
        WHERE bs.benchmark_id = 'scientific_reasoning_32_v1'
          AND bs.active = 1
          AND q.run_id NOT IN (
              SELECT run_id FROM run_exclusions
          );

        DROP VIEW IF EXISTS excluded_runs;
        CREATE VIEW excluded_runs AS
        SELECT
            q.run_id,
            q.model_name,
            q.question,
            e.exclusion_reason,
            e.detail
        FROM questions q
        JOIN run_exclusions e
            ON q.run_id = e.run_id;
        """
    )


def import_scenarios(
    con: sqlite3.Connection,
    scenarios: list[dict[str, Any]],
    gold_norm: dict[str, dict[str, Any]],
    benchmark_id: str,
) -> None:
    cur = con.cursor()
    cur.execute("DELETE FROM benchmark_scenarios WHERE benchmark_id = ?", (benchmark_id,))
    cur.execute("DELETE FROM gold_fields WHERE benchmark_id = ?", (benchmark_id,))

    for s in scenarios:
        sid = s["id"]
        gold = s.get("gold") or {}
        cur.execute(
            """
            INSERT OR REPLACE INTO scenarios
              (scenario_id, title, category, kind, enabled, prompt, prompt_hash, source_file, gold_json, imported_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
            """,
            (
                sid,
                s.get("title"),
                s.get("category"),
                s.get("kind"),
                1 if s.get("enabled", False) else 0,
                s.get("prompt", ""),
                prompt_hash(s.get("prompt", "")),
                s.get("_source_file"),
                json_dumps(gold),
            ),
        )
        cur.execute(
            """
            INSERT OR REPLACE INTO benchmark_scenarios
              (benchmark_id, scenario_id, category, source_file, active, imported_at)
            VALUES (?, ?, ?, ?, 1, CURRENT_TIMESTAMP)
            """,
            (benchmark_id, sid, s.get("category"), s.get("_source_file")),
        )

        tolerance = float(gold.get("tolerance", 0.01))
        tolerance_mode = str(gold.get("tolerance_mode", "relative"))
        fields = gold.get("expected_values") or []

        # Prefer explicit scenario JSON gold. Use gold_normalized only as a consistency source.
        norm_fields = {
            f.get("field_name"): f
            for f in (gold_norm.get(sid, {}).get("fields") or [])
            if isinstance(f, dict)
        }

        for idx, f in enumerate(fields):
            name = f.get("name")
            if not name:
                continue
            val = f.get("value")
            raw = str(val)
            try:
                num = float(val)
            except Exception:
                # fallback if normalized gold gives a number
                nf = norm_fields.get(name) or {}
                num = nf.get("value_num")
            cur.execute(
                """
                INSERT OR REPLACE INTO gold_fields
                  (benchmark_id, scenario_id, field_index, field_name,
                   expected_value_raw, expected_value_num, tolerance, tolerance_mode,
                   description, source)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    benchmark_id,
                    sid,
                    idx,
                    name,
                    raw,
                    num,
                    tolerance,
                    tolerance_mode,
                    f.get("description"),
                    "scenario_json",
                ),
            )


def match_runs(con: sqlite3.Connection, scenarios: list[dict[str, Any]]) -> dict[str, Any]:
    """Populate run_scenarios and run_exclusions from question prompt matching."""
    cur = con.cursor()
    cur.execute("DELETE FROM run_scenarios")
    cur.execute("DELETE FROM run_exclusions")

    scenario_prompts = []
    for s in scenarios:
        scenario_prompts.append(
            {
                "scenario_id": s["id"],
                "prompt": normalize_text(s.get("prompt", "")),
                "prompt_hash": prompt_hash(s.get("prompt", "")),
            }
        )
    # Longest prompt first prevents accidental partial matches.
    scenario_prompts.sort(key=lambda x: len(x["prompt"]), reverse=True)

    rows = cur.execute("SELECT run_id, model_name, question FROM questions ORDER BY run_id").fetchall()

    matched = []
    unmatched = []
    for run_id, model_name, question in rows:
        q_norm = normalize_text(question)
        q_hash = prompt_hash(question)
        found = None
        for s in scenario_prompts:
            p = s["prompt"]
            if q_norm == p or q_norm.startswith(p) or p in q_norm:
                found = s
                break
        if found:
            cur.execute(
                """
                INSERT OR REPLACE INTO run_scenarios
                  (run_id, scenario_id, match_method, confidence, prompt_hash, evidence, created_at)
                VALUES (?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
                """,
                (
                    run_id,
                    found["scenario_id"],
                    METHOD_VERSION,
                    1.0,
                    q_hash,
                    f"question contains official scenario prompt; scenario_prompt_hash={found['prompt_hash']}",
                ),
            )
            matched.append((run_id, model_name, found["scenario_id"]))
        else:
            snippet = q_norm[:240].replace("\n", " ")
            cur.execute(
                """
                INSERT OR REPLACE INTO run_exclusions
                  (run_id, exclusion_reason, detail, created_at)
                VALUES (?, ?, ?, CURRENT_TIMESTAMP)
                """,
                (
                    run_id,
                    "OUT_OF_BENCHMARK",
                    "No prompt match against locked 32-scenario benchmark. " + snippet,
                ),
            )
            unmatched.append((run_id, model_name, snippet))

    return {"matched": matched, "unmatched": unmatched}


def write_audit(
    audit_path: str,
    con: sqlite3.Connection,
    scenarios: list[dict[str, Any]],
    gold_norm: dict[str, dict[str, Any]],
    benchmark_id: str,
    match_info: dict[str, Any],
) -> None:
    cur = con.cursor()
    official = cur.execute(
        "SELECT COUNT(*) FROM benchmark_scenarios WHERE benchmark_id = ? AND active = 1",
        (benchmark_id,),
    ).fetchone()[0]
    total_runs = cur.execute("SELECT COUNT(*) FROM questions").fetchone()[0]
    prompt_families = cur.execute("SELECT COUNT(DISTINCT question) FROM questions").fetchone()[0]
    gradeable = cur.execute("SELECT COUNT(*) FROM official_gradeable_runs").fetchone()[0]
    excluded = cur.execute("SELECT COUNT(*) FROM run_exclusions").fetchone()[0]
    gold_fields = cur.execute(
        "SELECT COUNT(*) FROM gold_fields WHERE benchmark_id = ?", (benchmark_id,)
    ).fetchone()[0]

    by_scenario = cur.execute(
        """
        SELECT rs.scenario_id, COUNT(*) AS n
        FROM run_scenarios rs
        JOIN benchmark_scenarios bs ON bs.scenario_id = rs.scenario_id
        WHERE bs.benchmark_id = ?
        GROUP BY rs.scenario_id
        ORDER BY rs.scenario_id
        """,
        (benchmark_id,),
    ).fetchall()

    excluded_rows = cur.execute(
        """
        SELECT run_id, model_name, substr(detail, 1, 160)
        FROM excluded_runs
        ORDER BY run_id
        """
    ).fetchall()

    scenario_ids = {s["id"] for s in scenarios}
    norm_ids = set(gold_norm)
    missing_norm = sorted(scenario_ids - norm_ids)
    extra_norm = sorted(norm_ids - scenario_ids)

    lines = []
    lines.append(f"# Official Benchmark Audit\n")
    lines.append(f"- benchmark_id: `{benchmark_id}`")
    lines.append(f"- method_version: `{METHOD_VERSION}`")
    lines.append(f"- generated_at: `{dt.datetime.now(dt.UTC).isoformat(timespec='seconds').replace('+00:00', '')}Z`")
    lines.append(f"- official_scenarios: **{official}**")
    lines.append(f"- gold_fields: **{gold_fields}**")
    lines.append(f"- db_runs_total: **{total_runs}**")
    lines.append(f"- db_prompt_families: **{prompt_families}**")
    lines.append(f"- official_gradeable_runs: **{gradeable}**")
    lines.append(f"- excluded_runs: **{excluded}**")
    lines.append("")
    lines.append("## Gold-normalized consistency")
    lines.append(f"- scenario IDs missing from gold_normalized files: {len(missing_norm)}")
    if missing_norm:
        lines.extend([f"  - `{x}`" for x in missing_norm])
    lines.append(f"- extra gold_normalized IDs outside official scenarios: {len(extra_norm)}")
    if extra_norm:
        lines.extend([f"  - `{x}`" for x in extra_norm])
    lines.append("")
    lines.append("## Runs by scenario")
    for sid, n in by_scenario:
        lines.append(f"- `{sid}`: {n}")
    lines.append("")
    lines.append("## Excluded runs")
    if excluded_rows:
        for run_id, model_name, detail in excluded_rows:
            lines.append(f"- run_id={run_id}, model=`{model_name}`, reason=`OUT_OF_BENCHMARK`, detail={detail!r}")
    else:
        lines.append("- none")
    lines.append("")

    with open(audit_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default="learning.db")
    ap.add_argument("--scenarios", required=True, help="Path to the extracted 'Scenarios to Run' directory")
    ap.add_argument("--benchmark-id", default=DEFAULT_BENCHMARK_ID)
    ap.add_argument("--audit", default="official_benchmark_audit.md")
    args = ap.parse_args()

    scenarios = load_scenarios(args.scenarios)
    if not scenarios:
        raise SystemExit(f"No enabled scenarios found in {args.scenarios!r}")

    gold_norm = load_gold_normalized(args.scenarios)

    con = sqlite3.connect(args.db)
    try:
        ensure_schema(con)
        import_scenarios(con, scenarios, gold_norm, args.benchmark_id)
        match_info = match_runs(con, scenarios)
        con.commit()
        write_audit(args.audit, con, scenarios, gold_norm, args.benchmark_id, match_info)
    finally:
        con.close()

    print(f"Imported benchmark {args.benchmark_id}: {len(scenarios)} scenarios")
    print(f"Matched runs: {len(match_info['matched'])}")
    print(f"Excluded runs: {len(match_info['unmatched'])}")
    print(f"Wrote audit: {args.audit}")


if __name__ == "__main__":
    main()
