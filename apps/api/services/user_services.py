from django.contrib.auth.hashers import make_password

from apps.core.models import User


def create_user_by_data_service(data):
    """
    Функция создает нового пользователя по данным из request
    :param data: request.data
    :return: user
    """
    user = User.objects.create(
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email'],
        password=make_password(data['password'])
    )
    return user


def get_user_service(user_id):
    """
    Функция возвращает user по id
    :param user_id: user id
    :return: user
    """
    return User.objects.get(pk=user_id)


def get_user_by_slug_service(slug):
    return User.objects.get(slug=slug)


def verify_user_service(user):
    user.is_verified = True
    user.slug = None
    user.save()
    return user
