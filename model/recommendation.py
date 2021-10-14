from model.book import Book
from model.user import User


class Recommendation:
    def __init__(self, user: User, book: Book, confidence: float):
        self.user = user
        self.book = book
        self.confidence = confidence
