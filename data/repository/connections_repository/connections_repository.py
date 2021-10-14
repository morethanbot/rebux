from abc import *
from typing import List

from model.book import Book
from model.connection import Connection


class ConnectionsRepository(ABC):
    @abstractmethod
    def update_connection(self, connection: Connection):
        pass

    @abstractmethod
    def get_connections(self, book_from: Book) -> List[Connection]:
        pass
