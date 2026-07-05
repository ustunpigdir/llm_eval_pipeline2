#!/usr/bin/env python3
"""Compute and store BERTScore for all usable official benchmark runs."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sqlite3
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from statistics import mean, median


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DB = ROOT / "learning.db"
DEFAULT_REFERENCE_DIR = Path("/Users/upigdir/Desktop/Pipeline/Scenarios to Run")
OUTPUT_DIR = ROOT / "outputs" / "bertscore_full_usable_v1"
RUN_NAME = "pre_structured_prompt_usable_full_v1"
SCOPE = "all usable official runs before structured-prompt rerun"
REFERENCE_SOURCE = "worked_solutions_batch1.md through worked_solutions_batch7.md"
CANDIDATE_SOURCE = "questions.answer"
LANG = "en"
EXPECTED_USABLE_RUNS = 617
EXPECTED_SCENARIOS = 32

SCENARIO_HEADING_RE = re.compile(r"^##\s+([A-Z]{2,4}_[A-Z0-9]+_[0-9]{3})\b.*$", re.MULTILINE)
SUBHEADING_RE = re.compile(r"^\*\*(.+?)\*\*\s*$")
USEFUL_HEADING_RE = re.compile(r"(derivation|reasoning checkpoint|checkpoints|reasoning|solution)", re.I)
STOP_HEADING_RE = re.compile(r"(final answer|wrong-answer|wrong answer|fingerprint)", re.I)


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def preview(text: str, limit: int = 260) -> str:
    compact = re.sub(r"\s+", " ", text).strip()
    return compact if len(compact) <= limit else compact[: limit - 3] + "..."


def iter_reference_files(reference_dir: Path) -> list[Path]:
    return sorted(reference_dir.glob("worked_solutions_batch*.md"))


def split_scenario_sections(markdown: str) -> dict[str, str]:
    matches = list(SCENARIO_HEADING_RE.finditer(markdown))
    sections: dict[str, str] = {}
    for idx, match in enumerate(matches):
        scenario_id = match.group(1)
        start = match.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(markdown)
        sections[scenario_id] = markdown[start:end].strip()
    return sections


def extract_reference_text(section: str) -> str:
    lines = section.splitlines()
    selected: list[str] = []
    capture = False
    for line in lines:
        heading_match = SUBHEADING_RE.match(line.strip())
        if heading_match:
            heading = heading_match.group(1)
            if STOP_HEADING_RE.search(heading):
                capture = False
                continue
            capture = bool(USEFUL_HEADING_RE.search(heading))
            if capture:
                selected.append(line)
            continue
        if capture:
            selected.append(line)
    text = "\n".join(selected).strip()
    return text if text else section.strip()


def parse_references(reference_dir: Path) -> tuple[dict[str, str], list[Path]]:
    files = iter_reference_files(reference_dir)
    if len(files) != 7:
        raise SystemExit(f"Expected 7 worked_solutions_batch*.md files, found {len(files)} in {reference_dir}")
    references: dict[str, str] = {}
    for path in files:
        for scenario_id, section in split_scenario_sections(path.read_text(encoding="utf-8")).items():
            references[scenario_id] = extract_reference_text(section)
    if len(references) != EXPECTED_SCENARIOS:
        raise SystemExit(f"Expected {EXPECTED_SCENARIOS} scenario references, found {len(references)}")
    return references, files


def connect(db_path: Path) -> sqlite3.Connection:
    con = sqlite3.connect(db_path)
    con.row_factory = sqlite3.Row
    return con


def ensure_schema(con: sqlite3.Connection) -> None:
    con.executescript(
        """
        CREATE TABLE IF NOT EXISTS bertscore_runs (
            bertscore_run_id INTEGER PRIMARY KEY AUTOINCREMENT,
            run_name TEXT NOT NULL UNIQUE,
            scope TEXT NOT NULL,
            reference_source TEXT NOT NULL,
            candidate_source TEXT NOT NULL,
            bertscore_model TEXT,
            lang TEXT NOT NULL,
            rescale_with_baseline INTEGER NOT NULL,
            n_references INTEGER NOT NULL,
            n_candidates INTEGER NOT NULL,
            notes TEXT,
            created_at TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS bertscore_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            bertscore_run_id INTEGER NOT NULL,
            run_id INTEGER NOT NULL,
            scenario_id TEXT NOT NULL,
            model_name TEXT,
            deterministic_match_count INTEGER,
            deterministic_mismatch_count INTEGER,
            deterministic_not_found_count INTEGER,
            deterministic_review_count INTEGER,
            reference_text_hash TEXT NOT NULL,
            candidate_text_hash TEXT NOT NULL,
            bertscore_precision REAL NOT NULL,
            bertscore_recall REAL NOT NULL,
            bertscore_f1 REAL NOT NULL,
            created_at TEXT NOT NULL,
            FOREIGN KEY(bertscore_run_id) REFERENCES bertscore_runs(bertscore_run_id),
            FOREIGN KEY(run_id) REFERENCES questions(run_id)
        );

        CREATE UNIQUE INDEX IF NOT EXISTS idx_bertscore_results_unique
        ON bertscore_results(bertscore_run_id, run_id);

        DROP VIEW IF EXISTS bertscore_latest_results;
        CREATE VIEW bertscore_latest_results AS
        SELECT br.run_name, br.scope, br.bertscore_model, br.lang, br.rescale_with_baseline, bres.*
        FROM bertscore_results AS bres
        JOIN bertscore_runs AS br
            ON br.bertscore_run_id = bres.bertscore_run_id
        WHERE bres.bertscore_run_id = (
            SELECT bertscore_run_id
            FROM bertscore_runs
            ORDER BY created_at DESC, bertscore_run_id DESC
            LIMIT 1
        );

        DROP VIEW IF EXISTS bertscore_summary_by_model;
        CREATE VIEW bertscore_summary_by_model AS
        SELECT
            model_name,
            COUNT(*) AS n_runs,
            AVG(bertscore_precision) AS mean_precision,
            AVG(bertscore_recall) AS mean_recall,
            AVG(bertscore_f1) AS mean_f1,
            MIN(bertscore_f1) AS min_f1,
            MAX(bertscore_f1) AS max_f1
        FROM bertscore_latest_results
        GROUP BY model_name;

        DROP VIEW IF EXISTS bertscore_summary_by_scenario;
        CREATE VIEW bertscore_summary_by_scenario AS
        SELECT
            scenario_id,
            COUNT(*) AS n_runs,
            AVG(bertscore_precision) AS mean_precision,
            AVG(bertscore_recall) AS mean_recall,
            AVG(bertscore_f1) AS mean_f1,
            MIN(bertscore_f1) AS min_f1,
            MAX(bertscore_f1) AS max_f1
        FROM bertscore_latest_results
        GROUP BY scenario_id;

        DROP VIEW IF EXISTS bertscore_summary_by_deterministic_group;
        CREATE VIEW bertscore_summary_by_deterministic_group AS
        SELECT
            CASE
                WHEN deterministic_match_count > 0
                 AND deterministic_mismatch_count = 0
                 AND deterministic_not_found_count = 0
                 AND deterministic_review_count = 0
                    THEN 'MATCH_HEAVY'
                WHEN deterministic_mismatch_count > 0
                 AND deterministic_mismatch_count >= deterministic_match_count
                 AND deterministic_not_found_count = 0
                    THEN 'MISMATCH_HEAVY'
                WHEN deterministic_not_found_count > 0
                  OR deterministic_review_count > 0
                    THEN 'NOT_FOUND_REVIEW_HEAVY'
                ELSE 'MIXED'
            END AS deterministic_group,
            COUNT(*) AS n_runs,
            AVG(bertscore_precision) AS mean_precision,
            AVG(bertscore_recall) AS mean_recall,
            AVG(bertscore_f1) AS mean_f1,
            MIN(bertscore_f1) AS min_f1,
            MAX(bertscore_f1) AS max_f1
        FROM bertscore_latest_results
        GROUP BY deterministic_group;
        """
    )


def official_scenario_ids(con: sqlite3.Connection) -> set[str]:
    return {
        row["scenario_id"]
        for row in con.execute("SELECT DISTINCT scenario_id FROM official_usable_gradeable_runs ORDER BY scenario_id")
    }


def usable_runs(con: sqlite3.Connection, references: dict[str, str]) -> list[sqlite3.Row]:
    rows = list(
        con.execute(
            """
            WITH verdict_counts AS (
                SELECT
                    ugr.run_id,
                    ugr.scenario_id,
                    ugr.model_name,
                    SUM(CASE WHEN ugr.verdict = 'MATCH' THEN 1 ELSE 0 END) AS match_count,
                    SUM(CASE WHEN ugr.verdict = 'MISMATCH' THEN 1 ELSE 0 END) AS mismatch_count,
                    SUM(CASE WHEN ugr.verdict = 'NOT_FOUND' THEN 1 ELSE 0 END) AS not_found_count,
                    SUM(CASE WHEN ugr.verdict = 'REVIEW' THEN 1 ELSE 0 END) AS review_count
                FROM usable_grading_results AS ugr
                GROUP BY ugr.run_id, ugr.scenario_id, ugr.model_name
            )
            SELECT
                ogr.run_id,
                ogr.scenario_id,
                ogr.model_name,
                q.answer,
                vc.match_count,
                vc.mismatch_count,
                vc.not_found_count,
                vc.review_count
            FROM official_usable_gradeable_runs AS ogr
            JOIN questions AS q
                ON q.run_id = ogr.run_id
            JOIN verdict_counts AS vc
                ON vc.run_id = ogr.run_id
            ORDER BY ogr.run_id
            """
        )
    )
    rows = [row for row in rows if row["scenario_id"] in references]
    if len(rows) != EXPECTED_USABLE_RUNS:
        raise SystemExit(f"Expected {EXPECTED_USABLE_RUNS} usable official runs with references, found {len(rows)}")
    return rows


def existing_run(con: sqlite3.Connection) -> sqlite3.Row | None:
    return con.execute(
        "SELECT * FROM bertscore_runs WHERE run_name = ?",
        (RUN_NAME,),
    ).fetchone()


def existing_result_count(con: sqlite3.Connection, bertscore_run_id: int) -> int:
    return int(
        con.execute(
            "SELECT COUNT(*) FROM bertscore_results WHERE bertscore_run_id = ?",
            (bertscore_run_id,),
        ).fetchone()[0]
    )


def require_bertscore():
    try:
        from bert_score import score
    except ImportError:
        print("Missing dependency: bert-score")
        print("Install with:")
        print("python3 -m pip install bert-score")
        raise SystemExit(2)
    return score


def unpack_bertscore_result(result):
    if len(result) == 3:
        precision, recall, f1 = result
        return precision, recall, f1, "unknown"
    if len(result) == 4:
        precision, recall, f1, model_hash = result
        return precision, recall, f1, model_hash
    raise RuntimeError(f"Unexpected bert_score.score return length: {len(result)}")


def compute_bertscore_batches(
    candidates: list[str],
    references: list[str],
    batch_size: int,
) -> tuple[list[float], list[float], list[float], str, bool, str]:
    score = require_bertscore()
    all_precision: list[float] = []
    all_recall: list[float] = []
    all_f1: list[float] = []
    model_hash = "unknown"
    notes = ""
    rescale = True

    for start in range(0, len(candidates), batch_size):
        end = min(start + batch_size, len(candidates))
        batch_candidates = candidates[start:end]
        batch_references = references[start:end]
        try:
            precision, recall, f1, batch_model_hash = unpack_bertscore_result(
                score(
                    batch_candidates,
                    batch_references,
                    lang=LANG,
                    rescale_with_baseline=True,
                    verbose=False,
                )
            )
        except Exception as exc:
            if start != 0:
                raise
            notes = f"rescale_with_baseline=True failed; retried without baseline: {type(exc).__name__}: {exc}"
            rescale = False
            precision, recall, f1, batch_model_hash = unpack_bertscore_result(
                score(
                    batch_candidates,
                    batch_references,
                    lang=LANG,
                    rescale_with_baseline=False,
                    verbose=False,
                )
            )

        if batch_model_hash != "unknown":
            model_hash = str(batch_model_hash)
        all_precision.extend(float(x) for x in precision.tolist())
        all_recall.extend(float(x) for x in recall.tolist())
        all_f1.extend(float(x) for x in f1.tolist())
        print(f"processed {end}/{len(candidates)}")

    return all_precision, all_recall, all_f1, model_hash, rescale, notes


def create_run_row(
    con: sqlite3.Connection,
    model_hash: str,
    rescale: bool,
    notes: str,
) -> int:
    con.execute(
        """
        INSERT INTO bertscore_runs (
            run_name, scope, reference_source, candidate_source, bertscore_model,
            lang, rescale_with_baseline, n_references, n_candidates, notes, created_at
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            RUN_NAME,
            SCOPE,
            REFERENCE_SOURCE,
            CANDIDATE_SOURCE,
            model_hash,
            LANG,
            1 if rescale else 0,
            EXPECTED_SCENARIOS,
            EXPECTED_USABLE_RUNS,
            notes,
            utc_now(),
        ),
    )
    return int(con.execute("SELECT last_insert_rowid()").fetchone()[0])


