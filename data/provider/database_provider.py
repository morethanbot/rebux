from abc import abstractmethod


class DBProvider:
    def __init__(self):
        pass

    @abstractmethod
    def connect(self, host=None, dbname=None, user=None, password=None, port=None, sslmode=None):
        pass

    @abstractmethod
    def execute(self, sql, *args):
        pass

    @abstractmethod
    def get_cursor(self):
        pass

    @abstractmethod
    def commit(self):
        pass


