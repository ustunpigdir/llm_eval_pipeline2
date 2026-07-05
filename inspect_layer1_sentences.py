import sqlite3
from splitter import make_nlp

conn = sqlite3.connect("learning.db")
cursor = conn.cursor()

cursor.execute("""
SELECT id, model_name, normalized_answer
FROM questions
WHERE normalized_answer IS NOT NULL AND normalized_answer != ''
LIMIT 5
""")
rows = cursor.fetchall()

nlp = make_nlp()

for row_id, model_name, normalized_answer in rows:
    print("ID:", row_id)
    print("Model:", model_name)
    print("Preview:", normalized_answer[:200])
    print("Sentences:")
    for index, sentence in enumerate(nlp(normalized_answer).sents, start=1):
        print(f"{index}. {sentence.text.strip()}")
    print("---")

conn.close()
