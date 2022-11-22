from django.db.models import QuerySet

from apps.core.models import Review, User

from .branch_service import verification_owner_branch_service
from .company_services import verification_owner_company_service


def get_review_by_id_service(user: QuerySet[User], review_id: int) -> QuerySet[Review] | None:
    """
    Функция возвращает review по review id если у текущего пользователя есть доступ, иначе вернется None
    :param user: Текущий пользователь
    :param review_id: Review id
    :return: optional: review
    """
    review: QuerySet[Review] = Review.objects.get(pk=review_id)
    result: QuerySet[Review] | None = (
        None,
        review
    )[
        verification_owner_branch_service(
            user=user,
            branch_id=review.branch_id
        )
    ]

    return result


def create_review_by_branch_id_service(
        user: QuerySet[User],
        branch_id: int,
        full_name: str,
        link: str,
        rating: int,
        connect_id: int = None
) -> QuerySet[Review] | None:
    """
    Функция создает review, если у текущего пользователя есть доступ, иначе вернет None
    :param connect_id: connect id
    :param user: Текущий пользователь
    :param branch_id: branch id
    :param full_name: Полное имя
    :param link: Ссылка
    :param rating: Оценка
    :return: optional: review
    """
    result: QuerySet[Review] | None = (
        None,
        _create_review_by_branch_id_service(
            branch_id=branch_id,
            full_name=full_name,
            link=link,
            rating=rating,
            connect_id=connect_id
        )
    )[verification_owner_branch_service(user=user, branch_id=branch_id)]

    return result


def _create_review_by_branch_id_service(
        branch_id: int,
        full_name: str,
        link: str,
        rating: int,
        connect_id: int
) -> QuerySet[Review]:
    """
    Функция создает review по branch id
    :param branch_id: branch id
    :param full_name: full name
    :param link: link
    :param rating: rating
    :param connect_id: connect id
    :return: review
    """
    if connect_id is None:
        review: QuerySet[Review] = Review.objects.create(
            branch_id=branch_id,
            full_name=full_name,
            link=link,
            rating=rating
        )
    else:
        review: QuerySet[Review] = Review.objects.create(
            branch_id=branch_id,
            full_name=full_name,
            link=link,
            rating=rating,
            connect_id=connect_id
        )
    return review


def verification_owner_review_service(user: QuerySet[User], review_id: int) -> bool:
    """
    Функция проверяет имеет ли текущий пользователь доступ к review
    :param user: текущий пользователь
    :param review_id: review id
    :return: True или False
    """
    review: QuerySet[Review] = Review.objects.get(pk=review_id)
    return verification_owner_branch_service(user, review.branch_id)


def get_all_review_by_company_id_service(user: QuerySet[User], company_id: int) -> QuerySet[Review] | None:
    """
    Функция возвращает review list определенной company
    :param user: текущий пользователь
    :param company_id: company id
    :return: optional: review list
    """
    review_list: QuerySet[Review] = Review.objects.filter(branch__company_id=company_id)
    result: QuerySet[Review] | None = (None, review_list)[verification_owner_company_service(user, company_id)]

    return result
