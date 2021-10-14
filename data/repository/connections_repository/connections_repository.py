from abc import *

from model.book import Book
from model.connection import Connection


class ConnectionsRepository(ABC):
    @abstractmethod
    def add_connection(self, connection: Connection):
        pass

    @abstractmethod
    def get_connections(self, book_from: Book):
        pass
