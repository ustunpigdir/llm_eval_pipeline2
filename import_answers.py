import csv
import sqlite3

conn = sqlite3.connect("learning.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS questions")

cursor.execute("""
CREATE TABLE questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id INTEGER,
    model_name TEXT NOT NULL,
    question TEXT NOT NULL,
    answer TEXT NOT NULL,
    normalized_answer TEXT
)
""")

with open("existing_answers.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for run_id, row in enumerate(reader, start=1):
        cursor.execute(
            """
            INSERT INTO questions (run_id, model_name, question, answer, normalized_answer)
            VALUES (?, ?, ?, ?, ?)
            """,
            (run_id, row["model_label"], row["question"], row["response"], None),
        )

conn.commit()

cursor.execute("""
SELECT run_id, model_name, question, answer
FROM questions
ORDER BY run_id
""")
rows = cursor.fetchall()
for run_id, model_name, question, answer in rows:
    print(run_id, model_name, question, answer)

conn.close()

print(f"Imported {len(rows)} rows")
