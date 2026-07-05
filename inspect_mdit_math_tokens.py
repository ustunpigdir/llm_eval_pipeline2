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


def print_token(token, prefix=""):
    print(
        f"{prefix}type={getattr(token, 'type', '')} tag={getattr(token, 'tag', '')} nesting={getattr(token, 'nesting', '')} content={shorten(getattr(token, 'content', ''))} markup={shorten(getattr(token, 'markup', ''))}"
    )


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

    md = MarkdownIt().use(dollarmath_plugin)

    for row in rows:
        print("ID:", row["id"])
        print("Model:", row["model_name"])
        tokens = md.parse(row["answer"])
        for index, token in enumerate(tokens):
            print(f"Top token {index}:", end=" ")
            print_token(token)
            children = getattr(token, "children", None)
            if children:
                for child_index, child in enumerate(children):
                    print(f"  Child {child_index}:", end=" ")
                    print_token(child, prefix="  ")
        print("---")

    conn.close()


if __name__ == "__main__":
    main()
