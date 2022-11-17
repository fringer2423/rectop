from django.contrib.auth.hashers import make_password

from apps.core.models import User

from apps.core.services.random_generate_service import generate_random_number_service


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
    """
    Функция возвращает user по slug
    :param slug: slug
    :return: user
    """
    return User.objects.get(slug=slug)


def verify_user_service(user):
    """
    Функция верифицирует пользователя
    :param user: user
    :return: user
    """
    user.is_verified = True
    user.slug = None
    user.save()
    return user


def generate_new_verify_code_for_user_service(user_id):
    user = get_user_service(user_id)
    user.verify_code = generate_random_number_service(6)
    user.save()
    return user


def verify_user_by_code_service(user, verify_code):
    if user.verify_code == verify_code:
        user.verify_code = None
        user.save()
        return True
    else:
        return False
