from models.book import *

book1 = Book("Brave New World", "Aldous Huxley", "Dystopian/Sci-fi")
book2 = Book("The Reluctant Fundamentalist", "Mohsin Hamid", "Cultural fiction")
book3 = Book("The Northern Lights", "Philip Pullman", "Fantasy")

books = [book1, book2, book3]

def add_new_book(book):
    books.append(book)

def show_all_books():
    print(books)
    return books

def delete_book(book_title):
    book_to_delete = None
    for book in books:
        if book.title == book_title:
            book_to_delete = book
            break
    books.remove(book_to_delete)