from abc import *

from model.book import Book


class BookRepository(ABC):
    def __init__(self):
        self.books = {}

    @abstractmethod
    def get_book(self, book_id: int):
        pass

    @abstractmethod
    def add_book(self, book: Book):
        pass
