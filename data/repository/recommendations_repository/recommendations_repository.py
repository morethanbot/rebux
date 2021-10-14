from abc import *

from model.recommendation import Recommendation
from model.user import User


class RecommendationsRepository(ABC):
    @abstractmethod
    def add_recommendation(self, recommendation: Recommendation):
        pass

    @abstractmethod
    def get_recommendations(self, user: User, count: int):
        pass
