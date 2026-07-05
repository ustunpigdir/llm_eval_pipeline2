import sqlite3
from normalizer import normalize_answer

conn = sqlite3.connect("learning.db")
cursor = conn.cursor()

cursor.execute("""
SELECT id, answer
FROM questions
WHERE normalized_answer IS NULL OR normalized_answer = ''
LIMIT 1
""")
row = cursor.fetchone()

if row is not None:
    question_id, answer = row
    normalized_answer = normalize_answer(answer)
    cursor.execute("""
    UPDATE questions
    SET normalized_answer = ?
    WHERE id = ?
    """, (normalized_answer, question_id))

conn.commit()
conn.close()