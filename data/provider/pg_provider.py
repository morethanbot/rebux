from data.provider.database_provider import DBProvider
import psycopg2


class PGProvider(DBProvider):
    def __init__(self):
        super().__init__()
        self.__connection__ = None
        self.__cursor__ = None

    def connect(self, host=None, dbname=None, user=None, password=None, port=None, sslmode=None):
        self.__connection__ = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port,
                                               sslmode=sslmode)
        self.__cursor__ = self.__connection__.cursor()

    def execute(self, sql, *args):
        self.__cursor__.execute(sql, *args)

    def get_cursor(self):
        return self.__cursor__

    def commit(self):
        self.__connection__.commit()

    def disconnect(self):
        if self.__connection__ is not None:
            self.__connection__.close()
            self.__cursor__.close()

