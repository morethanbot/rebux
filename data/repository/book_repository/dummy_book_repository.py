from data.repository.book_repository.book_repository import BookRepository
from model.book import Book
from model.user import User


class DummyBookRepository(BookRepository):
    def get_book(self, book_id: int) -> Book:
        return Book(book_id=book_id, rating=0)

    def add_book(self, user: User):
        pass
        