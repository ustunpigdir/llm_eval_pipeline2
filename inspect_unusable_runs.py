import csv
import sqlite3
from collections import Counter
from pathlib import Path

from classify_remaining_layer1b_flags import find_final_answer_blocks, detect_repetition_regions

ROOT = Path(__file__).resolve().parent
DB_PATH = ROOT / "learning.db"
V3_CSV_PATH = ROOT / "remaining_layer1b_flag_classification_v3.csv"
MD_OUTPUT_PATH = ROOT / "inspect_unusable_runs.md"
CSV_OUTPUT_PATH = ROOT / "inspect_unusable_runs.csv"

RUNS_TABLE = "questions"

TARGET_RUN_IDS = [185, 187, 188, 256, 286, 380, 514]

FIRST_SNIPPET_LIMIT = 1500
MIDDLE_SNIPPET_LIMIT = 1500
LAST_SNIPPET_LIMIT = 2000
LAST_SPAN_COUNT = 10


def load_v3_rows():
    rows = {}
    if V3_CSV_PATH.exists():
        with V3_CSV_PATH.open("r", encoding="utf-8", newline="") as handle:
            for row in csv.DictReader(handle):
                rows[int(row["run_id"])] = row
    return rows


def middle_snippet(text, limit):
    if len(text) <= limit:
        return text
    mid = len(text) // 2
    half = limit // 2
    start = max(0, mid - half)
    end = min(len(text), start + limit)
    return text[start:end]


