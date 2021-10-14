from abc import *
from typing import List

from model.book import Book
from model.user import User


class CirculationRepository(ABC):
    @abstractmethod
    def get_user_books(self, user: User) -> List[Book]:
        pass

    @abstractmethod
    def add_user_book(self, user: User, book: Book):
        pass
