import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "learning.db"

CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS extraction_quality_flags (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id INTEGER NOT NULL,
    flag_type TEXT NOT NULL,
    severity TEXT NOT NULL,
    source TEXT NOT NULL,
    detail TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
)
"""

CREATE_INDEXES_SQL = [
    "CREATE INDEX IF NOT EXISTS idx_extraction_quality_flags_run_id ON extraction_quality_flags(run_id)",
    "CREATE INDEX IF NOT EXISTS idx_extraction_quality_flags_flag_type ON extraction_quality_flags(flag_type)",
    "CREATE INDEX IF NOT EXISTS idx_extraction_quality_flags_severity ON extraction_quality_flags(severity)",
]


def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(CREATE_TABLE_SQL)
    for statement in CREATE_INDEXES_SQL:
        cursor.execute(statement)

    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='extraction_quality_flags'"
    )
    table_exists = cursor.fetchone() is not None

    index_names = [
        row[0]
        for row in cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='index' AND name IN ('idx_extraction_quality_flags_run_id', 'idx_extraction_quality_flags_flag_type', 'idx_extraction_quality_flags_severity') ORDER BY name"
        )
    ]

    print(f"Table exists: {table_exists}")
    print("Indexes present:", ", ".join(index_names) if index_names else "none")

    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
