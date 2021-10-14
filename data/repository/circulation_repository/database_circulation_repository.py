from typing import List

from data.repository.circulation_repository.circulation_repository import CirculationRepository
from model.book import Book
from model.user import User
import data


class DatabaseCirculationRepository(CirculationRepository):
    def get_user_books(self, user: User) -> List[Book]:
        data.database_provider.execute('''SELECT DISTINCT "catalogueRecordID" FROM circulation WHERE 
        "readerID" = %s''', (user.user_id,))
        results_list: List[Book] = []
        for book_id in data.database_provider.get_cursor():
            results_list.append(data.book_repository.get_book(book_id))
        return results_list

    def add_user_book(self, user: User, book: Book):
        pass

