from datetime import datetime

from apps.core.models import Answer

from .review_service import get_review_by_id_service, verification_owner_review_service


def create_answer_by_review_id_service(user: object, review_id: int, body: str, type: int) -> object | None:
    """
    Функция создает новый answer по id review. Если отказано в доступе, вернется None
    :param user: Текущий пользователь
    :param review_id: id review
    :param body: Тело answer
    :param type: Тип answer
    :return: optional: answer
    """
    review: object | None = get_review_by_id_service(user=user, review_id=review_id)
    answer: object | None = None
    if review:
        review.status = 2
        review.answered_at = datetime.now()
        review.save()
        answer = _create_answer_service(
            review_id=review_id,
            body=body,
            type=type,
            user_id=user.id
        )
    return answer


def _create_answer_service(review_id: int, body: str, type: int, user_id) -> object:
    """
    Функция создает answer
    :param review_id: review id
    :param body: body
    :param type: type
    :param user_id: user id
    :return: answer
    """
    answer: object = Answer.objects.create(
        review_id=review_id,
        body=body,
        type=type,
        user_id=user_id
    )
    return answer


def get_answer_by_id_service(user: object, answer_id: int) -> object | None:
    """
    Функция вернет answer по id answer, если у пользователя есть доступ, иначе вернется False
    :param user: Текущий пользователь
    :param answer_id: id answer
    :return: optional: answer
    """
    answer: object = Answer.objects.get(pk=answer_id)
    result: object | None = (None, answer)[verification_owner_review_service(user, answer.review_id)]
    return result
