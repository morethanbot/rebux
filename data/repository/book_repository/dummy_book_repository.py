from data.repository.book_repository.book_repository import BookRepository
from model.book import Book
from model.user import User


class DummyBookRepository(BookRepository):
    def get_book(self, user_id: int) -> Book:
        return self.books[user_id]

    def add_book(self, user: User):
        self.books[user.user_id] = user
        