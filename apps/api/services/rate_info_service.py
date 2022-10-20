from apps.core.models import RateInfo


def get_rate_info():
    return RateInfo.objects.last()
