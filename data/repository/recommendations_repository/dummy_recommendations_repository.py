from data.repository.recommendations_repository.recommendations_repository import RecommendationsRepository
from model.recommendation import Recommendation
from model.user import User


class DummyRecommendationsRepository(RecommendationsRepository):
    def __init__(self):
        self.recommendations = {}

    def add_recommendation(self, recommendation: Recommendation):
        self.recommendations[recommendation.user.user_id].append(recommendation)

    def get_recommendations(self, user: User, count: int):
        return self.recommendations[user.user_id].sort(key=lambda x: x.confidence, reverse=True)[:count]
