import sqlite3

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nama TEXT NOT NULL,
               email TEXT NOT NULL
               )

''')

conn.commit()
conn.close()