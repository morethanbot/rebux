from model.user import User
from data import *


def add_user(user_id: int):
    user = User(user_id=user_id)
    user_repository.add_user(user=user)
