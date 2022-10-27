from apps.core.models import Connect

from .branch_service import verification_owner_branch_service


def get_connect_by_id_service(user, connect_id):
    """
    Функция возвращает connect по connect_id если пользователь является owner в company, иначе вернет False
    :param user: Текущий пользователь
    :param connect_id: id соединения
    :return: connect или False
    """
    connect = Connect.objects.get(pk=connect_id)
    if verification_owner_branch_service(branch_id=connect.branch_id, user=user):
        return connect
    else:
        return False


def create_connect_by_branch_id_service(user, branch_id, connect_type, key):
    """
    Создает новый connect если пользователь является owner в company, иначе вернет False
    :param user: Текущий пользователь
    :param branch_id: id branch
    :param connect_type: Тип платформы
    :param key: Ключ для соединения с площадкой
    :return: connect или False
    """
    if verification_owner_branch_service(user=user, branch_id=branch_id):
        return Connect.objects.create(branch_id=branch_id, type=connect_type, key=key)
    else:
        return False
