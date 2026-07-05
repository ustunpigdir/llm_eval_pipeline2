import re
import shutil
import sqlite3
from datetime import datetime
from pathlib import Path

DRY_RUN = False

ROOT = Path(__file__).resolve().parent
DB_PATH = ROOT / "learning.db"
BACKUP_DIR = ROOT / "backups"

MODEL_COLUMN_CANDIDATES = ["model_name", "model_label", "model", "provider", "model_id"]
ID_COLUMN_CANDIDATES = ["scenario_id", "question_id"]
ANSWER_COLUMN_CANDIDATES = ["answer", "raw_answer", "response"]

QWEN_TERMS = [
    "qwen",
    "Qwen",
    "QWEN",
    "qwen3",
    "qwen3_8b",
    "qwen3.5",
    "qwen3_5",
    "qwen3 8b",
    "qwen3.5 9b",
]

KNOWN_LAYER1B_TABLES = [
    "extracted_markdown_blocks",
    "extracted_math_spans",
    "extraction_quality_flags",
]


def normalize(value):
    if value is None:
        return ""
    return re.sub(r"[^a-z0-9]", "", str(value).lower())


NORMALIZED_QWEN_TERMS = {normalize(term) for term in QWEN_TERMS}


def is_qwen_value(value):
    normalized_value = normalize(value)
    if not normalized_value:
        return False
    if "qwen" in normalized_value:
        return True
    return any(term in normalized_value for term in NORMALIZED_QWEN_TERMS)


def get_table_columns(cursor, table_name):
    return [row[1] for row in cursor.execute(f'PRAGMA table_info("{table_name}")').fetchall()]


def get_tables_with_run_id(cursor):
    tables = [
        row[0]
        for row in cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
        ).fetchall()
    ]
    tables_with_run_id = []
    for table_name in tables:
        columns = get_table_columns(cursor, table_name)
        if "run_id" in columns:
            tables_with_run_id.append((table_name, columns))
    return tables_with_run_id


def find_primary_table(tables_with_run_id):
    for table_name, columns in tables_with_run_id:
        for candidate in MODEL_COLUMN_CANDIDATES:
            if candidate in columns:
                return table_name, candidate, columns
    return None, None, None


def find_first_present(columns, candidates):
    for candidate in candidates:
        if candidate in columns:
            return candidate
    return None


def find_qwen_runs(cursor, primary_table, model_column, primary_columns):
    id_column = find_first_present(primary_columns, ID_COLUMN_CANDIDATES)
    answer_column = find_first_present(primary_columns, ANSWER_COLUMN_CANDIDATES)

    select_parts = ["run_id", model_column]
    select_parts.append(f"{id_column}" if id_column else "NULL")
    select_parts.append(f"LENGTH({answer_column})" if answer_column else "NULL")

    query = f"SELECT {', '.join(select_parts)} FROM \"{primary_table}\""
    rows = cursor.execute(query).fetchall()

    qwen_runs = []
    for run_id, model_value, id_value, answer_length in rows:
        if is_qwen_value(model_value):
            qwen_runs.append(
                {
                    "run_id": run_id,
                    "model_value": model_value,
                    "id_value": id_value,
                    "answer_length": answer_length,
                }
            )
    qwen_runs.sort(key=lambda entry: entry["run_id"])
    return qwen_runs


def create_backup():
    BACKUP_DIR.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = BACKUP_DIR / f"pre_delete_qwen_{timestamp}.db"
    shutil.copy2(DB_PATH, backup_path)
    return backup_path


def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    tables_with_run_id = get_tables_with_run_id(cursor)
    primary_table, model_column, primary_columns = find_primary_table(tables_with_run_id)

    if primary_table is None:
        print("error: could not find a table with run_id and a model-name-like column")
        conn.close()
        return

    dependent_tables = [
        (table_name, columns)
        for table_name, columns in tables_with_run_id
        if table_name != primary_table
    ]
    dependent_table_names = {name for name, _ in dependent_tables}
    for known_table in KNOWN_LAYER1B_TABLES:
        if known_table not in dependent_table_names:
            print(f"warning: known Layer 1B table not found or lacks run_id: {known_table}")

    qwen_runs = find_qwen_runs(cursor, primary_table, model_column, primary_columns)
    qwen_run_ids = [entry["run_id"] for entry in qwen_runs]

    print(f"primary_table={primary_table} model_column={model_column}")
    print(f"qwen_runs_found={len(qwen_runs)}")
    for entry in qwen_runs:
        print(
            f"  run_id={entry['run_id']} model={entry['model_value']} "
            f"scenario/question_id={entry['id_value']} answer_length={entry['answer_length']}"
        )

    if not qwen_run_ids:
        print("no qwen runs found; nothing to do")
        conn.close()
        return

    placeholders = ", ".join("?" for _ in qwen_run_ids)

    if DRY_RUN:
        print("DRY_RUN=True: no changes will be made")
        for table_name, _ in dependent_tables:
            count = cursor.execute(
                f'SELECT COUNT(*) FROM "{table_name}" WHERE run_id IN ({placeholders})',
                qwen_run_ids,
            ).fetchone()[0]
            print(f"  would_delete from {table_name}: {count}")
        print(f"  would_delete from {primary_table}: {len(qwen_run_ids)}")
        conn.close()
        return

    backup_path = create_backup()
    print(f"backup_created={backup_path}")

    deleted_counts = {}
    for table_name, _ in dependent_tables:
        cursor.execute(
            f'DELETE FROM "{table_name}" WHERE run_id IN ({placeholders})', qwen_run_ids
        )
        deleted_counts[table_name] = cursor.rowcount

    cursor.execute(
        f'DELETE FROM "{primary_table}" WHERE run_id IN ({placeholders})', qwen_run_ids
    )
    deleted_from_primary = cursor.rowcount

    conn.commit()

    print(f"qwen_runs_found={len(qwen_runs)}")
    for table_name, count in deleted_counts.items():
        print(f"deleted_from_{table_name}={count}")
    print(f"deleted_from_{primary_table}={deleted_from_primary}")

    remaining_total_runs = cursor.execute(f'SELECT COUNT(*) FROM "{primary_table}"').fetchone()[0]
    print(f"remaining_total_runs={remaining_total_runs}")
    print(f"remaining_raw_answer_runs={remaining_total_runs}")

    for known_table in KNOWN_LAYER1B_TABLES:
        if known_table in dependent_table_names:
            remaining = cursor.execute(f'SELECT COUNT(*) FROM "{known_table}"').fetchone()[0]
            print(f"remaining_{known_table}={remaining}")

    conn.close()


if __name__ == "__main__":
    main()
