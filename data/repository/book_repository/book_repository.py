from abc import *

from model.book import Book


class BookRepository(ABC):
    @abstractmethod
    def get_book(self, book_id: str) -> Book:
        pass

    @abstractmethod
    def add_book(self, book: Book):
        pass
