from data import *


def get_recommendations(user_id: str, count: int):
    user = user_repository.get_user(user_id=user_id)
    return recommendations_repository.get_recommendations(user=user, count=count)
