from typing import List

import data
from data.repository.recommendations_repository.recommendations_repository import RecommendationsRepository
from model.recommendation import Recommendation
from model.user import User


class DatabaseRecommendationsRepository(RecommendationsRepository):
    def update_recommendations(self, user: User, recommendations: List[Recommendation]):
        data.database_provider.execute('''DELETE FROM recommendations WHERE "user_id" = %s''', (user.user_id,))
        data.database_provider.commit()
        for recommendation in recommendations:
            data.database_provider.execute(
                '''INSERT INTO recommendations (user_id, book_id, confidence) VALUES (%s, %s, %s)''',
                (recommendation.user.user_id, recommendation.book.book_id, recommendation.confidence)
            )
        data.database_provider.commit()

    def get_recommendations(self, user: User, count: int) -> List[Recommendation]:
        data.database_provider.execute(
            '''SELECT * FROM recommendations WHERE user_id = %s ORDER BY confidence DESC LIMIT %s''',
            (user.user_id, count)
        )
        recommendations: List[Recommendation] = []
        for row in data.database_provider.get_cursor():
            user = data.user_repository.get_user(row[0])
            book = data.book_repository.get_book(row[1])
            confidence = row[2]
            recommendation = Recommendation(user=user, book=book, confidence=confidence)
            recommendations.append(recommendation)
        return recommendations
