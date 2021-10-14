from typing import List

from data.repository.connections_repository.connections_repository import ConnectionsRepository
from model.book import Book
from model.connection import Connection


class DatabaseConnectionsRepository(ConnectionsRepository):
    def update_connection(self, connection: Connection):
        pass

    def get_connections(self, book_from: Book) -> List[Connection]:
        pass
