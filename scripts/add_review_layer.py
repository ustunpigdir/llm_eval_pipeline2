#!/usr/bin/env python3
"""Add and populate the database-backed review/correction layer."""
from __future__ import annotations

import argparse
import csv
import sqlite3
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DB = ROOT / "learning.db"
DEFAULT_CLASSIFICATION_CSV = ROOT / "remaining_layer1b_flag_classification_v3.csv"
METHOD_VERSION = "review_layer_v1"
REVIEWER = "pipeline_manual_review"

STATUS_TO_USABILITY = {
    "KEEP_CLEAN": "USABLE",
    "KEEP_RECOVERABLE_WITH_WARNINGS": "USABLE",
    "REVIEW": "REVIEW",
    "UNUSABLE": "UNUSABLE",
}

EXPECTED_UNUSABLE_IDS = {185, 187, 188, 256, 286, 380, 514}


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def normalize_header(value: str) -> str:
    return value.strip().lower().replace(" ", "_")


def find_column(headers: list[str], candidates: list[str]) -> str | None:
    normalized = {normalize_header(header): header for header in headers}
    for candidate in candidates:
        if candidate in normalized:
            return normalized[candidate]
    return None


def ensure_schema(con: sqlite3.Connection) -> None:
    con.executescript(
        """
        CREATE TABLE IF NOT EXISTS run_quality_status (
            run_id INTEGER PRIMARY KEY,
            quality_status TEXT NOT NULL,
            usability_status TEXT NOT NULL,
            source_artifact TEXT,
            rationale TEXT,
            reviewer TEXT DEFAULT 'pipeline_manual_review',
            method_version TEXT NOT NULL,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL,
            FOREIGN KEY(run_id) REFERENCES questions(run_id)
        );

        CREATE TABLE IF NOT EXISTS review_overrides (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            run_id INTEGER NOT NULL,
            target_table TEXT NOT NULL,
            target_id TEXT,
            field_name TEXT,
            original_value TEXT,
            override_value TEXT NOT NULL,
            override_reason TEXT NOT NULL,
            reviewer TEXT DEFAULT 'human',
            created_at TEXT NOT NULL,
            FOREIGN KEY(run_id) REFERENCES questions(run_id)
        );

        CREATE TABLE IF NOT EXISTS correction_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            correction_type TEXT NOT NULL,
            affected_layer TEXT NOT NULL,
            affected_table TEXT,
            affected_run_id INTEGER,
            summary TEXT NOT NULL,
            cause TEXT,
            fix TEXT,
            validation TEXT,
            source_artifact TEXT,
            created_at TEXT NOT NULL
        );
        """
    )


def load_classifications(csv_path: Path) -> tuple[list[str], dict[int, dict[str, str]]]:
    with csv_path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        headers = reader.fieldnames or []
        print("classification_csv_headers=" + ", ".join(headers))

        run_id_col = find_column(headers, ["run_id", "run"])
        quality_col = find_column(headers, ["classification", "quality_status", "layer1b_classification"])
        rationale_col = find_column(headers, ["reason", "rationale", "review_reason", "notes"])

        missing = []
        if run_id_col is None:
            missing.append("run_id")
        if quality_col is None:
            missing.append("classification/quality_status")
        if missing:
            raise SystemExit(
                "Cannot populate run_quality_status: missing required CSV column(s): "
                + ", ".join(missing)
            )

        rows: dict[int, dict[str, str]] = {}
        for line_no, row in enumerate(reader, start=2):
            raw_run_id = (row.get(run_id_col) or "").strip()
            if not raw_run_id:
                raise SystemExit(f"Cannot populate run_quality_status: blank run_id at CSV line {line_no}")
            try:
                run_id = int(raw_run_id)
            except ValueError as exc:
                raise SystemExit(f"Cannot populate run_quality_status: invalid run_id {raw_run_id!r}") from exc

            quality_status = (row.get(quality_col) or "").strip()
            if quality_status not in STATUS_TO_USABILITY:
                raise SystemExit(
                    "Cannot populate run_quality_status: unsupported classification "
                    f"{quality_status!r} for run_id={run_id}"
                )

            rows[run_id] = {
                "quality_status": quality_status,
                "usability_status": STATUS_TO_USABILITY[quality_status],
                "rationale": (row.get(rationale_col) or "").strip() if rationale_col else None,
            }

    return headers, rows


def upsert_status(
    con: sqlite3.Connection,
    run_id: int,
    quality_status: str,
    usability_status: str,
    source_artifact: str | None,
    rationale: str | None,
    now: str,
) -> None:
    con.execute(
        """
        INSERT INTO run_quality_status (
            run_id,
            quality_status,
            usability_status,
            source_artifact,
            rationale,
            reviewer,
            method_version,
            created_at,
            updated_at
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(run_id) DO UPDATE SET
            quality_status = excluded.quality_status,
            usability_status = excluded.usability_status,
            source_artifact = excluded.source_artifact,
            rationale = excluded.rationale,
            reviewer = excluded.reviewer,
            method_version = excluded.method_version,
            updated_at = excluded.updated_at
        """,
        (
            run_id,
            quality_status,
            usability_status,
            source_artifact,
            rationale,
            REVIEWER,
            METHOD_VERSION,
            now,
            now,
        ),
    )


