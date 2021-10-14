from data import *


def add_entry(user_id: str, book_id: str):
    user = user_repository.get_user(user_id=user_id)
    book = book_repository.get_book(book_id=book_id)
    circulation_repository.add_user_book(user=user, book=book)
