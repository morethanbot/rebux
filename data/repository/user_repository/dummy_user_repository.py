from data.repository.user_repository.user_repository import UserRepository
from model.user import User


class DummyUserRepository(UserRepository):
    def get_user(self, user_id: int):
        return self.users[user_id]

    def add_user(self, user: User):
        self.users[user.user_id] = user
