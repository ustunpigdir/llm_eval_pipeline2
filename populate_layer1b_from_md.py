import csv
import re
import sqlite3
from pathlib import Path

from markdown_it import MarkdownIt
from mdit_py_plugins.dollarmath import dollarmath_plugin

ROOT = Path(__file__).resolve().parent
DB_PATH = ROOT / "learning.db"
MANIFEST_PATH = ROOT / "raw_answers_md" / "manifest.csv"
EXPORT_DIR = ROOT / "raw_answers_md"


REQUIRED_TABLES = {"extracted_markdown_blocks", "extracted_math_spans"}


def ensure_tables(conn):
    cursor = conn.cursor()
    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name IN ('extracted_markdown_blocks', 'extracted_math_spans')"
    )
    existing = {row[0] for row in cursor.fetchall()}
    missing = REQUIRED_TABLES - existing
    if missing:
        raise RuntimeError(f"Required tables missing: {sorted(missing)}")


def read_manifest():
    with MANIFEST_PATH.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def extract_display_math(text):
    spans = []
    for pattern in [r"\\\[(.*?)\\\]", r"\$\$(.*?)\$\$"]:
        for match in re.finditer(pattern, text, re.DOTALL):
            spans.append((match.start(), match.end(), match.group(0)))
    return spans


def extract_environments(text, display_ranges):
    spans = []
    pattern = re.compile(r"\\begin\{([^}]+)\}(.*?)\\end\{\1\}", re.DOTALL)
    for match in pattern.finditer(text):
        start, end = match.span()
        if any(s <= start and end <= e for s, e in display_ranges):
            continue
        spans.append((start, end, match.group(0)))
    return spans


def extract_inline_math_tokens(text):
    md = MarkdownIt().use(dollarmath_plugin)
    tokens = md.parse(text)
    spans = []
    for token in tokens:
        for child in getattr(token, "children", []) or []:
            if getattr(child, "type", "") == "math_inline":
                spans.append((None, None, getattr(child, "content", "") or ""))
    return spans


def extract_markdown_blocks(text):
    md = MarkdownIt()
    tokens = md.parse(text)
    blocks = []
    for index, token in enumerate(tokens):
        token_type = getattr(token, "type", "")
        if token_type in {"paragraph_open", "ordered_list_open", "bullet_list_open", "code_block", "fence", "heading_open"}:
            content = getattr(token, "content", "") or ""
            if not content and token_type == "inline":
                content = "".join(getattr(child, "content", "") or "" for child in getattr(token, "children", []) or [])
            blocks.append((index, token_type, content))
    return blocks


def main():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        ensure_tables(conn)
    except Exception as exc:
        print(f"error: {exc}")
        conn.close()
        return

    rows = read_manifest()
    cursor = conn.cursor()

    blocks_inserted = 0
    spans_inserted = 0
    span_counts = {}
    missing_files = 0
    errors = 0

    for row in rows:
        run_id = int(row["run_id"])
        md_path = (EXPORT_DIR / row["md_path"]).resolve()
        if not md_path.exists():
            missing_files += 1
            continue

        try:
            raw_text = md_path.read_text(encoding="utf-8")
            cursor.execute("DELETE FROM extracted_markdown_blocks WHERE run_id = ?", (run_id,))
            cursor.execute("DELETE FROM extracted_math_spans WHERE run_id = ?", (run_id,))

            markdown_blocks = extract_markdown_blocks(raw_text)
            for block_index, block_type, block_text in markdown_blocks:
                cursor.execute(
                    """
                    INSERT INTO extracted_markdown_blocks (run_id, block_index, block_type, raw_text, normalized_text)
                    VALUES (?, ?, ?, ?, NULL)
                    """,
                    (run_id, block_index, block_type, block_text),
                )
                blocks_inserted += 1

            display_spans = extract_display_math(raw_text)
            display_ranges = [(start, end) for start, end, _ in display_spans]
            for span_index, (start, end, span_text) in enumerate(display_spans, start=1):
                cursor.execute(
                    """
                    INSERT INTO extracted_math_spans (run_id, span_index, span_type, source, start_char, end_char, raw_text, normalized_text)
                    VALUES (?, ?, 'display_math', 'regex_display', ?, ?, ?, NULL)
                    """,
                    (run_id, span_index, start, end, span_text),
                )
                spans_inserted += 1
                span_counts["display_math"] = span_counts.get("display_math", 0) + 1

            environment_spans = extract_environments(raw_text, display_ranges)
            for span_index, (start, end, span_text) in enumerate(environment_spans, start=1):
                cursor.execute(
                    """
                    INSERT INTO extracted_math_spans (run_id, span_index, span_type, source, start_char, end_char, raw_text, normalized_text)
                    VALUES (?, ?, 'environment', 'regex_environment', ?, ?, ?, NULL)
                    """,
                    (run_id, len(display_spans) + span_index, start, end, span_text),
                )
                spans_inserted += 1
                span_counts["environment"] = span_counts.get("environment", 0) + 1

            inline_spans = extract_inline_math_tokens(raw_text)
            for span_index, (start, end, span_text) in enumerate(inline_spans, start=1):
                cursor.execute(
                    """
                    INSERT INTO extracted_math_spans (run_id, span_index, span_type, source, start_char, end_char, raw_text, normalized_text)
                    VALUES (?, ?, 'inline_math', 'mdit_child', NULL, NULL, ?, NULL)
                    """,
                    (run_id, len(display_spans) + len(environment_spans) + span_index, span_text),
                )
                spans_inserted += 1
                span_counts["inline_math"] = span_counts.get("inline_math", 0) + 1
        except Exception as exc:
            errors += 1
            print(f"error run_id={run_id} file={md_path.name} {exc}")

    conn.commit()
    conn.close()

    print(f"manifest_rows_processed={len(rows)}")
    print(f"markdown_blocks_inserted={blocks_inserted}")
    print(f"math_spans_inserted={spans_inserted}")
    print(f"span_counts={span_counts}")
    print(f"missing_files={missing_files}")
    print(f"errors={errors}")


if __name__ == "__main__":
    main()
