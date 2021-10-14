from model.book import Book
from data import *


def add_book(book_id: int, rating: float):
    book = Book(book_id=book_id, rating=rating)
    book_repository.add_book(book=book)
