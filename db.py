# database.py
import sqlite3

def setup_database():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            title TEXT,
            author TEXT
        )
    ''')

    conn.commit()
