import csv
import hashlib
import sqlite3
from collections import defaultdict
from pathlib import Path
import re

DB_PATH = Path(__file__).resolve().parent / "learning.db"
OUT_DIR = Path(__file__).resolve().parent / "raw_answers_md"
MANIFEST_PATH = OUT_DIR / "manifest.csv"


def safe_slug(value):
    if not value:
        return "unknown"
    value = re.sub(r"[^A-Za-z0-9]+", "_", str(value).strip().lower()).strip("_")
    return value or "unknown"


def export_raw_answers():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT run_id, model_name, question, answer
        FROM questions
        WHERE answer IS NOT NULL AND answer != ''
        ORDER BY run_id, id
        """
    )
    rows = cursor.fetchall()

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    grouped_rows = defaultdict(list)
    for row in rows:
        grouped_rows[row["run_id"]].append(row)

    manifest_rows = []
    for run_id, run_rows in sorted(grouped_rows.items()):
        answers = [row["answer"] for row in run_rows if row["answer"] is not None]
        content = "\n\n".join(answers)

        model_name = run_rows[0]["model_name"] or "unknown"
        model_slug = safe_slug(model_name)
        scenario_slug = "unknown"

        filename = f"run_{run_id}__{scenario_slug}__{model_slug}.md"
        output_path = OUT_DIR / filename

        with output_path.open("w", encoding="utf-8", newline="") as handle:
            handle.write(content)

        digest = hashlib.sha256(content.encode("utf-8")).hexdigest()
        manifest_rows.append(
            {
                "run_id": run_id,
                "scenario_id": scenario_slug,
                "model_name": model_name,
                "md_path": output_path.name,
                "answer_char_length": len(content),
                "answer_sha256": digest,
            }
        )

    with MANIFEST_PATH.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["run_id", "scenario_id", "model_name", "md_path", "answer_char_length", "answer_sha256"],
        )
        writer.writeheader()
        writer.writerows(manifest_rows)

    conn.close()
    return len(rows), len(manifest_rows), str(OUT_DIR), str(MANIFEST_PATH)


def main():
    count, files_written, out_dir, manifest_path = export_raw_answers()
    print(f"raw_answers_found={count}")
    print(f"markdown_files_written={files_written}")
    print(f"output_folder={out_dir}")
    print(f"manifest_path={manifest_path}")


if __name__ == "__main__":
    main()
