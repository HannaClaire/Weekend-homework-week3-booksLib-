from flask import render_template, request, redirect
from app import app
from models.books import *
from models.book import *

@app.route('/books')
def index():
    return render_template('index.html', title="Home", books=books)


@app.route('/books', methods = ['POST'])
def add_book():
    title = request.form['title']
    author = request.form['author']
    genre = request.form['genre']
    new_book= Book(title, author, genre)
    add_new_book(new_book)
    books = show_all_books()
    return render_template('index.html', title="Home", books=books)


@app.route("/books/<index>")  # this will return the details of a chosen book
def show_selected_book(index):
    return render_template("specific_book.html", book=books[int(index)])

@app.route('/books/delete/<title>', methods=['POST'])
def delete(title):
    delete_book(title)
    return redirect('/books')



    # add_new_book(new_book)
    # # add redirect here instead of render
    # return render_template('index.html', title='Home', books=books)





# @app.route('/books/<int:book_id>')
# def show_book(book_id):
#     book = books
#     return render_template('specific_book.html', book = book)


# @app.route('/books/index')
# def specific_book(index):
#     book = books[int(index)]
#     return render_template('book.html', book = book)

