from model.book import Book


class Connection:
    def __init__(self, book_from: Book, book_to: Book, weight: float):
        self.book_from = book_from
        self.book_to = book_to
        self.weight = weight
