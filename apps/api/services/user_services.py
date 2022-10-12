from django.contrib.auth.hashers import make_password

from apps.core.models import User


def create_user_by_data(data):
    """
    Функция создает нового пользователя по данным из request
    :param data: request.data
    :return: user
    """
    user = User.objects.create(
        first_name=data['first_name'],
        last_name=data['last_name'],
        # username=data['email'],
        email=data['email'],
        password=make_password(data['password'])
    )
    return user
