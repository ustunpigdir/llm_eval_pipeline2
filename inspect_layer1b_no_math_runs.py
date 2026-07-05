import csv
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "learning.db"
ROOT = Path(__file__).resolve().parent
MANIFEST_PATH = ROOT / "raw_answers_md" / "manifest.csv"
EXPORT_DIR = ROOT / "raw_answers_md"


def load_manifest():
    with MANIFEST_PATH.open("r", encoding="utf-8", newline="") as handle:
        return {int(row["run_id"]): row for row in csv.DictReader(handle)}


def shorten(text, limit=1500):
    if text is None:
        return ""
    text = " ".join(str(text).split())
    if len(text) <= limit:
        return text
    return text[:limit] + "..."


def main():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT DISTINCT run_id FROM questions WHERE answer IS NOT NULL AND answer != '' ORDER BY run_id")
    raw_runs = {row[0] for row in cursor.fetchall()}

    cursor.execute("SELECT DISTINCT run_id FROM extracted_math_spans ORDER BY run_id")
    math_runs = {row[0] for row in cursor.fetchall()}

    missing_runs = sorted(raw_runs - math_runs)
    manifest = load_manifest()

    print(f"runs_with_raw_answers={len(raw_runs)}")
    print(f"runs_with_math_spans={len(math_runs)}")
    print(f"runs_with_raw_answers_but_no_math_spans={len(missing_runs)}")

    for run_id in missing_runs:
        meta = manifest.get(run_id, {})
        md_path = EXPORT_DIR / meta.get("md_path", "")
        content = md_path.read_text(encoding="utf-8") if md_path.exists() else ""
        print(f"run_id={run_id}")
        print(f"scenario_id={meta.get('scenario_id', '')}")
        print(f"model_name={meta.get('model_name', '')}")
        print(f"md_path={meta.get('md_path', '')}")
        print(f"answer_char_length={meta.get('answer_char_length', '')}")
        print("preview=")
        print(shorten(content))
        print("---")

    conn.close()


if __name__ == "__main__":
    main()
