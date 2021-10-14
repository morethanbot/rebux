class Book:
    def __init__(self, book_id: int, author: str, title: str, subject: str, serial: str):
        self.book_id = book_id
        self.author = author
        self.title = title
        self.subject = subject
        self.serial = serial

    def __str__(self):
        return f'{self.author}, {self.title}\n{self.subject}\n{self.serial}\n'
