from apps.core.models import RateInfo


def get_rate_info_service() -> object:
    """
    Функция возвращает последний rate info
    :return: rate info
    """
    return RateInfo.objects.last()
