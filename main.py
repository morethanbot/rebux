import data
from data.provider.pg_provider import PGProvider


print(data.circulation_repository.get_user_books(data.user_repository.get_user(44894)))
