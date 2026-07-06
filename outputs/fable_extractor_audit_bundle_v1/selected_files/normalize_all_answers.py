import sqlite3
from normalizer import normalize_answer

conn = sqlite3.connect("learning.db")
cursor = conn.cursor()

cursor.execute("""
SELECT id, answer
FROM questions
WHERE normalized_answer IS NULL OR normalized_answer = ''
""")
rows = cursor.fetchall()

normalized_count = 0
for question_id, answer in rows:
    cleaned_answer = normalize_answer(answer)
    cursor.execute(
        "UPDATE questions SET normalized_answer = ? WHERE id = ?",
        (cleaned_answer, question_id),
    )
    normalized_count += 1

conn.commit()
conn.close()

print(f"Normalized {normalized_count} rows")
