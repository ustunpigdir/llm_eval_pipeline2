import re
import sqlite3
from pathlib import Path

from markdown_it import MarkdownIt
from mdit_py_plugins.dollarmath import dollarmath_plugin

DB_PATH = Path(__file__).resolve().parent / "learning.db"


def shorten(text, limit=300):
    if text is None:
        return ""
    text = " ".join(str(text).split())
    if len(text) <= limit:
        return text
    return text[:limit] + "..."


def extract_display_math(text):
    candidates = []
    for pattern in [r"\\\[(.*?)\\\]", r"\$\$(.*?)\$\$"]:
        for match in re.finditer(pattern, text, re.DOTALL):
            candidates.append((match.group(0), match.start(), match.end()))
    return candidates


def extract_inline_math_from_tokens(text):
    md = MarkdownIt().use(dollarmath_plugin)
    tokens = md.parse(text)
    candidates = []
    for token in tokens:
        for child in getattr(token, "children", []) or []:
            if getattr(child, "type", "") == "math_inline":
                candidates.append((getattr(child, "content", "") or "", getattr(child, "markup", "") or ""))
    return candidates


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

        display_candidates = extract_display_math(row["answer"])
        for index, (content, start, end) in enumerate(display_candidates, start=1):
            print(
                f"Candidate {index}: type=display_math source=regex_display range=({start},{end}) content={shorten(content)}"
            )

        inline_candidates = extract_inline_math_from_tokens(row["answer"])
        for index, (content, markup) in enumerate(inline_candidates, start=1):
            print(
                f"Candidate {index}: type=inline_math source=mdit_child content={shorten(content)} markup={shorten(markup)}"
            )

        print("---")

    conn.close()


if __name__ == "__main__":
    main()
