#!/usr/bin/env python3
"""Export the pre-concept-gate usable benchmark snapshot."""
from __future__ import annotations

import argparse
import csv
import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DB = ROOT / "learning.db"
SNAPSHOT_NAME = "baseline_usable_20260705"
SNAPSHOT_DIR = ROOT / "exports" / SNAPSHOT_NAME
GITHUB_REPO = "https://github.com/ustunpigdir/llm_eval_pipeline2"
SNAPSHOT_STAGE = "post_official_grading_post_structural_quality_pre_concept_gate"

EXPECTED_COUNTS = {
    "official_gradeable_runs": 624,
    "usable_official_gradeable_runs": 617,
    "unusable_official_runs": 7,
    "grading_result_rows_all": 1861,
    "grading_result_rows_usable": 1839,
}
EXPECTED_ALL_VERDICTS = {
    "MATCH": 1012,
    "MISMATCH": 742,
    "NOT_FOUND": 63,
    "REVIEW": 44,
}
EXPECTED_USABLE_VERDICTS = {
    "MATCH": 1012,
    "MISMATCH": 742,
    "NOT_FOUND": 41,
    "REVIEW": 44,
}

CSV_EXPORTS = {
    "usable_grading_summary_overall.csv": "SELECT * FROM usable_grading_summary_overall",
    "usable_grading_summary_by_model.csv": (
        "SELECT * FROM usable_grading_summary_by_model ORDER BY match_rate_found_rows DESC, model_name"
    ),
    "usable_grading_summary_by_scenario.csv": (
        "SELECT * FROM usable_grading_summary_by_scenario ORDER BY scenario_id"
    ),
    "usable_grading_results.csv": "SELECT * FROM usable_grading_results ORDER BY run_id, scenario_id, field_name",
    "official_usable_gradeable_runs.csv": (
        "SELECT * FROM official_usable_gradeable_runs ORDER BY run_id"
    ),
    "unusable_official_runs.csv": "SELECT * FROM unusable_official_runs ORDER BY run_id",
    "all_grading_summary_overall.csv": "SELECT * FROM grading_summary_overall ORDER BY benchmark_id, verdict",
    "all_grading_results_verdict_distribution.csv": (
        "SELECT verdict, COUNT(*) AS count FROM grading_results GROUP BY verdict ORDER BY verdict"
    ),
}

REQUIRED_OBJECTS = [
    "usable_grading_summary_overall",
    "usable_grading_summary_by_model",
    "usable_grading_summary_by_scenario",
    "usable_grading_results",
    "official_usable_gradeable_runs",
    "unusable_official_runs",
    "grading_summary_overall",
    "grading_results",
    "official_gradeable_runs",
    "review_overrides",
]


def connect_readonly(db_path: Path) -> sqlite3.Connection:
    return sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)


def object_exists(con: sqlite3.Connection, name: str) -> bool:
    row = con.execute(
        "SELECT 1 FROM sqlite_master WHERE name = ? AND type IN ('table', 'view')",
        (name,),
    ).fetchone()
    return row is not None


def count(con: sqlite3.Connection, table_or_view: str) -> int:
    return int(con.execute(f'SELECT COUNT(*) FROM "{table_or_view}"').fetchone()[0])


def verdict_distribution(con: sqlite3.Connection, table_or_view: str) -> dict[str, int]:
    return {
        str(verdict): int(row_count)
        for verdict, row_count in con.execute(
            f'SELECT verdict, COUNT(*) FROM "{table_or_view}" GROUP BY verdict'
        )
    }


def rows_for_query(con: sqlite3.Connection, sql: str) -> tuple[list[str], list[sqlite3.Row]]:
    cur = con.execute(sql)
    headers = [description[0] for description in cur.description or []]
    return headers, cur.fetchall()


def write_csv(con: sqlite3.Connection, output_path: Path, sql: str) -> int:
    headers, rows = rows_for_query(con, sql)
    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(headers)
        writer.writerows(rows)
    return len(rows)


def compute_manifest(con: sqlite3.Connection) -> dict[str, Any]:
    manifest = {
        "snapshot_name": SNAPSHOT_NAME,
        "snapshot_stage": SNAPSHOT_STAGE,
        "source_database": "learning.db",
        "github_repo": GITHUB_REPO,
        "created_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "official_gradeable_runs": count(con, "official_gradeable_runs"),
        "usable_official_gradeable_runs": count(con, "official_usable_gradeable_runs"),
        "unusable_official_runs": count(con, "unusable_official_runs"),
        "grading_result_rows_all": count(con, "grading_results"),
        "grading_result_rows_usable": count(con, "usable_grading_results"),
        "all_verdict_distribution": verdict_distribution(con, "grading_results"),
        "usable_verdict_distribution": verdict_distribution(con, "usable_grading_results"),
        "concept_gate_applied": False,
        "review_overrides_applied": False,
    }
    return manifest


def verify_expected(manifest: dict[str, Any]) -> None:
    for key, expected in EXPECTED_COUNTS.items():
        actual = manifest.get(key)
        if actual != expected:
            raise SystemExit(f"Expected {key}={expected}, found {actual}")
    if manifest["all_verdict_distribution"] != EXPECTED_ALL_VERDICTS:
        raise SystemExit(
            "All-results verdict distribution mismatch: "
            + json.dumps(manifest["all_verdict_distribution"], sort_keys=True)
        )
    if manifest["usable_verdict_distribution"] != EXPECTED_USABLE_VERDICTS:
        raise SystemExit(
            "Usable verdict distribution mismatch: "
            + json.dumps(manifest["usable_verdict_distribution"], sort_keys=True)
        )


