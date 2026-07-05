import re
import sqlite3
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DB_PATH = ROOT / "learning.db"
OUTPUT_PATH = ROOT / "post_qwen_deletion_review.md"

RUNS_TABLE = "questions"
MODEL_COLUMN_CANDIDATES = ["model_name", "model_label", "model", "provider", "model_id"]

FIRST_SNIPPET_LIMIT = 800
LAST_SNIPPET_LIMIT = 1200
TOP_FLAGGED_RUN_LIMIT = 30
SPAN_SNIPPET_LIMIT = 3
FINAL_ANSWER_WINDOW = 2000
SHORT_ANSWER_THRESHOLD = 500
HARMLESS_MIN_LENGTH = 1000

FINAL_ANSWER_MARKERS = ["FINAL ANSWER", "Final Answer", r"\mathrm{"]


def get_table_columns(cursor, table_name):
    return [row[1] for row in cursor.execute(f'PRAGMA table_info("{table_name}")').fetchall()]


def count_math_markers(text):
    dollar_count = text.count("$")
    double_dollar_count = text.count("$$")
    single_dollar_count = dollar_count - 2 * double_dollar_count
    bracket_open = text.count(r"\[")
    paren_open = text.count(r"\(")
    begin_count = text.count(r"\begin")
    has_markers = any(
        [single_dollar_count > 0, double_dollar_count > 0, bracket_open > 0, paren_open > 0, begin_count > 0]
    )
    return has_markers


def shorten(text, limit):
    if text is None:
        return ""
    if len(text) <= limit:
        return text
    return text[:limit] + "..."


def check_remaining_qwen(cursor):
    columns = get_table_columns(cursor, RUNS_TABLE)
    model_columns = [c for c in MODEL_COLUMN_CANDIDATES if c in columns]
    matches = []
    for column in model_columns:
        rows = cursor.execute(
            f'SELECT run_id, "{column}" FROM "{RUNS_TABLE}" WHERE LOWER("{column}") LIKE \'%qwen%\''
        ).fetchall()
        for run_id, value in rows:
            matches.append((run_id, column, value))
    return matches


