import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "learning.db"


CREATE_TABLES_SQL = [
    """
    CREATE TABLE IF NOT EXISTS extracted_markdown_blocks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        run_id INTEGER NOT NULL,
        block_index INTEGER NOT NULL,
        block_type TEXT NOT NULL,
        raw_text TEXT NOT NULL,
        normalized_text TEXT,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS extracted_math_spans (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        run_id INTEGER NOT NULL,
        span_index INTEGER NOT NULL,
        span_type TEXT NOT NULL,
        source TEXT NOT NULL,
        start_char INTEGER,
        end_char INTEGER,
        raw_text TEXT NOT NULL,
        normalized_text TEXT,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    )
    """,
]

CREATE_INDEXES_SQL = [
    "CREATE INDEX IF NOT EXISTS idx_extracted_markdown_blocks_run_id ON extracted_markdown_blocks(run_id)",
    "CREATE INDEX IF NOT EXISTS idx_extracted_math_spans_run_id ON extracted_math_spans(run_id)",
    "CREATE INDEX IF NOT EXISTS idx_extracted_math_spans_type ON extracted_math_spans(span_type)",
]


def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for statement in CREATE_TABLES_SQL + CREATE_INDEXES_SQL:
        cursor.execute(statement)

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name IN ('extracted_markdown_blocks', 'extracted_math_spans') ORDER BY name")
    tables = [row[0] for row in cursor.fetchall()]
    print("Created tables:", ", ".join(tables))

    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
