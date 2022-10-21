from apps.core.models import Rate


def create_rate_by_user(user, type=0):
    """
    Функция создает rate для пользователя
    :param user: текущий пользователь
    :param type: type rate. Default = 0
    :return: rate
    """
    rate = Rate.objects.create(user_id=user.id, type=0)
    return rate


def get_rate_by_user(user):
    """
    Функция возвращает rate текущего пользователя
    :param user: текущий пользователь
    :return: rate
    """
    return user.rate
