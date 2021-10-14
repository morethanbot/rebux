import data
from model.connection import Connection


def add_connection(from_id, to_id, weight):
    book_from = data.book_repository.get_book(book_id=from_id)
    book_to = data.book_repository.get_book(book_id=to_id)
    connection = Connection(book_from=book_from, book_to=book_to, weight=weight)
    data.connections_repository.update_connection(connection=connection)
