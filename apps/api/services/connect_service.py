from apps.core.models import Connect
from .company_services import verification_owner_company


def get_connect_by_id(user, connect_id):
    """
    Функция возвращает connect по connect_id если пользователь является owner в company, иначе вернет False
    :param user: Текущий пользователь
    :param connect_id: id соединения
    :return: connect или False
    """
    connect = Connect.objects.get(pk=connect_id)
    if verification_owner_company(company_id=connect.company.id, user=user):
        return connect
    else:
        return False


def create_connect_by_company_id(user, company_id, connect_type, key):
    """
    Создает новый connect если пользователь является owner в company, иначе вернет False
    :param user: Текущий пользователь
    :param company_id: id компании
    :param connect_type: Тип платформы
    :param key: Ключ для соединения с площадкой
    :return: connect или False
    """
    if verification_owner_company(user=user, company_id=company_id):
        return Connect.objects.create(company_id=company_id, type=connect_type, key=key)
    else:
        return False
