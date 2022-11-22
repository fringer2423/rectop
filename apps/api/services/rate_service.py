from django.db.models import QuerySet

from apps.core.models import Rate, User


def create_rate_by_user_service(user: QuerySet[User], type: int = 0) -> QuerySet[Rate]:
    """
    Функция создает rate для пользователя
    :param user: текущий пользователь
    :param type: type rate. Default = 0
    :return: rate
    """
    rate: QuerySet[Rate] = Rate.objects.create(user_id=user.id, type=0)
    return rate


def get_rate_by_user_service(user: QuerySet[User]) -> QuerySet[Rate]:
    """
    Функция возвращает rate текущего пользователя
    :param user: текущий пользователь
    :return: rate
    """
    return user.rate
