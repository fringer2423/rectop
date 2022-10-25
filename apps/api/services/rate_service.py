from apps.core.models import Rate


def create_rate_by_user_service(user, type=0):
    """
    Функция создает rate для пользователя
    :param user: текущий пользователь
    :param type: type rate. Default = 0
    :return: rate
    """
    rate = Rate.objects.create(user_id=user.id, type=0)
    return rate


def get_rate_by_user_service(user):
    """
    Функция возвращает rate текущего пользователя
    :param user: текущий пользователь
    :return: rate
    """
    return user.rate
