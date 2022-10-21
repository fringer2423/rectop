from apps.core.models import RateInfo


def get_rate_info():
    """
    Функция возвращает последний rate info
    :return: rate info
    """
    return RateInfo.objects.last()
