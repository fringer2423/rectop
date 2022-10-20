from apps.core.models import Rate


def create_rate_by_user(user, type=0):
    rate = Rate.objects.create(user_id=user.id, type=0)
    return rate


def get_rate_by_user(user):
    return user.rate
