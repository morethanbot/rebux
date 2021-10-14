from data.repository.circulation_repository.circulation_repository import CirculationRepository
from model.book import Book
from model.user import User


class DummyCirculationRepository(CirculationRepository):
    def __init__(self):
        self.user_books = {}

    def get_user_books(self, user: User):
        return self.user_books[user.user_id]

    def add_user_book(self, user: User, book: Book):
        self.user_books[user.user_id].append(book)
