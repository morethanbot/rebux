from model.recommendation import Recommendation
from model.user import User


class RecommendationsRepository:
    def __init__(self):
        self.recommendations = {}

    def add_recommendation(self, recommendation: Recommendation):
        self.recommendations[recommendation.user.id].append(recommendation)

    def get_recommendations(self, user: User):
        return self.recommendations[user.id].sort(key=lambda x: x.confidence, reverse=True)
