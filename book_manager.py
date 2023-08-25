# book_manager.py
import sqlite3

def add_book(title, author):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute('INSERT INTO books (title, author) VALUES (?, ?)', (title, author))
    conn.commit()
    conn.close()

def list_books():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()

    conn.close()

    return books

def delete_book(book_id):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute('DELETE FROM books WHERE id = ?', (book_id,))
    conn.commit()
    conn.close()
