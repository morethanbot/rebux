from model.book import Book


class ConnectionsRepository:

    def __init__(self):
        self.connections = {}

    def add_connection(self, book_from: Book, book_to: Book):
        self.connections[book_from]