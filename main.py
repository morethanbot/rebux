import data
from data.provider.pg_provider import PGProvider


db = PGProvider()
db.connect(host="rc1b-3t64ginmv5ottmzv.mdb.yandexcloud.net",
           port=6432,
           sslmode=None,
           dbname="rebux",
           user="lavrov",
           password="relibrebux")

db.execute('''CREATE TABLE "circulation" (
     "circulation_id"	INTEGER,
     "catalogue"	INTEGER,
     "barcode"	INTEGER,
     "startdate"	INTEGER,
     "finishdate"	INTEGER,
     "reader_id"	INTEGER,
     "bookpoint_id"	INTEGER,
     "state"	TEXT
);''')

db.commit()

data.circulation_repository
