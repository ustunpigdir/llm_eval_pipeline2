import re
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "learning.db"


def shorten(text, limit=300):
    if text is None:
        return ""
    text = " ".join(str(text).split())
    if len(text) <= limit:
        return text
    return text[:limit] + "..."


def extract_math_spans(text):
    spans = []
    display_ranges = []

    for pattern in [r"\\\[(.*?)\\\]", r"\$\$(.*?)\$\$"]:
        for match in re.finditer(pattern, text, re.DOTALL):
            start, end = match.span()
            display_ranges.append((start, end))
            spans.append(("display_math", start, end, match.group(0)))

    def inside_display(start, end):
        return any(s <= start and end <= e for s, e in display_ranges)

    for match in re.finditer(r"\$([^$]+)\$", text):
        start, end = match.span()
        if not inside_display(start, end):
            spans.append(("inline_math", start, end, match.group(0)))

    for match in re.finditer(r"\\begin\{([^}]+)\}(.*?)\\end\{\1\}", text, re.DOTALL):
        start, end = match.span()
        if not inside_display(start, end):
            spans.append(("environment", start, end, match.group(0)))

    spans.sort(key=lambda item: item[1])
    return spans


def main():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, model_name, answer
        FROM questions
        WHERE answer IS NOT NULL AND answer != ''
        LIMIT 5
        """
    )
    rows = cursor.fetchall()

    for row in rows:
        print("ID:", row["id"])
        print("Model:", row["model_name"])
        spans = extract_math_spans(row["answer"])
        for index, (span_type, start, end, span_text) in enumerate(spans, start=1):
            print(f"Span {index}: type={span_type} range=({start},{end}) text={shorten(span_text)}")
        print("---")

    conn.close()


if __name__ == "__main__":
    main()