def write_manifest(manifest: dict[str, Any], output_path: Path) -> None:
    output_path.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def write_snapshot_report(manifest: dict[str, Any], csv_row_counts: dict[str, int], output_path: Path) -> None:
    all_verdicts = manifest["all_verdict_distribution"]
    usable_verdicts = manifest["usable_verdict_distribution"]
    removed_not_found = all_verdicts["NOT_FOUND"] - usable_verdicts["NOT_FOUND"]
    rows_removed = manifest["grading_result_rows_all"] - manifest["grading_result_rows_usable"]

    lines = [
        "# Baseline Usable Snapshot Report",
        "",
        "## Snapshot Purpose",
        "",
        "This snapshot freezes the usable-only official benchmark state before the concept gate is added.",
        "",
        "## Pipeline Stage",
        "",
        f"`{manifest['snapshot_stage']}`",
        "",
        "## Counts",
        "",
        f"- Official gradeable runs: {manifest['official_gradeable_runs']}",
        f"- Usable official gradeable runs: {manifest['usable_official_gradeable_runs']}",
        f"- Unusable official runs: {manifest['unusable_official_runs']}",
        f"- All grading rows: {manifest['grading_result_rows_all']}",
        f"- Usable-only grading rows: {manifest['grading_result_rows_usable']}",
        "",
        "## All-Results Verdict Distribution",
        "",
        f"- MATCH: {all_verdicts['MATCH']}",
        f"- MISMATCH: {all_verdicts['MISMATCH']}",
        f"- NOT_FOUND: {all_verdicts['NOT_FOUND']}",
        f"- REVIEW: {all_verdicts['REVIEW']}",
        "",
        "## Usable-Only Verdict Distribution",
        "",
        f"- MATCH: {usable_verdicts['MATCH']}",
        f"- MISMATCH: {usable_verdicts['MISMATCH']}",
        f"- NOT_FOUND: {usable_verdicts['NOT_FOUND']}",
        f"- REVIEW: {usable_verdicts['REVIEW']}",
        "",
        "## Change From All-Results To Usable-Only",
        "",
        f"- Removed grading rows: {rows_removed}",
        f"- Removed NOT_FOUND rows: {removed_not_found}",
        "- MATCH, MISMATCH, and REVIEW counts are unchanged in this baseline.",
        "",
        "This snapshot is pre-concept-gate. It only excludes structurally unusable runs through run_quality_status.",
        "",
        "## Exported CSV Files",
        "",
    ]
    for filename in sorted(csv_row_counts):
        lines.append(f"- `{filename}` ({csv_row_counts[filename]} rows)")

    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_root_report(manifest: dict[str, Any], csv_row_counts: dict[str, int], output_path: Path) -> None:
    lines = [
        "# Baseline Export Report",
        "",
        f"- Snapshot folder: `exports/{SNAPSHOT_NAME}/`",
        f"- Official gradeable runs: {manifest['official_gradeable_runs']}",
        f"- Usable official gradeable runs: {manifest['usable_official_gradeable_runs']}",
        f"- Unusable official runs: {manifest['unusable_official_runs']}",
        f"- All grading rows: {manifest['grading_result_rows_all']}",
        f"- Usable-only grading rows: {manifest['grading_result_rows_usable']}",
        "- Verification result: PASS",
        "- Later use: compare this baseline snapshot against a post-concept-gate snapshot.",
        "",
        "## Exported Files",
        "",
        "- `manifest.json`",
        "- `BASELINE_USABLE_SNAPSHOT_REPORT.md`",
    ]
    for filename in sorted(csv_row_counts):
        lines.append(f"- `{filename}`")

    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", default=str(DEFAULT_DB))
    parser.add_argument("--out", default=str(SNAPSHOT_DIR))
    args = parser.parse_args()

    db_path = Path(args.db)
    out_dir = Path(args.out)

    con = connect_readonly(db_path)
    con.row_factory = sqlite3.Row
    try:
        missing = [name for name in REQUIRED_OBJECTS if not object_exists(con, name)]
        if missing:
            raise SystemExit("Missing required source object(s): " + ", ".join(missing))

        out_dir.mkdir(parents=True, exist_ok=True)

        csv_row_counts = {
            filename: write_csv(con, out_dir / filename, sql)
            for filename, sql in CSV_EXPORTS.items()
        }
        manifest = compute_manifest(con)
        verify_expected(manifest)
        write_manifest(manifest, out_dir / "manifest.json")
        write_snapshot_report(manifest, csv_row_counts, out_dir / "BASELINE_USABLE_SNAPSHOT_REPORT.md")
        write_root_report(manifest, csv_row_counts, ROOT / "BASELINE_EXPORT_REPORT.md")

        print(f"snapshot_folder={out_dir.relative_to(ROOT)}")
        for filename, row_count in sorted(csv_row_counts.items()):
            print(f"{filename}={row_count}")
        print(f"manifest={out_dir.relative_to(ROOT) / 'manifest.json'}")
        print("verification=PASS")
    finally:
        con.close()


if __name__ == "__main__":
    main()
