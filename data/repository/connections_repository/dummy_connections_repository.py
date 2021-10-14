from typing import List

from data.repository.connections_repository.connections_repository import ConnectionsRepository
from model.book import Book
from model.connection import Connection


class DummyConnectionsRepository(ConnectionsRepository):
    def __init__(self):
        self.connections = {}

    def get_connections(self, book_from: Book) -> List[Connection]:
        return self.connections[book_from.book_id]

    def update_connection(self, connection: Connection):
        from_id = connection.book_from.book_id
        to_id = connection.book_to.book_id
        if self.connections[from_id] is None:
            self.connections[from_id] = {}
        if self.connections[to_id] is None:
            self.connections[to_id] = {}
        if self.connections[from_id][to_id] is not None:
            connection.weight += self.connections[from_id][to_id].weight
        self.connections[from_id][to_id] = connection
        self.connections[to_id][from_id] = connection