def main():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    console_lines = []
    report_lines = []

    def emit(line=""):
        console_lines.append(line)

    # --- Section 1: Qwen removal confirmation ---
    qwen_matches = check_remaining_qwen(cursor)
    emit("=== Qwen removal confirmation ===")
    if qwen_matches:
        for run_id, column, value in qwen_matches:
            emit(f"REMAINING_QWEN_MATCH run_id={run_id} column={column} value={value}")
    else:
        emit("NO_QWEN_RUNS_REMAINING = yes")
    emit()

    # --- Section 2: main counts ---
    total_runs = cursor.execute(f'SELECT COUNT(*) FROM "{RUNS_TABLE}"').fetchone()[0]
    non_empty_answer_run_ids = {
        row[0]
        for row in cursor.execute(
            f'SELECT run_id FROM "{RUNS_TABLE}" WHERE answer IS NOT NULL AND TRIM(answer) != \'\''
        ).fetchall()
    }
    runs_with_non_empty_answers = len(non_empty_answer_run_ids)

    distinct_runs_blocks = cursor.execute(
        "SELECT COUNT(DISTINCT run_id) FROM extracted_markdown_blocks"
    ).fetchone()[0]
    distinct_runs_spans = cursor.execute(
        "SELECT COUNT(DISTINCT run_id) FROM extracted_math_spans"
    ).fetchone()[0]
    distinct_runs_flags = cursor.execute(
        "SELECT COUNT(DISTINCT run_id) FROM extraction_quality_flags"
    ).fetchone()[0]

    total_blocks = cursor.execute("SELECT COUNT(*) FROM extracted_markdown_blocks").fetchone()[0]
    total_spans = cursor.execute("SELECT COUNT(*) FROM extracted_math_spans").fetchone()[0]
    total_flags = cursor.execute("SELECT COUNT(*) FROM extraction_quality_flags").fetchone()[0]

    emit("=== Main counts ===")
    emit(f"total_runs={total_runs}")
    emit(f"runs_with_non_empty_raw_answers={runs_with_non_empty_answers}")
    emit(f"distinct_run_id_in_extracted_markdown_blocks={distinct_runs_blocks}")
    emit(f"distinct_run_id_in_extracted_math_spans={distinct_runs_spans}")
    emit(f"distinct_run_id_in_extraction_quality_flags={distinct_runs_flags}")
    emit(f"total_extracted_markdown_blocks={total_blocks}")
    emit(f"total_extracted_math_spans={total_spans}")
    emit(f"total_extraction_quality_flags={total_flags}")
    emit()

    # --- Section 3: coverage gaps ---
    runs_with_blocks = {
        row[0] for row in cursor.execute("SELECT DISTINCT run_id FROM extracted_markdown_blocks").fetchall()
    }
    runs_with_any_spans = {
        row[0] for row in cursor.execute("SELECT DISTINCT run_id FROM extracted_math_spans").fetchall()
    }
    runs_with_display = {
        row[0]
        for row in cursor.execute(
            "SELECT DISTINCT run_id FROM extracted_math_spans WHERE span_type = 'display_math'"
        ).fetchall()
    }
    runs_with_inline = {
        row[0]
        for row in cursor.execute(
            "SELECT DISTINCT run_id FROM extracted_math_spans WHERE span_type = 'inline_math'"
        ).fetchall()
    }

    no_blocks = non_empty_answer_run_ids - runs_with_blocks
    no_spans = non_empty_answer_run_ids - runs_with_any_spans
    no_display = non_empty_answer_run_ids - runs_with_display
    no_inline = non_empty_answer_run_ids - runs_with_inline

    emit("=== Math-span coverage gaps ===")
    emit(f"raw_answer_runs_with_no_markdown_blocks={len(no_blocks)}")
    emit(f"raw_answer_runs_with_no_math_spans={len(no_spans)}")
    emit(f"raw_answer_runs_with_no_display_math_spans={len(no_display)}")
    emit(f"raw_answer_runs_with_no_inline_math_spans={len(no_inline)}")
    emit()

    # --- Section 4: span counts by type ---
    span_type_rows = cursor.execute(
        """
        SELECT span_type, COUNT(*), COUNT(DISTINCT run_id)
        FROM extracted_math_spans
        GROUP BY span_type
        ORDER BY span_type
        """
    ).fetchall()
    emit("=== Span counts by type ===")
    for span_type, row_count, run_count in span_type_rows:
        emit(f"span_type={span_type} total_rows={row_count} distinct_run_count={run_count}")
    emit()

    # --- Preload per-run data needed for sections 5-7 ---
    answers_by_run = {
        row["run_id"]: {"model_name": row["model_name"], "answer": row["answer"]}
        for row in cursor.execute(f'SELECT run_id, model_name, answer FROM "{RUNS_TABLE}"').fetchall()
    }

    block_count_by_run = Counter()
    for row in cursor.execute("SELECT run_id, COUNT(*) FROM extracted_markdown_blocks GROUP BY run_id"):
        block_count_by_run[row[0]] = row[1]

    span_counts_by_run = defaultdict(lambda: Counter())
    for row in cursor.execute("SELECT run_id, span_type, COUNT(*) FROM extracted_math_spans GROUP BY run_id, span_type"):
        span_counts_by_run[row[0]][row[1]] = row[2]

    display_spans_by_run = defaultdict(list)
    for row in cursor.execute(
        "SELECT run_id, raw_text FROM extracted_math_spans WHERE span_type = 'display_math' ORDER BY run_id, span_index"
    ):
        display_spans_by_run[row[0]].append(row[1])

    inline_spans_by_run = defaultdict(list)
    for row in cursor.execute(
        "SELECT run_id, raw_text FROM extracted_math_spans WHERE span_type = 'inline_math' ORDER BY run_id, span_index"
    ):
        inline_spans_by_run[row[0]].append(row[1])

    flags_by_run = defaultdict(list)
    for row in cursor.execute(
        "SELECT run_id, flag_type, severity, detail FROM extraction_quality_flags ORDER BY run_id, id"
    ):
        flags_by_run[row[0]].append({"flag_type": row[1], "severity": row[2], "detail": row[3]})

    # --- Section 5: quality flags summary ---
    flag_type_counts = Counter()
    severity_counts = Counter()
    for flags in flags_by_run.values():
        for flag in flags:
            flag_type_counts[flag["flag_type"]] += 1
            severity_counts[flag["severity"]] += 1

    flagged_run_count = len(flags_by_run)
    top_flagged_run_ids = sorted(
        flags_by_run.keys(), key=lambda rid: (-len(flags_by_run[rid]), rid)
    )[:TOP_FLAGGED_RUN_LIMIT]

    emit("=== Quality flags after Qwen deletion ===")
    emit("counts_by_flag_type:")
    for flag_type, count in sorted(flag_type_counts.items()):
        emit(f"  {flag_type}={count}")
    emit("counts_by_severity:")
    for severity, count in sorted(severity_counts.items()):
        emit(f"  {severity}={count}")
    emit(f"flagged_run_count={flagged_run_count}")
    emit(f"top_{TOP_FLAGGED_RUN_LIMIT}_flagged_runs:")

    def run_span_summary(run_id):
        counts = span_counts_by_run.get(run_id, Counter())
        total = sum(counts.values())
        return {
            "total": total,
            "display_math": counts.get("display_math", 0),
            "inline_math": counts.get("inline_math", 0),
            "environment": counts.get("environment", 0),
        }

    for run_id in top_flagged_run_ids:
        flags = flags_by_run[run_id]
        info = answers_by_run.get(run_id, {})
        answer = info.get("answer") or ""
        span_summary = run_span_summary(run_id)
        flag_types = sorted({f["flag_type"] for f in flags})
        severities = sorted({f["severity"] for f in flags})
        emit(
            f"  run_id={run_id} model={info.get('model_name')} flag_count={len(flags)} "
            f"flag_types={flag_types} severities={severities} answer_length={len(answer)} "
            f"markdown_block_count={block_count_by_run.get(run_id, 0)} "
            f"math_span_count={span_summary['total']} display_math={span_summary['display_math']} "
            f"inline_math={span_summary['inline_math']} environment={span_summary['environment']}"
        )
    emit()

    # --- Section 6: serious remaining flags ---
    serious_run_ids = set()
    for run_id, flags in flags_by_run.items():
        severities = {f["severity"] for f in flags}
        flag_types = {f["flag_type"] for f in flags}
        answer = (answers_by_run.get(run_id, {}) or {}).get("answer") or ""
        if "critical" in severities:
            serious_run_ids.add(run_id)
        if "math_markers_but_zero_spans" in flag_types:
            serious_run_ids.add(run_id)
        if "short_math_heavy_answer" in flag_types:
            serious_run_ids.add(run_id)
        if len(answer) < SHORT_ANSWER_THRESHOLD and len(flags) > 0:
            serious_run_ids.add(run_id)

    for run_id in non_empty_answer_run_ids:
        answer = (answers_by_run.get(run_id, {}) or {}).get("answer") or ""
        span_summary = run_span_summary(run_id)
        if count_math_markers(answer) and span_summary["total"] == 0:
            serious_run_ids.add(run_id)

    emit("=== SERIOUS_REMAINING_FLAGS ===")
    emit(f"serious_remaining_run_count={len(serious_run_ids)}")
    for run_id in sorted(serious_run_ids):
        info = answers_by_run.get(run_id, {})
        emit(f"  run_id={run_id} model={info.get('model_name')}")
    emit()

    # --- Section 7: likely harmless warnings ---
    harmless_run_ids = set()
    for run_id, flags in flags_by_run.items():
        severities = {f["severity"] for f in flags}
        if severities != {"warning"}:
            continue
        span_summary = run_span_summary(run_id)
        if span_summary["display_math"] < 1:
            continue
        answer = (answers_by_run.get(run_id, {}) or {}).get("answer") or ""
        if len(answer) < HARMLESS_MIN_LENGTH:
            continue
        window = answer[-FINAL_ANSWER_WINDOW:] if len(answer) > FINAL_ANSWER_WINDOW else answer
        if not any(marker in window for marker in FINAL_ANSWER_MARKERS):
            continue
        harmless_run_ids.add(run_id)

    emit("=== LIKELY_HARMLESS_WARNINGS ===")
    emit(f"likely_harmless_run_count={len(harmless_run_ids)}")
    for run_id in sorted(harmless_run_ids):
        info = answers_by_run.get(run_id, {})
        emit(f"  run_id={run_id} model={info.get('model_name')}")
    emit()

    for line in console_lines:
        print(line)

    # ================= Markdown report =================
    report_lines.append("# Post Qwen Deletion Review")
    report_lines.append("")

    report_lines.append("## Summary counts")
    report_lines.append("")
    report_lines.append(f"- total_runs: {total_runs}")
    report_lines.append(f"- runs_with_non_empty_raw_answers: {runs_with_non_empty_answers}")
    report_lines.append(f"- distinct_run_id_in_extracted_markdown_blocks: {distinct_runs_blocks}")
    report_lines.append(f"- distinct_run_id_in_extracted_math_spans: {distinct_runs_spans}")
    report_lines.append(f"- distinct_run_id_in_extraction_quality_flags: {distinct_runs_flags}")
    report_lines.append(f"- total_extracted_markdown_blocks: {total_blocks}")
    report_lines.append(f"- total_extracted_math_spans: {total_spans}")
    report_lines.append(f"- total_extraction_quality_flags: {total_flags}")
    report_lines.append("")

    report_lines.append("## Qwen removal confirmation")
    report_lines.append("")
    if qwen_matches:
        for run_id, column, value in qwen_matches:
            report_lines.append(f"- REMAINING_QWEN_MATCH run_id={run_id} column={column} value={value}")
    else:
        report_lines.append("NO_QWEN_RUNS_REMAINING = yes")
    report_lines.append("")

    report_lines.append("## Remaining coverage gaps")
    report_lines.append("")
    report_lines.append(f"- raw_answer_runs_with_no_markdown_blocks: {len(no_blocks)}")
    report_lines.append(f"- raw_answer_runs_with_no_math_spans: {len(no_spans)}")
    report_lines.append(f"- raw_answer_runs_with_no_display_math_spans: {len(no_display)}")
    report_lines.append(f"- raw_answer_runs_with_no_inline_math_spans: {len(no_inline)}")
    report_lines.append("")
    report_lines.append("### Span counts by type")
    report_lines.append("")
    for span_type, row_count, run_count in span_type_rows:
        report_lines.append(f"- {span_type}: total_rows={row_count} distinct_run_count={run_count}")
    report_lines.append("")

    report_lines.append("## Remaining quality flags by type")
    report_lines.append("")
    report_lines.append("### Counts by flag_type")
    for flag_type, count in sorted(flag_type_counts.items()):
        report_lines.append(f"- {flag_type}: {count}")
    report_lines.append("")
    report_lines.append("### Counts by severity")
    for severity, count in sorted(severity_counts.items()):
        report_lines.append(f"- {severity}: {count}")
    report_lines.append("")
    report_lines.append(f"flagged_run_count: {flagged_run_count}")
    report_lines.append("")

    report_lines.append("## Serious remaining flags")
    report_lines.append("")
    report_lines.append(f"serious_remaining_run_count: {len(serious_run_ids)}")
    report_lines.append("")
    for run_id in sorted(serious_run_ids):
        info = answers_by_run.get(run_id, {})
        flags = flags_by_run.get(run_id, [])
        flag_types = sorted({f["flag_type"] for f in flags})
        report_lines.append(f"- run_id={run_id} model={info.get('model_name')} flag_types={flag_types}")
    report_lines.append("")

    report_lines.append("## Likely harmless warnings")
    report_lines.append("")
    report_lines.append(f"likely_harmless_run_count: {len(harmless_run_ids)}")
    report_lines.append("")
    for run_id in sorted(harmless_run_ids):
        info = answers_by_run.get(run_id, {})
        report_lines.append(f"- run_id={run_id} model={info.get('model_name')}")
    report_lines.append("")

    report_lines.append("## Top flagged runs with snippets")
    report_lines.append("")
    for run_id in top_flagged_run_ids:
        flags = flags_by_run[run_id]
        info = answers_by_run.get(run_id, {})
        answer = info.get("answer") or ""
        span_summary = run_span_summary(run_id)
        flag_types = sorted({f["flag_type"] for f in flags})
        severities = sorted({f["severity"] for f in flags})

        report_lines.append(f"### run_id={run_id}")
        report_lines.append("")
        report_lines.append(f"- model_name: {info.get('model_name')}")
        report_lines.append(f"- answer_length: {len(answer)}")
        report_lines.append(f"- markdown_block_count: {block_count_by_run.get(run_id, 0)}")
        report_lines.append(f"- math_span_count: {span_summary['total']}")
        report_lines.append(f"- display_math_count: {span_summary['display_math']}")
        report_lines.append(f"- inline_math_count: {span_summary['inline_math']}")
        report_lines.append(f"- environment_count: {span_summary['environment']}")
        report_lines.append("")

        report_lines.append("**Quality flags:**")
        report_lines.append("")
        for flag in flags:
            report_lines.append(
                f"- flag_type={flag['flag_type']} severity={flag['severity']} detail={flag['detail']}"
            )
        report_lines.append("")

        report_lines.append(f"**First {FIRST_SNIPPET_LIMIT} characters:**")
        report_lines.append("")
        report_lines.append("```")
        report_lines.append(shorten(answer, FIRST_SNIPPET_LIMIT))
        report_lines.append("```")
        report_lines.append("")

        report_lines.append(f"**Last {LAST_SNIPPET_LIMIT} characters:**")
        report_lines.append("")
        report_lines.append("```")
        tail_source = answer[-LAST_SNIPPET_LIMIT:] if len(answer) > LAST_SNIPPET_LIMIT else answer
        report_lines.append(tail_source)
        report_lines.append("```")
        report_lines.append("")

        report_lines.append(f"**Display math spans (up to {SPAN_SNIPPET_LIMIT}):**")
        report_lines.append("")
        display_spans = display_spans_by_run.get(run_id, [])[:SPAN_SNIPPET_LIMIT]
        if display_spans:
            for index, span_text in enumerate(display_spans, start=1):
                report_lines.append(f"span {index}:")
                report_lines.append("```")
                report_lines.append(span_text)
                report_lines.append("```")
        else:
            report_lines.append("(none)")
        report_lines.append("")

        report_lines.append(f"**Inline math spans (up to {SPAN_SNIPPET_LIMIT}):**")
        report_lines.append("")
        inline_spans = inline_spans_by_run.get(run_id, [])[:SPAN_SNIPPET_LIMIT]
        if inline_spans:
            for index, span_text in enumerate(inline_spans, start=1):
                report_lines.append(f"- span {index}: `{span_text}`")
        else:
            report_lines.append("(none)")
        report_lines.append("")
        report_lines.append("---")
        report_lines.append("")

    OUTPUT_PATH.write_text("\n".join(report_lines), encoding="utf-8")
    print(f"markdown_report_written={OUTPUT_PATH}")

    conn.close()


if __name__ == "__main__":
    main()
