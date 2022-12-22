from datetime import datetime

from django.db.models import QuerySet

from apps.core.models import Answer, User, Review

from .review_service import get_review_by_id_service, verification_owner_review_service


def create_answer_by_review_id_service(
        user: QuerySet[User],
        review_id: int,
        body: str,
        type_answer: int
) -> QuerySet[Answer] | None:
    """
    Функция создает новый answer по id review. Если отказано в доступе, вернется None
    :param user: Текущий пользователь
    :param review_id: id review
    :param body: Тело answer
    :param type_answer: Тип answer
    :return: optional: answer
    """
    review: QuerySet[Review] | None = get_review_by_id_service(user=user, review_id=review_id)
    answer: QuerySet[Answer] | None = None
    if review:
        review.status = 2
        review.answered_at = datetime.now()
        review.save()
        answer = _create_answer_service(
            review_id=review_id,
            body=body,
            type_answer=type_answer,
            user_id=user.id
        )
    return answer


def _create_answer_service(review_id: int, body: str, type_answer: int, user_id: int) -> QuerySet[Answer]:
    """
    Функция создает answer
    :param review_id: review id
    :param body: body
    :param type_answer: type
    :param user_id: user id
    :return: answer
    """
    answer: QuerySet[Answer] = Answer.objects.create(
        review_id=review_id,
        body=body,
        type=type_answer,
        user_id=user_id
    )
    return answer


def get_answer_by_id_service(user: QuerySet[User], answer_id: int) -> QuerySet[Answer] | None:
    """
    Функция вернет answer по id answer, если у пользователя есть доступ, иначе вернется False
    :param user: Текущий пользователь
    :param answer_id: id answer
    :return: optional: answer
    """
    answer: QuerySet[Answer] = Answer.objects.get(pk=answer_id)
    result: QuerySet[Answer] | None = (None, answer)[verification_owner_review_service(user, answer.review_id)]
    return result
