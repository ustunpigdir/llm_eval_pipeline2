import sqlite3
from normalizer import normalize_answer

conn = sqlite3.connect("learning.db")
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM questions")
count = cursor.fetchone()[0]
print(f"Row count: {count}")

cursor.execute("""
SELECT id, model_name, question, answer
FROM questions
LIMIT 3
""")
for row in cursor.fetchall():
    row_id, model_name, question, answer = row
    normalized_answer = normalize_answer(answer)
    print("ID:", row_id)
    print("Model:", model_name)
    print("Question:", question)
    print("Normalized:", normalized_answer)
    print("---")

conn.close()
