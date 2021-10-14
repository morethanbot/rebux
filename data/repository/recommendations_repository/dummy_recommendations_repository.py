from typing import List

from data.repository.recommendations_repository.recommendations_repository import RecommendationsRepository
from model.recommendation import Recommendation
from model.user import User


class DummyRecommendationsRepository(RecommendationsRepository):
    def __init__(self):
        self.recommendations = {}

    def update_recommendations(self, user: User, recommendations: List[Recommendation]):
        self.recommendations[user.user_id] = recommendations

    def get_recommendations(self, user: User, count: int) -> List[Recommendation]:
        return self.recommendations[user.user_id][:count]
