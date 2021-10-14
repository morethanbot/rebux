from abc import *

from model.user import User


class UserRepository(ABC):
    def __init__(self):
        self.users = {}

    @abstractmethod
    def get_user(self, user_id: int):
        pass

    @abstractmethod
    def add_user(self, user: User):
        pass
