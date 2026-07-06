import csv
import re
import sqlite3
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DB_PATH = ROOT / "learning.db"
MANIFEST_PATH = ROOT / "raw_answers_md" / "manifest.csv"
MD_OUTPUT_PATH = ROOT / "remaining_layer1b_flag_classification_v3.md"
CSV_OUTPUT_PATH = ROOT / "remaining_layer1b_flag_classification_v3.csv"

RUNS_TABLE = "questions"

FINAL_ANSWER_TEXT_MARKERS = ["FINAL ANSWER", "Final Answer", "final answer"]
FINAL_ANSWER_WINDOW = 2000
KEEP_MIN_ANSWER_LENGTH = 1000
LAST_SNIPPET_LIMIT = 1200
LAST_DISPLAY_SPAN_COUNT = 3
MARKER_NEARBY_WINDOW = 500
POLLUTION_PROSE_LENGTH_THRESHOLD = 500

ALIGNED_BLOCK_PATTERN = re.compile(r"\\begin\{aligned\}.*?\\end\{aligned\}", re.DOTALL)
# Value may follow "&" via "=", "\approxeq", "\approx", "\simeq", "\sim", "\cong", etc., not only a literal "&=".
FIELD_PATTERN = re.compile(r"\\mathrm\{([^}]+)\}\s*&\s*(.*?)(?=\\\\|\\end\{aligned\}|$)", re.DOTALL)
FIELD_VALUE_OPERATOR_PREFIX = re.compile(r"^(\\approxeq|\\approx|\\simeq|\\sim|\\cong|=)\s*")
LOOP_PATTERN = re.compile(r"(.{15,100}?)\1{2,}", re.DOTALL)

META_DISCUSSION_PHRASES = [
    "now we need to",
    "we can output",
    "the template shows",
    "the final answer should be",
    "we need to ensure",
    "the problem says",
    "inside the final answer section",
]

DISPLAY_SPAN_POLLUTION_MARKERS = ["**", "FINAL ANSWER", "The problem says", "Now we need"]

FORMAT_WARNING_KEEP = "FORMAT_WARNING_KEEP"
FORMAT_WARNING_REVIEW = "FORMAT_WARNING_REVIEW"
UNUSABLE = "UNUSABLE"

KEEP_CLEAN = "KEEP_CLEAN"
KEEP_RECOVERABLE_WITH_WARNINGS = "KEEP_RECOVERABLE_WITH_WARNINGS"
REVIEW = "REVIEW"
UNUSABLE_V3 = "UNUSABLE"


def extract_field_value(raw_value):
    return FIELD_VALUE_OPERATOR_PREFIX.sub("", raw_value.strip(), count=1).strip()


def load_manifest_scenarios():
    scenarios = {}
    if MANIFEST_PATH.exists():
        with MANIFEST_PATH.open("r", encoding="utf-8", newline="") as handle:
            for row in csv.DictReader(handle):
                scenarios[int(row["run_id"])] = row.get("scenario_id", "")
    return scenarios


def find_final_answer_blocks(answer_text):
    """Find all \\begin{aligned}...\\end{aligned} candidate final-answer blocks anywhere in the text."""
    blocks = []
    for match in ALIGNED_BLOCK_PATTERN.finditer(answer_text):
        start_char, end_char = match.start(), match.end()
        raw_text = match.group(0)

        fields = FIELD_PATTERN.findall(raw_text)
        field_count = len(fields)
        filled_field_count = sum(1 for _, value in fields if extract_field_value(value))

        has_marker_before = any(
            marker in answer_text[:start_char] for marker in FINAL_ANSWER_TEXT_MARKERS
        )

        blocks.append(
            {
                "start_char": start_char,
                "end_char": end_char,
                "raw_text": raw_text,
                "field_count": field_count,
                "filled_field_count": filled_field_count,
                "complete_aligned_environment": True,
                "has_values_after_equals": field_count > 0 and filled_field_count == field_count,
                "has_final_answer_marker_before": has_marker_before,
            }
        )
    return blocks


