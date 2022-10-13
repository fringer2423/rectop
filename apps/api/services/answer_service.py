from datetime import datetime

from apps.core.models import Answer

from .review_service import get_review_by_id, verification_owner_review


def create_answer_by_review_id(user, review_id, body, type):
    review = get_review_by_id(user=user, review_id=review_id)
    if review:
        review.status = 2
        review.answered_at = datetime.now()
        review.save()
        answer = Answer.objects.create(
            review_id=review_id,
            body=body,
            type=type,
            user_id=user.id
        )
        return answer
    else:
        return False


def get_answer_by_id(user, answer_id):
    answer = Answer.objects.get(pk=answer_id)
    if verification_owner_review(user, answer.review_id):
        return answer
    else:
        return False
