from flask import Flask, render_template, request, redirect
from db import setup_database
from book_manager import add_book, list_books, delete_book

app = Flask(__name__)

# Set up the database
setup_database()

@app.route('/')
def index():
    books = list_books()
    return render_template('index.html', books=books)

@app.route('/add', methods=['POST'])
def add():
    title = request.form.get('title')
    author = request.form.get('author')
    add_book(title, author)
    return redirect('/')

@app.route('/delete/<int:book_id>')
def delete(book_id):
    delete_book(book_id)
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