def detect_repetition_regions(answer_text):
    """Detect repeated/looping phrases anywhere in the text (typically tail degeneration)."""
    matches = list(LOOP_PATTERN.finditer(answer_text))
    if not matches:
        return None
    return {
        "repetition_start_char": min(m.start() for m in matches),
        "repetition_end_char": max(m.end() for m in matches),
        "repeated_phrase": matches[0].group(1),
    }


def normalized_field_values(block):
    return tuple(extract_field_value(v) for _, v in FIELD_PATTERN.findall(block["raw_text"]))


def compute_display_span_pollution(display_spans, final_block_raw_text):
    """A run's final block is 'polluted' if the Layer 1B display_math span that stored it
    also swallowed large amounts of surrounding prose (a known regex-extraction artifact)."""
    needle = final_block_raw_text.strip()
    if not needle:
        return False
    for span_text in display_spans:
        if needle not in span_text:
            continue
        begin_idx = span_text.find("\\begin{aligned}")
        end_idx = span_text.rfind("\\end{aligned}")
        if begin_idx == -1 or end_idx == -1:
            continue
        prefix = span_text[:begin_idx]
        suffix = span_text[end_idx + len("\\end{aligned}"):]
        if len(prefix) > POLLUTION_PROSE_LENGTH_THRESHOLD or len(suffix) > POLLUTION_PROSE_LENGTH_THRESHOLD:
            return True
        if any(marker in prefix or marker in suffix for marker in DISPLAY_SPAN_POLLUTION_MARKERS):
            return True
    return False


def classify_run_v2(answer, severities):
    blocks = find_final_answer_blocks(answer)
    repetition = detect_repetition_regions(answer)

    valid_blocks = [b for b in blocks if b["field_count"] >= 2]

    if not valid_blocks:
        return UNUSABLE, "no complete final-answer block (\\begin{aligned}...\\end{aligned} with >=2 \\mathrm{} fields) found anywhere in the answer", blocks, repetition, None

    fully_filled_blocks = [b for b in valid_blocks if b["has_values_after_equals"]]
    partially_filled_blocks = [
        b for b in valid_blocks if not b["has_values_after_equals"] and b["filled_field_count"] > 0
    ]

    if not fully_filled_blocks:
        if partially_filled_blocks:
            return FORMAT_WARNING_REVIEW, "final-answer block(s) found but field values are partially blank", blocks, repetition, None
        return UNUSABLE, "final-answer block(s) found but all candidate field values are blank/template-only", blocks, repetition, None

    distinct_value_sets = {normalized_field_values(b) for b in fully_filled_blocks}
    if len(distinct_value_sets) > 1:
        return FORMAT_WARNING_REVIEW, "multiple final-answer blocks found with differing (conflicting) values", blocks, repetition, None

    final_block = max(fully_filled_blocks, key=lambda b: b["end_char"])

    if final_block["has_final_answer_marker_before"]:
        lookback_start = max(0, final_block["start_char"] - MARKER_NEARBY_WINDOW)
        marker_nearby = any(
            marker in answer[lookback_start:final_block["start_char"]] for marker in FINAL_ANSWER_TEXT_MARKERS
        )
        if not marker_nearby:
            return (
                FORMAT_WARNING_REVIEW,
                f"final-answer marker exists but not within {MARKER_NEARBY_WINDOW} chars before the aligned block",
                blocks,
                repetition,
                final_block,
            )

    if repetition is not None and repetition["repetition_start_char"] < final_block["end_char"]:
        return (
            FORMAT_WARNING_REVIEW,
            "repetition/looping region overlaps or occurs before the final-answer block",
            blocks,
            repetition,
            final_block,
        )

    if severities != {"warning"}:
        return (
            FORMAT_WARNING_REVIEW,
            "final-answer block is complete but severities include non-warning flags",
            blocks,
            repetition,
            final_block,
        )

    reason = "complete final-answer block with all fields filled"
    if repetition is not None:
        reason += "; repetition/looping detected but occurs entirely after the final-answer block"
    return FORMAT_WARNING_KEEP, reason, blocks, repetition, final_block


