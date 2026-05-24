import sqlite3

conn = sqlite3.connect("travel.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS saved_places (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    location TEXT,
    description TEXT
)
''')

conn.commit()
conn.close()