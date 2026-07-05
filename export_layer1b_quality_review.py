import csv
import sqlite3
from collections import Counter, defaultdict
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "learning.db"
ROOT = Path(__file__).resolve().parent
MANIFEST_PATH = ROOT / "raw_answers_md" / "manifest.csv"
EXPORT_DIR = ROOT / "raw_answers_md"
OUTPUT_PATH = ROOT / "layer1b_quality_review.md"

HEAD_TAIL_LIMIT = 1200
DISPLAY_SPAN_LIMIT = 5
DISPLAY_SPAN_TEXT_LIMIT = 500
INLINE_SPAN_LIMIT = 5


def load_manifest():
    with MANIFEST_PATH.open("r", encoding="utf-8", newline="") as handle:
        return {int(row["run_id"]): row for row in csv.DictReader(handle)}


def load_flags(cursor):
    cursor.execute(
        "SELECT run_id, flag_type, severity, detail FROM extraction_quality_flags ORDER BY run_id, id"
    )
    flags_by_run = defaultdict(list)
    for run_id, flag_type, severity, detail in cursor.fetchall():
        flags_by_run[run_id].append({"flag_type": flag_type, "severity": severity, "detail": detail})
    return flags_by_run


def load_span_counts(cursor, run_id):
    cursor.execute(
        "SELECT span_type, COUNT(*) FROM extracted_math_spans WHERE run_id = ? GROUP BY span_type",
        (run_id,),
    )
    counts = {row[0]: row[1] for row in cursor.fetchall()}
    total = sum(counts.values())
    return {
        "total": total,
        "display_math": counts.get("display_math", 0),
        "inline_math": counts.get("inline_math", 0),
        "environment": counts.get("environment", 0),
    }


def load_block_count(cursor, run_id):
    cursor.execute("SELECT COUNT(*) FROM extracted_markdown_blocks WHERE run_id = ?", (run_id,))
    return cursor.fetchone()[0]


def load_spans(cursor, run_id, span_type, limit):
    cursor.execute(
        """
        SELECT raw_text FROM extracted_math_spans
        WHERE run_id = ? AND span_type = ?
        ORDER BY span_index
        LIMIT ?
        """,
        (run_id, span_type, limit),
    )
    return [row[0] for row in cursor.fetchall()]


def shorten(text, limit):
    if text is None:
        return ""
    if len(text) <= limit:
        return text
    return text[:limit] + "..."


def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    manifest = load_manifest()
    flags_by_run = load_flags(cursor)

    run_ids = list(flags_by_run.keys())

    run_meta = {}
    for run_id in run_ids:
        flags = flags_by_run[run_id]
        severities = {f["severity"] for f in flags}
        has_critical = "critical" in severities
        run_meta[run_id] = {
            "flags": flags,
            "flag_count": len(flags),
            "has_critical": has_critical,
        }

    ordered_run_ids = sorted(
        run_ids,
        key=lambda rid: (
            0 if run_meta[rid]["has_critical"] else 1,
            -run_meta[rid]["flag_count"],
            rid,
        ),
    )

    severity_counts = Counter()
    flag_type_counts = Counter()
    for flags in flags_by_run.values():
        for flag in flags:
            severity_counts[flag["severity"]] += 1
            flag_type_counts[flag["flag_type"]] += 1

    report_lines = []
    report_lines.append("# Layer 1B Extraction Quality Review")
    report_lines.append("")
    report_lines.append(f"Flagged runs: {len(ordered_run_ids)}")
    report_lines.append("")

    for run_id in ordered_run_ids:
        manifest_row = manifest.get(run_id)
        flags = run_meta[run_id]["flags"]
        span_counts = load_span_counts(cursor, run_id)
        block_count = load_block_count(cursor, run_id)

        content = ""
        if manifest_row and manifest_row.get("md_path"):
            md_path = (EXPORT_DIR / manifest_row["md_path"]).resolve()
            if md_path.exists():
                content = md_path.read_text(encoding="utf-8")

        report_lines.append(f"## run_id={run_id}")
        report_lines.append("")
        report_lines.append(f"- scenario_id: {manifest_row.get('scenario_id', '') if manifest_row else ''}")
        report_lines.append(f"- model_name: {manifest_row.get('model_name', '') if manifest_row else ''}")
        report_lines.append(f"- md_path: {manifest_row.get('md_path', '') if manifest_row else ''}")
        report_lines.append(f"- answer_char_length: {manifest_row.get('answer_char_length', '') if manifest_row else ''}")
        report_lines.append("")

        report_lines.append("### Quality flags")
        report_lines.append("")
        for flag in flags:
            report_lines.append(
                f"- flag_type={flag['flag_type']} severity={flag['severity']} detail={flag['detail']}"
            )
        report_lines.append("")

        report_lines.append("### Extraction counts")
        report_lines.append("")
        report_lines.append(f"- markdown_block_count: {block_count}")
        report_lines.append(f"- total_math_span_count: {span_counts['total']}")
        report_lines.append(f"- display_math_span_count: {span_counts['display_math']}")
        report_lines.append(f"- inline_math_span_count: {span_counts['inline_math']}")
        report_lines.append(f"- environment_span_count: {span_counts['environment']}")
        report_lines.append("")

        report_lines.append(f"### First {HEAD_TAIL_LIMIT} characters")
        report_lines.append("")
        report_lines.append("```")
        report_lines.append(shorten(content, HEAD_TAIL_LIMIT))
        report_lines.append("```")
        report_lines.append("")

        report_lines.append(f"### Last {HEAD_TAIL_LIMIT} characters")
        report_lines.append("")
        report_lines.append("```")
        tail_source = content[-HEAD_TAIL_LIMIT:] if len(content) > HEAD_TAIL_LIMIT else content
        report_lines.append(tail_source)
        report_lines.append("```")
        report_lines.append("")

        display_spans = load_spans(cursor, run_id, "display_math", DISPLAY_SPAN_LIMIT)
        report_lines.append(f"### Display math spans (up to {DISPLAY_SPAN_LIMIT})")
        report_lines.append("")
        if display_spans:
            for index, span_text in enumerate(display_spans, start=1):
                report_lines.append(f"**span {index}:**")
                report_lines.append("```")
                report_lines.append(shorten(span_text, DISPLAY_SPAN_TEXT_LIMIT))
                report_lines.append("```")
        else:
            report_lines.append("(none)")
        report_lines.append("")

        inline_spans = load_spans(cursor, run_id, "inline_math", INLINE_SPAN_LIMIT)
        report_lines.append(f"### Inline math spans (up to {INLINE_SPAN_LIMIT})")
        report_lines.append("")
        if inline_spans:
            for index, span_text in enumerate(inline_spans, start=1):
                report_lines.append(f"**span {index}:** `{span_text}`")
        else:
            report_lines.append("(none)")
        report_lines.append("")

        report_lines.append("---")
        report_lines.append("")

    OUTPUT_PATH.write_text("\n".join(report_lines), encoding="utf-8")

    conn.close()

    print(f"flagged_runs={len(ordered_run_ids)}")
    print(f"output_path={OUTPUT_PATH}")
    print("counts_by_severity")
    for severity, count in sorted(severity_counts.items()):
        print(f"  {severity}={count}")
    print("counts_by_flag_type")
    for flag_type, count in sorted(flag_type_counts.items()):
        print(f"  {flag_type}={count}")


if __name__ == "__main__":
    main()
