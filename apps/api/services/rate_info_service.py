from django.db.models import QuerySet

from apps.core.models import RateInfo


def get_rate_info_service() -> QuerySet[RateInfo]:
    """
    Функция возвращает последний rate info
    :return: rate info
    """
    return RateInfo.objects.last()
