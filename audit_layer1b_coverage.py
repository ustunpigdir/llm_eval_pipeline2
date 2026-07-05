import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "learning.db"


def shorten(text, limit=200):
    if text is None:
        return ""
    text = " ".join(str(text).split())
    if len(text) <= limit:
        return text
    return text[:limit] + "..."


def main():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM questions WHERE answer IS NOT NULL AND answer != ''")
    raw_answer_runs = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(DISTINCT run_id) FROM extracted_markdown_blocks")
    markdown_run_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(DISTINCT run_id) FROM extracted_math_spans")
    math_run_count = cursor.fetchone()[0]

    cursor.execute("SELECT span_type, COUNT(*) AS count, COUNT(DISTINCT run_id) AS run_count FROM extracted_math_spans GROUP BY span_type")
    span_stats = cursor.fetchall()

    cursor.execute("SELECT DISTINCT run_id FROM questions WHERE answer IS NOT NULL AND answer != '' ORDER BY run_id")
    raw_runs = {row[0] for row in cursor.fetchall()}

    cursor.execute("SELECT DISTINCT run_id FROM extracted_markdown_blocks")
    markdown_runs = {row[0] for row in cursor.fetchall()}

    cursor.execute("SELECT DISTINCT run_id FROM extracted_math_spans")
    math_runs = {row[0] for row in cursor.fetchall()}

    cursor.execute("SELECT DISTINCT run_id FROM extracted_math_spans WHERE span_type = 'display_math'")
    display_math_runs = {row[0] for row in cursor.fetchall()}

    no_blocks = sorted(raw_runs - markdown_runs)
    no_math = sorted(raw_runs - math_runs)
    no_display = sorted(raw_runs - display_math_runs)

    cursor.execute("""
        SELECT run_id, COUNT(*) AS count
        FROM extracted_math_spans
        GROUP BY run_id
        ORDER BY count DESC, run_id DESC
        LIMIT 20
    """)
    top_math_runs = cursor.fetchall()

    cursor.execute("""
        SELECT run_id, COUNT(*) AS count
        FROM extracted_math_spans
        WHERE span_type = 'display_math'
        GROUP BY run_id
        ORDER BY count DESC, run_id DESC
        LIMIT 20
    """)
    top_display_runs = cursor.fetchall()

    print(f"raw_answer_runs={raw_answer_runs}")
    print(f"markdown_block_runs={markdown_run_count}")
    print(f"math_span_runs={math_run_count}")
    for row in span_stats:
        print(f"span_type={row['span_type']} total_rows={row['count']} distinct_runs={row['run_count']}")

    print("runs_with_raw_answers_but_no_markdown_blocks=" + ",".join(map(str, no_blocks)))
    print("runs_with_raw_answers_but_no_math_spans=" + ",".join(map(str, no_math)))
    print("runs_with_raw_answers_but_no_display_math_spans=" + ",".join(map(str, no_display)))

    print("top_20_runs_by_math_span_count")
    for row in top_math_runs:
        print(f"run_id={row['run_id']} math_span_count={row['count']}")

    print("top_20_runs_by_display_math_span_count")
    for row in top_display_runs:
        print(f"run_id={row['run_id']} display_math_count={row['count']}")

    print("sample_display_math_rows")
    cursor.execute("""
        SELECT run_id, span_type, source, start_char, end_char, raw_text
        FROM extracted_math_spans
        WHERE span_type = 'display_math'
        ORDER BY id
        LIMIT 5
    """)
    for row in cursor.fetchall():
        print(f"run_id={row['run_id']} span_type={row['span_type']} source={row['source']} start_char={row['start_char']} end_char={row['end_char']} raw_text={shorten(row['raw_text'])}")

    print("sample_inline_math_rows")
    cursor.execute("""
        SELECT run_id, span_type, source, start_char, end_char, raw_text
        FROM extracted_math_spans
        WHERE span_type = 'inline_math'
        ORDER BY id
        LIMIT 5
    """)
    for row in cursor.fetchall():
        print(f"run_id={row['run_id']} span_type={row['span_type']} source={row['source']} start_char={row['start_char']} end_char={row['end_char']} raw_text={shorten(row['raw_text'])}")

    print("sample_environment_rows")
    cursor.execute("""
        SELECT run_id, span_type, source, start_char, end_char, raw_text
        FROM extracted_math_spans
        WHERE span_type = 'environment'
        ORDER BY id
        LIMIT 5
    """)
    for row in cursor.fetchall():
        print(f"run_id={row['run_id']} span_type={row['span_type']} source={row['source']} start_char={row['start_char']} end_char={row['end_char']} raw_text={shorten(row['raw_text'])}")

    conn.close()


if __name__ == "__main__":
    main()
