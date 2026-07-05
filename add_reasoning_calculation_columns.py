import sqlite3

conn = sqlite3.connect("learning.db")
cursor = conn.cursor()

cursor.execute("PRAGMA table_info(questions)")
columns = [row[1] for row in cursor.fetchall()]

if "reasoning_text" not in columns:
    cursor.execute("ALTER TABLE questions ADD COLUMN reasoning_text TEXT")

if "calculation_text" not in columns:
    cursor.execute("ALTER TABLE questions ADD COLUMN calculation_text TEXT")

conn.commit()
conn.close()
