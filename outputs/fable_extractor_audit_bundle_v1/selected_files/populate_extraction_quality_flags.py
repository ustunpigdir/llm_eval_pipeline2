import csv
import sqlite3
from collections import Counter
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "learning.db"
ROOT = Path(__file__).resolve().parent
MANIFEST_PATH = ROOT / "raw_answers_md" / "manifest.csv"
EXPORT_DIR = ROOT / "raw_answers_md"

SOURCE = "layer1b_malformed_math_audit"

SEVERITY_BY_FLAG_TYPE = {
    "odd_single_dollar": "warning",
    "unmatched_bracket_display": "warning",
    "unmatched_parenthesis_inline": "warning",
    "unmatched_environment": "warning",
    "math_markers_but_zero_spans": "critical",
    "short_math_heavy_answer": "critical",
}


def load_manifest():
    with MANIFEST_PATH.open("r", encoding="utf-8", newline="") as handle:
        return {int(row["run_id"]): row for row in csv.DictReader(handle)}


def count_delimiters(text):
    dollar_count = text.count("$")
    double_dollar_count = text.count("$$")
    single_dollar_count = dollar_count - 2 * double_dollar_count
    bracket_open = text.count(r"\[")
    bracket_close = text.count(r"\]")
    paren_open = text.count(r"\(")
    paren_close = text.count(r"\)")
    begin_count = text.count(r"\begin")
    end_count = text.count(r"\end")
    return {
        "dollar_count": dollar_count,
        "double_dollar_count": double_dollar_count,
        "single_dollar_count": single_dollar_count,
        "bracket_open": bracket_open,
        "bracket_close": bracket_close,
        "paren_open": paren_open,
        "paren_close": paren_close,
        "begin_count": begin_count,
        "end_count": end_count,
    }


def extract_math_span_count(cursor, run_id):
    cursor.execute("SELECT COUNT(*) FROM extracted_math_spans WHERE run_id = ?", (run_id,))
    return cursor.fetchone()[0]


def build_flags(run_id, counts, char_len, span_count):
    flags = []

    if counts["single_dollar_count"] % 2 == 1:
        flags.append(
            (
                "odd_single_dollar",
                f"single_dollar_count={counts['single_dollar_count']} (odd) dollar_count={counts['dollar_count']} double_dollar_count={counts['double_dollar_count']}",
            )
        )

    if counts["bracket_open"] != counts["bracket_close"]:
        flags.append(
            (
                "unmatched_bracket_display",
                f"bracket_open={counts['bracket_open']} bracket_close={counts['bracket_close']}",
            )
        )

    if counts["paren_open"] != counts["paren_close"]:
        flags.append(
            (
                "unmatched_parenthesis_inline",
                f"paren_open={counts['paren_open']} paren_close={counts['paren_close']}",
            )
        )

    if counts["begin_count"] != counts["end_count"]:
        flags.append(
            (
                "unmatched_environment",
                f"begin_count={counts['begin_count']} end_count={counts['end_count']}",
            )
        )

    has_markers = any(
        [
            counts["single_dollar_count"] > 0,
            counts["double_dollar_count"] > 0,
            counts["bracket_open"] > 0,
            counts["paren_open"] > 0,
            counts["begin_count"] > 0,
        ]
    )

    if has_markers and span_count == 0:
        flags.append(
            (
                "math_markers_but_zero_spans",
                f"answer_char_length={char_len} extracted_span_count={span_count} dollar_count={counts['dollar_count']} bracket_open={counts['bracket_open']} paren_open={counts['paren_open']} begin_count={counts['begin_count']}",
            )
        )

    if has_markers and char_len < 300:
        flags.append(
            (
                "short_math_heavy_answer",
                f"answer_char_length={char_len} extracted_span_count={span_count} dollar_count={counts['dollar_count']}",
            )
        )

    return flags


def main():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    manifest = load_manifest()
    rows = [row for row in manifest.values() if row.get("md_path")]

    total_runs_scanned = 0
    total_flags_inserted = 0
    flag_type_counts = Counter()
    severity_counts = Counter()
    flags_per_run = Counter()
    run_labels = {}

    for row in rows:
        run_id = int(row["run_id"])
        md_path = (EXPORT_DIR / row["md_path"]).resolve()
        if not md_path.exists():
            continue

        total_runs_scanned += 1
        content = md_path.read_text(encoding="utf-8")
        char_len = len(content)
        counts = count_delimiters(content)
        span_count = extract_math_span_count(cursor, run_id)

        flags = build_flags(run_id, counts, char_len, span_count)

        cursor.execute(
            "DELETE FROM extraction_quality_flags WHERE run_id = ? AND source = ?",
            (run_id, SOURCE),
        )

        if flags:
            run_labels[run_id] = (row.get("scenario_id", ""), row.get("model_name", ""))
            for flag_type, detail in flags:
                severity = SEVERITY_BY_FLAG_TYPE[flag_type]
                cursor.execute(
                    """
                    INSERT INTO extraction_quality_flags (run_id, flag_type, severity, source, detail)
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (run_id, flag_type, severity, SOURCE, detail),
                )
                total_flags_inserted += 1
                flag_type_counts[flag_type] += 1
                severity_counts[severity] += 1
                flags_per_run[run_id] += 1

    conn.commit()

    print(f"total_runs_scanned={total_runs_scanned}")
    print(f"total_flags_inserted={total_flags_inserted}")

    print("counts_by_flag_type")
    for flag_type, count in sorted(flag_type_counts.items()):
        print(f"  {flag_type}={count}")

    print("counts_by_severity")
    for severity, count in sorted(severity_counts.items()):
        print(f"  {severity}={count}")

    print("top_20_flagged_runs_by_flag_count")
    for run_id, count in flags_per_run.most_common(20):
        scenario_id, model_name = run_labels.get(run_id, ("", ""))
        print(f"  run_id={run_id} flag_count={count} scenario_id={scenario_id} model_name={model_name}")

    conn.close()


if __name__ == "__main__":
    main()
