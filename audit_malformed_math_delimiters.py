import csv
import re
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "learning.db"
ROOT = Path(__file__).resolve().parent
MANIFEST_PATH = ROOT / "raw_answers_md" / "manifest.csv"
EXPORT_DIR = ROOT / "raw_answers_md"


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


def shorten(text, limit=1000):
    if text is None:
        return ""
    if len(text) <= limit:
        return text
    return text[:limit] + "..."


def extract_math_span_count(cursor, run_id):
    cursor.execute("SELECT COUNT(*) FROM extracted_math_spans WHERE run_id = ?", (run_id,))
    return cursor.fetchone()[0]


def main():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    manifest = load_manifest()
    rows = [row for row in manifest.values() if row.get("md_path")]

    odd_single_dollar = 0
    unmatched_bracket_display = 0
    unmatched_paren_inline = 0
    unmatched_environment = 0
    zero_span_with_markers = 0
    suspicious_short = 0
    suspicious_runs = []

    for row in rows:
        run_id = int(row["run_id"])
        md_path = (EXPORT_DIR / row["md_path"]).resolve()
        if not md_path.exists():
            continue
        content = md_path.read_text(encoding="utf-8")
        char_len = len(content)
        counts = count_delimiters(content)

        issues = []
        if counts["single_dollar_count"] % 2 == 1:
            issues.append("odd_single_dollar")
            odd_single_dollar += 1
        if counts["bracket_open"] != counts["bracket_close"]:
            issues.append("unmatched_bracket_display")
            unmatched_bracket_display += 1
        if counts["paren_open"] != counts["paren_close"]:
            issues.append("unmatched_paren_inline")
            unmatched_paren_inline += 1
        if counts["begin_count"] != counts["end_count"]:
            issues.append("unmatched_environment")
            unmatched_environment += 1

        has_markers = any(
            [counts["single_dollar_count"] > 0, counts["double_dollar_count"] > 0, counts["bracket_open"] > 0, counts["paren_open"] > 0, counts["begin_count"] > 0]
        )
        span_count = extract_math_span_count(cursor, run_id)
        if has_markers and span_count == 0:
            issues.append("zero_extracted_spans")
            zero_span_with_markers += 1
        if has_markers and char_len < 300:
            issues.append("suspicious_short")
            suspicious_short += 1

        if issues:
            suspicious_runs.append(
                {
                    "run_id": run_id,
                    "scenario_id": row.get("scenario_id", ""),
                    "model_name": row.get("model_name", ""),
                    "issues": issues,
                    "answer_char_length": char_len,
                    "head": shorten(content),
                    "tail": shorten(content[-1000:] if len(content) > 1000 else content),
                }
            )

    print(f"total_raw_answer_runs={len(rows)}")
    print(f"odd_single_dollar_runs={odd_single_dollar}")
    print(f"unmatched_bracket_display_runs={unmatched_bracket_display}")
    print(f"unmatched_paren_inline_runs={unmatched_paren_inline}")
    print(f"unmatched_environment_runs={unmatched_environment}")
    print(f"raw_math_markers_but_zero_extracted_spans={zero_span_with_markers}")
    print(f"suspicious_short_truncated_math_answers={suspicious_short}")
    print("suspicious_runs")
    for entry in suspicious_runs:
        print(
            f"run_id={entry['run_id']} scenario_id={entry['scenario_id']} model_name={entry['model_name']} issues={','.join(entry['issues'])} answer_char_length={entry['answer_char_length']}"
        )
        print("head=")
        print(entry["head"])
        print("tail=")
        print(entry["tail"])
        print("---")

    conn.close()


if __name__ == "__main__":
    main()