def main():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    v3_rows = load_v3_rows()

    answers_by_run = {}
    for row in cursor.execute(
        f'SELECT run_id, model_name, answer FROM "{RUNS_TABLE}" WHERE run_id IN ({",".join("?" * len(TARGET_RUN_IDS))})',
        TARGET_RUN_IDS,
    ):
        answers_by_run[row["run_id"]] = {"model_name": row["model_name"], "answer": row["answer"]}

    block_count_by_run = {}
    for row in cursor.execute(
        f'SELECT run_id, COUNT(*) FROM extracted_markdown_blocks WHERE run_id IN ({",".join("?" * len(TARGET_RUN_IDS))}) GROUP BY run_id',
        TARGET_RUN_IDS,
    ):
        block_count_by_run[row[0]] = row[1]

    span_counts_by_run = {}
    display_spans_by_run = {}
    inline_spans_by_run = {}
    for row in cursor.execute(
        f'SELECT run_id, span_type, raw_text FROM extracted_math_spans WHERE run_id IN ({",".join("?" * len(TARGET_RUN_IDS))}) ORDER BY run_id, span_index',
        TARGET_RUN_IDS,
    ):
        run_id, span_type, raw_text = row[0], row[1], row[2]
        span_counts_by_run.setdefault(run_id, Counter())[span_type] += 1
        if span_type == "display_math":
            display_spans_by_run.setdefault(run_id, []).append(raw_text)
        elif span_type == "inline_math":
            inline_spans_by_run.setdefault(run_id, []).append(raw_text)

    flags_by_run = {}
    for row in cursor.execute(
        f'SELECT run_id, flag_type, severity FROM extraction_quality_flags WHERE run_id IN ({",".join("?" * len(TARGET_RUN_IDS))}) ORDER BY run_id, id',
        TARGET_RUN_IDS,
    ):
        flags_by_run.setdefault(row[0], []).append({"flag_type": row[1], "severity": row[2]})

    report_lines = []
    report_lines.append("# Inspection: v3 UNUSABLE Runs")
    report_lines.append("")
    report_lines.append(
        "Human-review export for the 7 runs classified UNUSABLE by "
        "classify_remaining_layer1b_flags.py (v3), before deciding whether to delete, "
        "exclude, or keep them. No database changes were made by this script."
    )
    report_lines.append("")

    csv_rows = []
    answer_lengths = {}

    for run_id in TARGET_RUN_IDS:
        info = answers_by_run.get(run_id, {})
        model_name = info.get("model_name")
        answer = info.get("answer") or ""
        answer_length = len(answer)
        answer_lengths[run_id] = answer_length

        v3_row = v3_rows.get(run_id, {})
        scenario_id = v3_row.get("scenario_id", "")
        v3_classification = v3_row.get("classification", "")
        v3_reason = v3_row.get("reason", "")

        flags = flags_by_run.get(run_id, [])
        flag_types = sorted({f["flag_type"] for f in flags})
        severities = sorted({f["severity"] for f in flags})

        span_counts = span_counts_by_run.get(run_id, Counter())
        display_math_count = span_counts.get("display_math", 0)
        inline_math_count = span_counts.get("inline_math", 0)
        environment_count = span_counts.get("environment", 0)
        block_count = block_count_by_run.get(run_id, 0)

        blocks = find_final_answer_blocks(answer)
        final_candidates = [b for b in blocks if b["field_count"] >= 2]
        filled_blocks = [b for b in final_candidates if b["has_values_after_equals"]]
        blank_blocks = [b for b in final_candidates if b["filled_field_count"] == 0]
        repetition = detect_repetition_regions(answer)

        display_spans = display_spans_by_run.get(run_id, [])
        inline_spans = inline_spans_by_run.get(run_id, [])

        first_snippet = answer[:FIRST_SNIPPET_LIMIT]
        middle_text = middle_snippet(answer, MIDDLE_SNIPPET_LIMIT)
        last_snippet = answer[-LAST_SNIPPET_LIMIT:] if len(answer) > LAST_SNIPPET_LIMIT else answer

        csv_rows.append(
            {
                "run_id": run_id,
                "model_name": model_name,
                "scenario_id": scenario_id,
                "answer_length": answer_length,
                "flag_types": ";".join(flag_types),
                "severities": ";".join(severities),
                "v3_classification": v3_classification,
                "v3_reason": v3_reason,
                "markdown_block_count": block_count,
                "display_math_count": display_math_count,
                "inline_math_count": inline_math_count,
                "environment_count": environment_count,
                "final_answer_candidate_count": len(final_candidates),
                "filled_final_block_count": len(filled_blocks),
                "blank_template_block_count": len(blank_blocks),
                "repetition_detected": repetition is not None,
                "suggested_decision": "CONFIRM_UNUSABLE",
            }
        )

        report_lines.append(f"## run_id={run_id} — {model_name}")
        report_lines.append("")
        report_lines.append("### A. Metadata")
        report_lines.append("")
        report_lines.append(f"- run_id: {run_id}")
        report_lines.append(f"- model_name: {model_name}")
        report_lines.append(f"- scenario_id: {scenario_id}")
        report_lines.append(f"- answer_length: {answer_length}")
        report_lines.append(f"- flag_types: {flag_types}")
        report_lines.append(f"- severities: {severities}")
        report_lines.append(f"- v3_classification: {v3_classification}")
        report_lines.append(f"- v3_reason: {v3_reason}")
        report_lines.append("")

        report_lines.append("### B. Extraction counts")
        report_lines.append("")
        report_lines.append(f"- markdown_block_count: {block_count}")
        report_lines.append(f"- display_math_count: {display_math_count}")
        report_lines.append(f"- inline_math_count: {inline_math_count}")
        report_lines.append(f"- environment_count: {environment_count}")
        report_lines.append(f"- final_answer_candidate_count: {len(final_candidates)}")
        report_lines.append(f"- filled_final_block_count: {len(filled_blocks)}")
        report_lines.append(f"- blank_template_block_count: {len(blank_blocks)}")
        report_lines.append(f"- repetition_detected: {repetition is not None}")
        report_lines.append("")

        report_lines.append("### C. Full raw answer")
        report_lines.append("")
        report_lines.append("```")
        report_lines.append(answer)
        report_lines.append("```")
        report_lines.append("")

        report_lines.append("### D. Review-focused snippets")
        report_lines.append("")
        report_lines.append(f"**First {FIRST_SNIPPET_LIMIT} characters:**")
        report_lines.append("")
        report_lines.append("```")
        report_lines.append(first_snippet)
        report_lines.append("```")
        report_lines.append("")

        report_lines.append(f"**Middle {MIDDLE_SNIPPET_LIMIT} characters (around answer midpoint):**")
        report_lines.append("")
        report_lines.append("```")
        report_lines.append(middle_text)
        report_lines.append("```")
        report_lines.append("")

        report_lines.append(f"**Last {LAST_SNIPPET_LIMIT} characters:**")
        report_lines.append("")
        report_lines.append("```")
        report_lines.append(last_snippet)
        report_lines.append("```")
        report_lines.append("")

        report_lines.append("**Detected repetition regions:**")
        report_lines.append("")
        if repetition is not None:
            report_lines.append(
                f"- repetition_start_char={repetition['repetition_start_char']} "
                f"repetition_end_char={repetition['repetition_end_char']}"
            )
            report_lines.append(f"- repeated_phrase: `{repetition['repeated_phrase']}`")
        else:
            report_lines.append("(none detected)")
        report_lines.append("")

        report_lines.append(f"**Last {LAST_SPAN_COUNT} display_math spans:**")
        report_lines.append("")
        if display_spans:
            for index, span_text in enumerate(display_spans[-LAST_SPAN_COUNT:], start=1):
                report_lines.append(f"span {index}:")
                report_lines.append("```")
                report_lines.append(span_text)
                report_lines.append("```")
        else:
            report_lines.append("(none)")
        report_lines.append("")

        report_lines.append(f"**Last {LAST_SPAN_COUNT} inline_math spans:**")
        report_lines.append("")
        if inline_spans:
            for index, span_text in enumerate(inline_spans[-LAST_SPAN_COUNT:], start=1):
                report_lines.append(f"- span {index}: `{span_text}`")
        else:
            report_lines.append("(none)")
        report_lines.append("")

        report_lines.append("### E. Manual decision")
        report_lines.append("")
        report_lines.append("Manual decision:")
        report_lines.append("")
        report_lines.append("- [ ] CONFIRM_UNUSABLE")
        report_lines.append("- [ ] KEEP_RECOVERABLE")
        report_lines.append("- [ ] NEEDS_SECOND_REVIEW")
        report_lines.append("- [ ] OTHER")
        report_lines.append("")
        report_lines.append("Reviewer notes:")
        report_lines.append("")
        report_lines.append("")
        report_lines.append("")

        report_lines.append("### F. Suggested decision")
        report_lines.append("")
        report_lines.append("Suggested decision: CONFIRM_UNUSABLE")
        report_lines.append("")
        report_lines.append("---")
        report_lines.append("")

    MD_OUTPUT_PATH.write_text("\n".join(report_lines), encoding="utf-8")

    with CSV_OUTPUT_PATH.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "run_id",
                "model_name",
                "scenario_id",
                "answer_length",
                "flag_types",
                "severities",
                "v3_classification",
                "v3_reason",
                "markdown_block_count",
                "display_math_count",
                "inline_math_count",
                "environment_count",
                "final_answer_candidate_count",
                "filled_final_block_count",
                "blank_template_block_count",
                "repetition_detected",
                "suggested_decision",
            ],
        )
        writer.writeheader()
        writer.writerows(csv_rows)

    print(f"markdown_output={MD_OUTPUT_PATH}")
    print(f"csv_output={CSV_OUTPUT_PATH}")
    print(f"total_exported_runs={len(TARGET_RUN_IDS)}")
    print("answer_lengths_by_run_id:")
    for run_id in TARGET_RUN_IDS:
        print(f"  run_id={run_id} answer_length={answer_lengths.get(run_id)}")

    conn.close()


if __name__ == "__main__":
    main()
