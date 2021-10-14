from abc import *

from typing import List

from model.recommendation import Recommendation
from model.user import User


class RecommendationsRepository(ABC):
    @abstractmethod
    def update_recommendations(self, user: User, recommendations: List[Recommendation]):
        pass

    @abstractmethod
    def get_recommendations(self, user: User, count: int) -> List[Recommendation]:
        pass
