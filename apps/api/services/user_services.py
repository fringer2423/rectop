from django.contrib.auth.hashers import make_password
from django.db.models import QuerySet

from apps.core.models import User

from apps.core.services.random_generate_service import generate_random_number_service


def create_user_by_data_service(data: dict) -> QuerySet[User]:
    """
    Функция создает нового пользователя по данным из request
    :param data: request.data
    :return: user
    """
    user: QuerySet[User] = User.objects.create(
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email'],
        password=make_password(data['password'])
    )
    return user


def get_user_service(user_id: int) -> QuerySet[User]:
    """
    Функция возвращает user по id
    :param user_id: user id
    :return: user
    """
    return User.objects.get(pk=user_id)


def get_user_by_slug_service(slug: str) -> QuerySet[User]:
    """
    Функция возвращает user по slug
    :param slug: slug
    :return: user
    """
    return User.objects.get(slug=slug)


def verify_user_service(user: QuerySet[User]) -> QuerySet[User]:
    """
    Функция верифицирует пользователя
    :param user: user
    :return: user
    """
    user.is_verified = True
    user.slug = None
    user.save()
    return user


def generate_new_verify_code_for_user_service(user_id: int) -> QuerySet[User]:
    """
    Функция генерирует новый код подтверждения для user
    :param user_id: user id
    :return: user
    """
    user: QuerySet[User] = get_user_service(user_id)
    user.verify_code = generate_random_number_service(6)
    user.save()
    return user


def verify_user_by_code_service(user: QuerySet[User], verify_code: str) -> bool:
    """
    Функция проверяет код и возвращает результат проверки True или False соответственно
    :param user: user
    :param verify_code: verify code
    :return: True или False
    """
    if user.verify_code == verify_code:
        user.verify_code = None
        user.save()
        return True
    else:
        return False