def classify_run_v3(answer, severities, display_spans):
    blocks = find_final_answer_blocks(answer)
    repetition = detect_repetition_regions(answer)

    total_aligned_candidate_count = len(blocks)
    valid_blocks = [b for b in blocks if b["field_count"] >= 2]

    filled_blocks = [b for b in valid_blocks if b["has_values_after_equals"]]
    blank_blocks = [b for b in valid_blocks if b["filled_field_count"] == 0]
    partial_blocks = [
        b for b in valid_blocks if 0 < b["filled_field_count"] < b["field_count"]
    ]

    filled_final_block_count = len(filled_blocks)
    blank_template_block_count = len(blank_blocks)
    distinct_value_sets = {normalized_field_values(b) for b in filled_blocks}
    distinct_filled_final_block_count = len(distinct_value_sets)
    has_multiple_distinct_filled_blocks = distinct_filled_final_block_count > 1

    base_diagnostics = {
        "total_aligned_candidate_count": total_aligned_candidate_count,
        "filled_final_block_count": filled_final_block_count,
        "blank_template_block_count": blank_template_block_count,
        "distinct_filled_final_block_count": distinct_filled_final_block_count,
        "last_filled_final_block_start_char": None,
        "last_filled_final_block_end_char": None,
        "chars_after_last_filled_final_block": None,
        "has_repetition_after_final_block": False,
        "has_repetition_before_or_overlapping_final_block": False,
        "has_blank_template_after_last_filled_block": False,
        "has_multiple_distinct_filled_blocks": has_multiple_distinct_filled_blocks,
        "has_meta_discussion_after_final_block": False,
        "display_span_pollution_near_final": False,
    }

    if not filled_blocks:
        reason = "no complete filled final-answer block found anywhere in the answer"
        if blank_template_block_count > 0:
            reason = "final-answer block(s) found but all are blank/template-only (no filled values)"
        if repetition is not None:
            reason += "; repetition/looping present, preventing resolution"
        return UNUSABLE_V3, reason, blocks, repetition, None, base_diagnostics

    final_block = max(filled_blocks, key=lambda b: b["end_char"])
    chars_after = len(answer) - final_block["end_char"]

    has_repetition_after = repetition is not None and repetition["repetition_start_char"] >= final_block["end_char"]
    has_repetition_before_or_overlap = repetition is not None and repetition["repetition_start_char"] < final_block["end_char"]
    has_blank_after = any(b["start_char"] > final_block["end_char"] for b in blank_blocks)
    has_partial_after = any(b["start_char"] > final_block["end_char"] for b in partial_blocks)

    tail_text_lower = answer[final_block["end_char"]:].lower()
    has_meta_after = any(phrase in tail_text_lower for phrase in META_DISCUSSION_PHRASES)

    pollution = compute_display_span_pollution(display_spans, final_block["raw_text"])

    diagnostics = dict(base_diagnostics)
    diagnostics.update(
        {
            "last_filled_final_block_start_char": final_block["start_char"],
            "last_filled_final_block_end_char": final_block["end_char"],
            "chars_after_last_filled_final_block": chars_after,
            "has_repetition_after_final_block": has_repetition_after,
            "has_repetition_before_or_overlapping_final_block": has_repetition_before_or_overlap,
            "has_blank_template_after_last_filled_block": has_blank_after,
            "has_meta_discussion_after_final_block": has_meta_after,
            "display_span_pollution_near_final": pollution,
        }
    )

    # --- Ambiguity / conflict => REVIEW ---
    if has_multiple_distinct_filled_blocks:
        return (
            REVIEW,
            "multiple filled final-answer blocks exist with differing (conflicting) values",
            blocks,
            repetition,
            final_block,
            diagnostics,
        )

    if partial_blocks:
        return (
            REVIEW,
            "a final-answer block has partially blank field values, creating ambiguity about the true final answer",
            blocks,
            repetition,
            final_block,
            diagnostics,
        )

    if has_repetition_before_or_overlap:
        return (
            REVIEW,
            "repetition/looping region overlaps or occurs before the chosen final-answer block",
            blocks,
            repetition,
            final_block,
            diagnostics,
        )

    if severities != {"warning"}:
        return (
            REVIEW,
            "final-answer block is complete but severities include non-warning flags",
            blocks,
            repetition,
            final_block,
            diagnostics,
        )

    # --- No conflicts: decide CLEAN vs RECOVERABLE_WITH_WARNINGS ---
    pollution_reasons = []
    if filled_final_block_count > 1:
        pollution_reasons.append(f"{filled_final_block_count} repeated identical filled final-answer blocks")
    if has_blank_after:
        pollution_reasons.append("blank template final-answer block(s) appear after the chosen final block")
    if blank_template_block_count > 0 and not has_blank_after:
        pollution_reasons.append(f"{blank_template_block_count} blank template block(s) elsewhere in the answer")
    if has_repetition_after:
        pollution_reasons.append("tail repetition/looping detected after the final-answer block")
    if has_meta_after:
        pollution_reasons.append("meta-discussion about the answer format continues after the final-answer block")
    if pollution:
        pollution_reasons.append("the stored display_math span for this block also swallowed surrounding prose")

    if not pollution_reasons:
        return (
            KEEP_CLEAN,
            "single clean filled final-answer block near the end, no repetition or pollution detected",
            blocks,
            repetition,
            final_block,
            diagnostics,
        )

    reason = "filled final-answer block is recoverable (values: " + ", ".join(normalized_field_values(final_block)) + ") but answer has structural pollution: " + "; ".join(pollution_reasons)
    return (
        KEEP_RECOVERABLE_WITH_WARNINGS,
        reason,
        blocks,
        repetition,
        final_block,
        diagnostics,
    )


