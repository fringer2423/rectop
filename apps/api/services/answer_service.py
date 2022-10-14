from datetime import datetime

from apps.core.models import Answer

from .review_service import get_review_by_id, verification_owner_review


def create_answer_by_review_id(user, review_id, body, type):
    """
    Функция создает новый answer по id review. Если отказано в доступе, вернется False
    :param user: Текущий пользователь
    :param review_id: id review
    :param body: Тело answer
    :param type: Тип answer
    :return: Answer или False
    """
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
    """
    Функция вернет answer по id answer, если у пользователя есть доступ, иначе вернется False
    :param user: Текущий пользователь
    :param answer_id: id answer
    :return: answer или False
    """
    answer = Answer.objects.get(pk=answer_id)
    if verification_owner_review(user, answer.review_id):
        return answer
    else:
        return False
