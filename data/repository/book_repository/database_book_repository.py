import data
from data.repository.book_repository.book_repository import BookRepository
from model.book import Book
from model.user import User


class DatabaseBookRepository(BookRepository):
    def get_book(self, book_id: int) -> Book:
        data.database_provider.execute(
            '''SELECT * from cat WHERE "recId" = %s''',
            (book_id,)
        )
        books = []
        for row in data.database_provider.get_cursor():
            book = Book(
                book_id=row[0],
                author=row[1],
                title=row[2],
                subject=row[7],
                serial=row[9],
            )
            books.append(book)
        if len(books) == 0:
            return Book(
                book_id=book_id,
                author='-',
                title='-',
                subject='-',
                serial='-',
            )
        else:
            return books[0]
        