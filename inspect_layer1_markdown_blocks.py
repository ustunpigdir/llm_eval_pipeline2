import sqlite3
from pathlib import Path

from markdown_it import MarkdownIt


DB_PATH = Path(__file__).resolve().parent / "learning.db"


def shorten(text, limit=200):
    if not text:
        return ""
    return " ".join(str(text).split())[:limit]


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

    parser = MarkdownIt()

    for row in rows:
        print("ID:", row["id"])
        print("Model:", row["model_name"])
        print("Preview:", shorten(row["answer"]))
        print("Markdown tokens:")
        for token in parser.parse(row["answer"]):
            print(
                f"  type={token.type} tag={token.tag} nesting={token.nesting} content={shorten(token.content)}"
            )
        print("---")

    conn.close()


if __name__ == "__main__":
    main()
