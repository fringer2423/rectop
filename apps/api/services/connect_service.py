from apps.core.models import Connect

from .branch_service import verification_owner_branch_service


def get_connect_by_id_service(user: object, connect_id: int) -> object | None:
    """
    Функция возвращает connect по connect_id если пользователь является owner в company, иначе вернет None
    :param user: Текущий пользователь
    :param connect_id: id соединения
    :return: optional: connect
    """
    connect: object = Connect.objects.get(pk=connect_id)
    result: object | None = (None, connect)[verification_owner_branch_service(branch_id=connect.branch_id, user=user)]
    return result


def get_connect_by_id_branch_and_type(user: object, branch_id: int, connect_type: int) -> object:
    """
    Функция возвращает connect с указанным типом
    :param user: Текущий пользователь
    :param branch_id: id branch
    :param connect_type: тип connect
    :return: connect list
    """
    connect: object = Connect.objects.filter(branch_id=branch_id, type=connect_type).last()
    return connect


def create_connect_by_branch_id_service(user: object, branch_id: int, connect_type: int, key: int) -> object | None:
    """
    Создает новый connect если пользователь является owner в company, иначе вернет None
    :param user: Текущий пользователь
    :param branch_id: id branch
    :param connect_type: Тип платформы
    :param key: Ключ для соединения с площадкой
    :return: optional: connect
    """
    result: object | None = (
        None,
        Connect.objects.create(
            branch_id=branch_id,
            type=connect_type, key=key
        )
    )[verification_owner_branch_service(user=user, branch_id=branch_id)]
    return result
