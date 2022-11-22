from django.db.models import QuerySet

from apps.core.models import Connect, User

from .branch_service import verification_owner_branch_service


def get_connect_by_id_service(user: QuerySet[User], connect_id: int) -> QuerySet[Connect] | None:
    """
    Функция возвращает connect по connect_id если пользователь является owner в company, иначе вернет None
    :param user: Текущий пользователь
    :param connect_id: id соединения
    :return: optional: connect
    """
    connect: QuerySet[Connect] = Connect.objects.get(pk=connect_id)
    result: QuerySet[Connect] | None = (
        None,
        connect
    )[
        verification_owner_branch_service(
            branch_id=connect.branch_id,
            user=user
        )
    ]
    return result


def get_connect_by_id_branch_and_type(user: QuerySet[User], branch_id: int, connect_type: int) -> QuerySet[Connect]:
    """
    Функция возвращает connect с указанным типом
    :param user: Текущий пользователь
    :param branch_id: id branch
    :param connect_type: тип connect
    :return: connect list
    """
    connect: QuerySet[Connect] = Connect.objects.filter(branch_id=branch_id, type=connect_type).last()
    return connect


def create_connect_by_branch_id_service(
        user: QuerySet[User],
        branch_id: int,
        connect_type: int,
        key: int
) -> QuerySet[Connect] | None:
    """
    Создает новый connect если пользователь является owner в company, иначе вернет None
    :param user: Текущий пользователь
    :param branch_id: id branch
    :param connect_type: Тип платформы
    :param key: Ключ для соединения с площадкой
    :return: optional: connect
    """
    result: QuerySet[Connect] | None = (
        None,
        Connect.objects.create(
            branch_id=branch_id,
            type=connect_type, key=key
        )
    )[verification_owner_branch_service(user=user, branch_id=branch_id)]
    return result
