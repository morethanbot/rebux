from typing import List

from data.repository.circulation_repository.circulation_repository import CirculationRepository
from model.book import Book
from model.user import User
import data


class DatabaseCirculationRepository(CirculationRepository):
    def get_user_books(self, user: User) -> List[Book]:
        data.database_provider.execute(
            '''SELECT DISTINCT book_id FROM user_books WHERE user_id = %s''',
            (user.user_id,)
        )
        books: List[Book] = []
        for book_id in data.database_provider.get_cursor():
            book = data.book_repository.get_book(book_id)
            books.append(book)
        return books

    def add_user_book(self, user: User, book: Book):
        data.database_provider.execute(
            '''INSERT INTO user_books (user_id, book_id) SELECT %s, %s
            WHERE NOT EXISTS(SELECT * FROM user_books WHERE user_id = %s AND book_id = %s)''',
            (user.user_id, book.book_id,
             user.user_id, book.book_id)
        )
        data.database_provider.commit()
