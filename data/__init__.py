from data.provider.pg_provider import PGProvider
from data.repository.book_repository.dummy_book_repository import DummyBookRepository
from data.repository.circulation_repository.database_circulation_repository import DatabaseCirculationRepository
from data.repository.connections_repository.database_connections_repository import DatabaseConnectionsRepository
from data.repository.recommendations_repository.database_recommendations_repository import \
    DatabaseRecommendationsRepository
from data.repository.user_repository.dummy_user_repository import DummyUserRepository


database_provider = PGProvider()
database_provider.connect(
    host="rc1b-3t64ginmv5ottmzv.mdb.yandexcloud.net",
    port=6432,
    sslmode=None,
    dbname="rebux",
    user="lavrov",
    password="relibrebux"
)

circulation_repository = DatabaseCirculationRepository()
recommendations_repository = DatabaseRecommendationsRepository()
connections_repository = DatabaseConnectionsRepository()
book_repository = DummyBookRepository()
user_repository = DummyUserRepository()
