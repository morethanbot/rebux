class CirculationRepository:

    def __init__(self):
        self.user_books = {}

    def get_user_books(self, user_id: str):
        self._check_user_id(user_id)
        return self.user_books[user_id]

    def add_user_book(self, user_id: str, book_id: str):
        self._check_user_id(user_id)
        self.user_books[user_id].append(book_id)

    def _check_user_id(self, user_id: str):
        if self.user_books[user_id] is None:
            self.user_books[user_id] = []
