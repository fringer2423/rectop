from apps.core.models import Company


def verification_owner_company_service(user, company_id):
    """
    Функция проверяет, является ли пользователь владельцем компании
    :param user: Текущий пользователь
    :param company_id: id компании
    :return: True или False
    """
    company = Company.objects.get(pk=company_id)
    return company.owner == user


def get_company_by_id_service(user, company_id):
    """
    Функция возвращает компанию, если текущий пользователь ее владелец, иначе вернет False
    :param user: Текущий пользователь
    :param company_id: id компании
    :return: Company или False
    """
    if verification_owner_company_service(user, company_id):
        return Company.objects.get(pk=company_id)
    else:
        return False


def create_company_by_company_name_service(owner, company_name):
    """
    Функция создает новый объект компании и возвращает его
    :param owner: Владелец
    :param company_name: Название компании
    :return: Company
    """
    company = Company.objects.create(owner=owner, name=company_name)
    return company
