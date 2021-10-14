from typing import List

import data
from data.repository.connections_repository.connections_repository import ConnectionsRepository
from model.book import Book
from model.connection import Connection


class DatabaseConnectionsRepository(ConnectionsRepository):
    def update_connection(self, connection: Connection):
        data.database_provider.execute(
            '''INSERT INTO book_connections (book_from_id, book_to_id, weight) SELECT %s, %s, 0
            WHERE NOT EXISTS(SELECT * FROM book_connections WHERE book_from_id = %s AND book_to_id = %s)''',
            (connection.book_from.book_id, connection.book_to.book_id,
             connection.book_from.book_id, connection.book_to.book_id)
        )
        data.database_provider.execute(
            '''UPDATE book_connections SET weight = weight + %s WHERE book_from_id = %s AND book_to_id = %s''',
            (connection.weight, connection.book_from.book_id, connection.book_to.book_id)
        )
        data.database_provider.commit()

    def get_connections(self, book_from: Book) -> List[Connection]:
        data.database_provider.execute(
            '''SELECT * FROM book_connections WHERE book_from_id = %s''',
            (book_from.book_id,)
        )
        connections: List[Connection] = []
        for row in data.database_provider.get_cursor():
            book_from = data.book_repository.get_book(book_id=row[0])
            book_to = data.book_repository.get_book(book_id=row[1])
            weight = row[2]
            connection = Connection(book_from=book_from, book_to=book_to, weight=weight)
            connections.append(connection)
        return connections
