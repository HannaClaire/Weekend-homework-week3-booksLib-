from flask import render_template
from app import app
from models.books import books 
from models.book import *

@app.route('/books')
def index():
    return render_template('index.html', title="Home", books=books)

@app.route('/books/<int:book_id>')
def show_book(book_id):
    book = books
    return render_template('specific_book.html', book = book)


# @app.route('/books/index')
# def specific_book(index):

#     book = books[int(index)-1]
#     return render_template('book.html', book = book,)

