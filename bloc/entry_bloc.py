from typing import List

from data import *
from model.connection import Connection
from model.recommendation import Recommendation


def add_entry(user_id: str, book_id: str):
    user = user_repository.get_user(user_id=user_id)
    book = book_repository.get_book(book_id=book_id)
    circulation_repository.add_user_book(user=user, book=book)

    user_books = circulation_repository.get_user_books(user=user)
    user_book_ids = List[str]()
    for connected_book in user_books:
        user_book_ids.append(connected_book.book_id)
        if connected_book.book_id != book.book_id:
            connection = Connection(book_from=book, book_to=connected_book, weight=1)
            connections_repository.update_connection(connection=connection)

    recommendations = List[Recommendation]()
    for book in user_books:
        connections = connections_repository.get_connections(book_from=book)
        for connection in connections:
            if connection.book_to.book_id not in user_book_ids:
                recommendation = Recommendation(book=connection.book_to, user=user, confidence=connection.weight)
                recommendations.append(recommendation)
    recommendations.sort(key=lambda x: x.confidence, reverse=True)
    recommendations_repository.update_recommendations(user=user, recommendations=recommendations)
