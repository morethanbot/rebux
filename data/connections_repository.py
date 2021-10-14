from model.book import Book
from model.connection import Connection


class ConnectionsRepository:

    def __init__(self):
        self.connections = {}

    def add_connection(self, connection: Connection):
        self.connections[connection.book_from.id] = connection

    def get_connections(self, book_from: Book):
        return self.connections[book_from.id]