def populate_run_quality_status(con: sqlite3.Connection, csv_path: Path) -> None:
    if not csv_path.exists():
        raise SystemExit(f"Cannot populate run_quality_status: classification CSV not found: {csv_path}")

    _, classifications = load_classifications(csv_path)
    all_run_ids = {
        int(row[0])
        for row in con.execute("SELECT run_id FROM questions WHERE run_id IS NOT NULL ORDER BY run_id")
    }
    flagged_run_ids = {
        int(row[0])
        for row in con.execute("SELECT DISTINCT run_id FROM extraction_quality_flags ORDER BY run_id")
    }
    classified_run_ids = set(classifications)

    unclassified_flagged = flagged_run_ids - classified_run_ids
    if unclassified_flagged:
        raise SystemExit(
            "Cannot populate run_quality_status: flagged run(s) have no Layer 1B classification: "
            + ", ".join(str(run_id) for run_id in sorted(unclassified_flagged))
        )

    unknown_classified = classified_run_ids - all_run_ids
    if unknown_classified:
        raise SystemExit(
            "Cannot populate run_quality_status: classification CSV contains unknown run_id(s): "
            + ", ".join(str(run_id) for run_id in sorted(unknown_classified))
        )

    now = utc_now()
    source_artifact = csv_path.name
    for run_id, status in sorted(classifications.items()):
        upsert_status(
            con,
            run_id,
            status["quality_status"],
            status["usability_status"],
            source_artifact,
            status["rationale"],
            now,
        )

    default_run_ids = all_run_ids - classified_run_ids - flagged_run_ids
    for run_id in sorted(default_run_ids):
        upsert_status(
            con,
            run_id,
            "KEEP_CLEAN",
            "USABLE",
            "default_no_layer1b_flag",
            "No Layer 1B quality flag and no explicit classification artifact row.",
            now,
        )

    missing_rows = all_run_ids - {
        int(row[0]) for row in con.execute("SELECT run_id FROM run_quality_status")
    }
    if missing_rows:
        raise SystemExit(
            "Cannot populate run_quality_status: missing status row(s) after population: "
            + ", ".join(str(run_id) for run_id in sorted(missing_rows))
        )


def insert_correction_log(con: sqlite3.Connection) -> None:
    summary = (
        "Added database-backed review layer tables and populated run_quality_status "
        "from Layer 1B review artifacts."
    )
    existing = con.execute(
        """
        SELECT 1
        FROM correction_log
        WHERE correction_type = ?
          AND affected_layer = ?
          AND affected_table = ?
          AND summary = ?
        LIMIT 1
        """,
        ("schema_addition", "review_layer", "run_quality_status", summary),
    ).fetchone()
    if existing:
        return

    con.execute(
        """
        INSERT INTO correction_log (
            correction_type,
            affected_layer,
            affected_table,
            affected_run_id,
            summary,
            cause,
            fix,
            validation,
            source_artifact,
            created_at
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            "schema_addition",
            "review_layer",
            "run_quality_status",
            None,
            summary,
            "Human review decisions and correction history previously lived only in CSV/Markdown artifacts.",
            "Created run_quality_status, review_overrides, and correction_log tables; populated one status row per run.",
            "verify_review_layer.py checks row coverage, expected unusable runs, and unchanged official grading counts.",
            DEFAULT_CLASSIFICATION_CSV.name,
            utc_now(),
        ),
    )


def print_verification(con: sqlite3.Connection) -> None:
    total = con.execute("SELECT COUNT(*) FROM run_quality_status").fetchone()[0]
    print(f"run_quality_status_rows={total}")
    print("quality_usability_distribution")
    for quality_status, usability_status, count in con.execute(
        """
        SELECT quality_status, usability_status, COUNT(*)
        FROM run_quality_status
        GROUP BY quality_status, usability_status
        ORDER BY quality_status, usability_status
        """
    ):
        print(f"  {quality_status}|{usability_status}|{count}")

    unusable_ids = [
        int(row[0])
        for row in con.execute(
            """
            SELECT run_id
            FROM run_quality_status
            WHERE usability_status = 'UNUSABLE'
            ORDER BY run_id
            """
        )
    ]
    print("unusable_run_ids=" + ", ".join(str(run_id) for run_id in unusable_ids))

    if total != 641:
        raise SystemExit(f"Expected 641 run_quality_status rows, found {total}")
    if set(unusable_ids) != EXPECTED_UNUSABLE_IDS:
        raise SystemExit(
            "Expected unusable run IDs "
            + ", ".join(str(run_id) for run_id in sorted(EXPECTED_UNUSABLE_IDS))
            + "; found "
            + ", ".join(str(run_id) for run_id in unusable_ids)
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", default=str(DEFAULT_DB))
    parser.add_argument("--classification-csv", default=str(DEFAULT_CLASSIFICATION_CSV))
    args = parser.parse_args()

    con = sqlite3.connect(args.db)
    try:
        with con:
            ensure_schema(con)
            populate_run_quality_status(con, Path(args.classification_csv))
            insert_correction_log(con)
        print_verification(con)
    finally:
        con.close()


if __name__ == "__main__":
    main()