def main():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    scenarios = load_manifest_scenarios()

    flags_by_run = defaultdict(list)
    for row in cursor.execute(
        "SELECT run_id, flag_type, severity, detail FROM extraction_quality_flags ORDER BY run_id, id"
    ):
        flags_by_run[row[0]].append({"flag_type": row[1], "severity": row[2], "detail": row[3]})

    flagged_run_ids = sorted(flags_by_run.keys())

    display_spans_by_run = defaultdict(list)
    for row in cursor.execute(
        "SELECT run_id, raw_text FROM extracted_math_spans WHERE span_type = 'display_math' ORDER BY run_id, span_index"
    ):
        display_spans_by_run[row[0]].append(row[1])

    answers_by_run = {}
    for row in cursor.execute(f'SELECT run_id, model_name, answer FROM "{RUNS_TABLE}"'):
        answers_by_run[row[0]] = {"model_name": row[1], "answer": row[2]}

    classification_counts = Counter()
    csv_rows = []
    md_entries = []
    comparison_run_ids = {214, 235, 290, 380, 496, 497, 498}
    comparisons = {}

    for run_id in flagged_run_ids:
        flags = flags_by_run[run_id]
        flag_types = sorted({f["flag_type"] for f in flags})
        severities = {f["severity"] for f in flags}
        severity_list = sorted(severities)

        info = answers_by_run.get(run_id, {})
        model_name = info.get("model_name")
        answer = info.get("answer") or ""
        answer_length = len(answer)
        scenario_id = scenarios.get(run_id, "")
        display_spans = display_spans_by_run.get(run_id, [])

        classification, reason, blocks, repetition, final_block, diagnostics = classify_run_v3(
            answer, severities, display_spans
        )
        classification_counts[classification] += 1

        if run_id in comparison_run_ids:
            v2_classification, _, _, _, _ = classify_run_v2(answer, severities)
            comparisons[run_id] = (v2_classification, classification)

        last_display_spans = display_spans[-LAST_DISPLAY_SPAN_COUNT:]
        tail_answer = answer[-LAST_SNIPPET_LIMIT:] if len(answer) > LAST_SNIPPET_LIMIT else answer

        blank_blocks = [b for b in blocks if b["field_count"] >= 2 and b["filled_field_count"] == 0]

        csv_rows.append(
            {
                "run_id": run_id,
                "model_name": model_name,
                "scenario_id": scenario_id,
                "answer_length": answer_length,
                "flag_types": ";".join(flag_types),
                "severities": ";".join(severity_list),
                "classification": classification,
                "reason": reason,
                "total_aligned_candidate_count": diagnostics["total_aligned_candidate_count"],
                "filled_final_block_count": diagnostics["filled_final_block_count"],
                "blank_template_block_count": diagnostics["blank_template_block_count"],
                "distinct_filled_final_block_count": diagnostics["distinct_filled_final_block_count"],
                "chars_after_last_filled_final_block": diagnostics["chars_after_last_filled_final_block"],
                "has_repetition_after_final_block": diagnostics["has_repetition_after_final_block"],
                "has_blank_template_after_last_filled_block": diagnostics["has_blank_template_after_last_filled_block"],
                "has_multiple_distinct_filled_blocks": diagnostics["has_multiple_distinct_filled_blocks"],
                "has_meta_discussion_after_final_block": diagnostics["has_meta_discussion_after_final_block"],
                "display_span_pollution_near_final": diagnostics["display_span_pollution_near_final"],
            }
        )

        md_entries.append(
            {
                "run_id": run_id,
                "model_name": model_name,
                "scenario_id": scenario_id,
                "answer_length": answer_length,
                "flag_types": flag_types,
                "severity_list": severity_list,
                "classification": classification,
                "reason": reason,
                "diagnostics": diagnostics,
                "tail_answer": tail_answer,
                "last_display_spans": last_display_spans,
                "filled_blocks": [b for b in blocks if b["field_count"] >= 2 and b["has_values_after_equals"]],
                "blank_blocks": blank_blocks,
                "repetition": repetition,
            }
        )

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
                "classification",
                "reason",
                "total_aligned_candidate_count",
                "filled_final_block_count",
                "blank_template_block_count",
                "distinct_filled_final_block_count",
                "chars_after_last_filled_final_block",
                "has_repetition_after_final_block",
                "has_blank_template_after_last_filled_block",
                "has_multiple_distinct_filled_blocks",
                "has_meta_discussion_after_final_block",
                "display_span_pollution_near_final",
            ],
        )
        writer.writeheader()
        writer.writerows(csv_rows)

    report_lines = []
    report_lines.append("# Remaining Layer 1B Flag Classification (v3)")
    report_lines.append("")
    report_lines.append(
        "v3 separates a clean single final-answer block (KEEP_CLEAN) from a recoverable-but-messy "
        "one (KEEP_RECOVERABLE_WITH_WARNINGS: repeated/blank template blocks, tail repetition, "
        "meta-discussion, or polluted display spans, but a single unambiguous value set), from genuine "
        "ambiguity (REVIEW: conflicting values, partial blanks, or repetition overlapping the final "
        "block), from true failures (UNUSABLE: no filled final-answer block anywhere)."
    )
    report_lines.append("")
    report_lines.append(f"Total flagged runs classified: {len(flagged_run_ids)}")
    report_lines.append("")
    report_lines.append("## Counts by classification")
    report_lines.append("")
    for classification in [KEEP_CLEAN, KEEP_RECOVERABLE_WITH_WARNINGS, REVIEW, UNUSABLE_V3]:
        report_lines.append(f"- {classification}: {classification_counts.get(classification, 0)}")
    report_lines.append("")

    report_lines.append("## v2 vs v3 classification for selected runs")
    report_lines.append("")
    for run_id in sorted(comparisons):
        v2_c, v3_c = comparisons[run_id]
        report_lines.append(f"- run_id={run_id}: v2={v2_c} -> v3={v3_c}")
    report_lines.append("")

    for entry in md_entries:
        report_lines.append(f"## run_id={entry['run_id']} — {entry['classification']}")
        report_lines.append("")
        report_lines.append(f"- model_name: {entry['model_name']}")
        report_lines.append(f"- scenario_id: {entry['scenario_id']}")
        report_lines.append(f"- answer_length: {entry['answer_length']}")
        report_lines.append(f"- flag_types: {entry['flag_types']}")
        report_lines.append(f"- severities: {entry['severity_list']}")
        report_lines.append(f"- classification: {entry['classification']}")
        report_lines.append(f"- reason: {entry['reason']}")
        report_lines.append("")

        report_lines.append("**Computed diagnostics:**")
        report_lines.append("")
        for key, value in entry["diagnostics"].items():
            report_lines.append(f"- {key}: {value}")
        report_lines.append("")

        report_lines.append(f"**Last {LAST_SNIPPET_LIMIT} characters of answer:**")
        report_lines.append("")
        report_lines.append("```")
        report_lines.append(entry["tail_answer"])
        report_lines.append("```")
        report_lines.append("")

        report_lines.append(f"**Detected filled final-answer blocks ({len(entry['filled_blocks'])}):**")
        report_lines.append("")
        if entry["filled_blocks"]:
            for index, block in enumerate(entry["filled_blocks"], start=1):
                report_lines.append(
                    f"- filled {index}: start_char={block['start_char']} end_char={block['end_char']} "
                    f"field_count={block['field_count']}"
                )
                report_lines.append("```")
                report_lines.append(block["raw_text"])
                report_lines.append("```")
        else:
            report_lines.append("(none)")
        report_lines.append("")

        report_lines.append(f"**Detected blank template blocks ({len(entry['blank_blocks'])}):**")
        report_lines.append("")
        if entry["blank_blocks"]:
            for index, block in enumerate(entry["blank_blocks"], start=1):
                report_lines.append(
                    f"- blank {index}: start_char={block['start_char']} end_char={block['end_char']}"
                )
                report_lines.append("```")
                report_lines.append(block["raw_text"])
                report_lines.append("```")
        else:
            report_lines.append("(none)")
        report_lines.append("")

        report_lines.append("**Repetition/looping region:**")
        report_lines.append("")
        if entry["repetition"] is not None:
            report_lines.append(
                f"- repetition_start_char={entry['repetition']['repetition_start_char']} "
                f"repetition_end_char={entry['repetition']['repetition_end_char']}"
            )
            report_lines.append(f"- repeated_phrase: `{entry['repetition']['repeated_phrase']}`")
        else:
            report_lines.append("(no repetition/looping detected)")
        report_lines.append("")

        report_lines.append(f"**Last {LAST_DISPLAY_SPAN_COUNT} display_math spans:**")
        report_lines.append("")
        if entry["last_display_spans"]:
            for index, span_text in enumerate(entry["last_display_spans"], start=1):
                report_lines.append(f"span {index}:")
                report_lines.append("```")
                report_lines.append(span_text)
                report_lines.append("```")
        else:
            report_lines.append("(none)")
        report_lines.append("")
        report_lines.append("---")
        report_lines.append("")

    MD_OUTPUT_PATH.write_text("\n".join(report_lines), encoding="utf-8")

    print(f"total_flagged_runs_classified={len(flagged_run_ids)}")
    print("counts_by_classification:")
    for classification in [KEEP_CLEAN, KEEP_RECOVERABLE_WITH_WARNINGS, REVIEW, UNUSABLE_V3]:
        print(f"  {classification}={classification_counts.get(classification, 0)}")
    print(f"markdown_output={MD_OUTPUT_PATH}")
    print(f"csv_output={CSV_OUTPUT_PATH}")
    print("v2_vs_v3_for_selected_runs:")
    for run_id in sorted(comparisons):
        v2_c, v3_c = comparisons[run_id]
        print(f"  run_id={run_id} v2={v2_c} v3={v3_c}")

    conn.close()


if __name__ == "__main__":
    main()