def insert_results(
    con: sqlite3.Connection,
    bertscore_run_id: int,
    rows: list[sqlite3.Row],
    references: dict[str, str],
    precision: list[float],
    recall: list[float],
    f1: list[float],
) -> None:
    created_at = utc_now()
    payload = []
    for idx, row in enumerate(rows):
        reference_text = references[row["scenario_id"]]
        candidate_text = row["answer"] or ""
        payload.append(
            (
                bertscore_run_id,
                int(row["run_id"]),
                row["scenario_id"],
                row["model_name"],
                int(row["match_count"] or 0),
                int(row["mismatch_count"] or 0),
                int(row["not_found_count"] or 0),
                int(row["review_count"] or 0),
                sha256_text(reference_text),
                sha256_text(candidate_text),
                precision[idx],
                recall[idx],
                f1[idx],
                created_at,
            )
        )
    con.executemany(
        """
        INSERT INTO bertscore_results (
            bertscore_run_id, run_id, scenario_id, model_name,
            deterministic_match_count, deterministic_mismatch_count,
            deterministic_not_found_count, deterministic_review_count,
            reference_text_hash, candidate_text_hash,
            bertscore_precision, bertscore_recall, bertscore_f1, created_at
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        payload,
    )


def export_query(con: sqlite3.Connection, path: Path, sql: str, params: tuple = ()) -> list[dict[str, object]]:
    cur = con.execute(sql, params)
    headers = [item[0] for item in cur.description or []]
    rows = [dict(row) for row in cur.fetchall()]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)
    return rows


def overall_stats(con: sqlite3.Connection, bertscore_run_id: int) -> dict[str, float]:
    values = [
        float(row["bertscore_f1"])
        for row in con.execute(
            "SELECT bertscore_f1 FROM bertscore_results WHERE bertscore_run_id = ? ORDER BY run_id",
            (bertscore_run_id,),
        )
    ]
    return {
        "mean_f1": mean(values),
        "median_f1": median(values),
        "min_f1": min(values),
        "max_f1": max(values),
    }


def export_outputs(con: sqlite3.Connection, bertscore_run_id: int, references: dict[str, str], output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    result_rows = export_query(
        con,
        output_dir / "bertscore_full_usable_results.csv",
        """
        SELECT
            br.run_name,
            bres.run_id,
            bres.scenario_id,
            bres.model_name,
            bres.deterministic_match_count,
            bres.deterministic_mismatch_count,
            bres.deterministic_not_found_count,
            bres.deterministic_review_count,
            bres.reference_text_hash,
            bres.candidate_text_hash,
            bres.bertscore_precision,
            bres.bertscore_recall,
            bres.bertscore_f1,
            br.bertscore_model,
            br.rescale_with_baseline
        FROM bertscore_results AS bres
        JOIN bertscore_runs AS br
            ON br.bertscore_run_id = bres.bertscore_run_id
        WHERE bres.bertscore_run_id = ?
        ORDER BY bres.run_id
        """,
        (bertscore_run_id,),
    )
    model_rows = export_query(
        con,
        output_dir / "bertscore_summary_by_model.csv",
        "SELECT * FROM bertscore_summary_by_model ORDER BY model_name",
    )
    scenario_rows = export_query(
        con,
        output_dir / "bertscore_summary_by_scenario.csv",
        "SELECT * FROM bertscore_summary_by_scenario ORDER BY scenario_id",
    )
    group_rows = export_query(
        con,
        output_dir / "bertscore_summary_by_deterministic_group.csv",
        "SELECT * FROM bertscore_summary_by_deterministic_group ORDER BY deterministic_group",
    )

    run = con.execute(
        "SELECT * FROM bertscore_runs WHERE bertscore_run_id = ?",
        (bertscore_run_id,),
    ).fetchone()
    manifest = {
        "run_name": RUN_NAME,
        "scope": SCOPE,
        "n_usable_official_runs": int(con.execute("SELECT COUNT(*) FROM official_usable_gradeable_runs").fetchone()[0]),
        "n_bertscore_results": len(result_rows),
        "reference_source": REFERENCE_SOURCE,
        "candidate_source": CANDIDATE_SOURCE,
        "lang": LANG,
        "rescale_with_baseline": bool(run["rescale_with_baseline"]),
        "concept_gate_applied": False,
        "structured_prompt_run": False,
    }
    (output_dir / "manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    stats = overall_stats(con, bertscore_run_id)
    lines = [
        "# Full Usable BERTScore Report",
        "",
        "## Purpose",
        "",
        "Freeze the current natural-answer usable official runs before a future structured-prompt rerun.",
        "",
        "## Counts",
        "",
        f"- Usable official runs: {manifest['n_usable_official_runs']}",
        f"- BERTScore result rows: {manifest['n_bertscore_results']}",
        f"- Scenario references parsed: {len(references)}",
        f"- Rescale with baseline: {manifest['rescale_with_baseline']}",
        "",
        "## Overall F1",
        "",
        f"- Mean: {stats['mean_f1']:.6f}",
        f"- Median: {stats['median_f1']:.6f}",
        f"- Min: {stats['min_f1']:.6f}",
        f"- Max: {stats['max_f1']:.6f}",
        "",
        "## Summary By Deterministic Group",
        "",
        "| group | n_runs | mean_f1 | min_f1 | max_f1 |",
        "| --- | ---: | ---: | ---: | ---: |",
    ]
    for row in group_rows:
        lines.append(
            f"| {row['deterministic_group']} | {row['n_runs']} | "
            f"{float(row['mean_f1']):.6f} | {float(row['min_f1']):.6f} | {float(row['max_f1']):.6f} |"
        )
    lines.extend(
        [
            "",
            "## Outputs",
            "",
            "- `bertscore_full_usable_results.csv`",
            "- `bertscore_summary_by_model.csv`",
            "- `bertscore_summary_by_scenario.csv`",
            "- `bertscore_summary_by_deterministic_group.csv`",
            "- `manifest.json`",
        ]
    )
    (output_dir / "BERTSCORE_FULL_USABLE_REPORT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"exported_results={len(result_rows)}")
    print(f"exported_model_summary_rows={len(model_rows)}")
    print(f"exported_scenario_summary_rows={len(scenario_rows)}")
    print(f"exported_group_summary_rows={len(group_rows)}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", default=str(DEFAULT_DB))
    parser.add_argument("--reference-dir", default=str(DEFAULT_REFERENCE_DIR))
    parser.add_argument("--output-dir", default=str(OUTPUT_DIR))
    parser.add_argument("--batch-size", type=int, default=16)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    references, _ = parse_references(Path(args.reference_dir))
    con = connect(Path(args.db))
    try:
        with con:
            ensure_schema(con)

        official_ids = official_scenario_ids(con)
        missing = sorted(official_ids - set(references))
        extra = sorted(set(references) - official_ids)
        print(f"scenario_references_parsed={len(references)}")
        print("missing_official_references=" + (", ".join(missing) if missing else "none"))
        print("extra_reference_ids=" + (", ".join(extra) if extra else "none"))
        if missing:
            raise SystemExit("Missing official references: " + ", ".join(missing))

        rows = usable_runs(con, references)
        print(f"usable_official_runs={len(rows)}")

        existing = existing_run(con)
        if existing:
            existing_count = existing_result_count(con, int(existing["bertscore_run_id"]))
            if existing_count == EXPECTED_USABLE_RUNS and not args.force:
                print(f"{RUN_NAME} already exists with {existing_count} result rows; not recomputing.")
                export_outputs(con, int(existing["bertscore_run_id"]), references, Path(args.output_dir))
                return
            if not args.force:
                raise SystemExit(
                    f"{RUN_NAME} exists with {existing_count} rows; rerun with --force to replace this run only."
                )
            with con:
                con.execute(
                    "DELETE FROM bertscore_results WHERE bertscore_run_id = ?",
                    (int(existing["bertscore_run_id"]),),
                )
                con.execute("DELETE FROM bertscore_runs WHERE bertscore_run_id = ?", (int(existing["bertscore_run_id"]),))

        candidates = [row["answer"] or "" for row in rows]
        reference_texts = [references[row["scenario_id"]] for row in rows]
        precision, recall, f1, model_hash, rescale, notes = compute_bertscore_batches(
            candidates,
            reference_texts,
            args.batch_size,
        )

        with con:
            bertscore_run_id = create_run_row(con, model_hash, rescale, notes)
            insert_results(con, bertscore_run_id, rows, references, precision, recall, f1)
        print(f"bertscore_run_id={bertscore_run_id}")
        print(f"rescale_with_baseline={rescale}")

        export_outputs(con, bertscore_run_id, references, Path(args.output_dir))
        stats = overall_stats(con, bertscore_run_id)
        print(
            "overall_f1 "
            f"mean={stats['mean_f1']:.6f} median={stats['median_f1']:.6f} "
            f"min={stats['min_f1']:.6f} max={stats['max_f1']:.6f}"
        )
    finally:
        con.close()


if __name__ == "__main__":
    main()
