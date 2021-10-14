from model.book import Book



class DummyConnectionsRepository(ConnectionsRepository):
    def __init__(self):
        self.connections = {}

    def get_connections(self, book_from: Book):
        return self.connections[book_from.book_id]

    def add_connection(self, connection: Connection):
        self.connections[connection.book_from.book_id] = connection
