import sqlite3

# Connect to DB (creates file if it doesn’t exist)
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    company TEXT,
    salary TEXT,
    location TEXT,
    skills TEXT,
    job_link TEXT UNIQUE
)
""")

conn.commit()
conn.close()
