from django.db.models import QuerySet

from apps.core.models import Company, User


def verification_owner_company_service(user: QuerySet[User], company_id: int) -> bool:
    """
    Функция проверяет, является ли пользователь владельцем компании
    :param user: Текущий пользователь
    :param company_id: id компании
    :return: True или False
    """
    company: QuerySet[Company] = Company.objects.get(pk=company_id)
    return company.owner == user


def get_company_by_id_service(user: QuerySet[User], company_id: int) -> QuerySet[Company] | None:
    """
    Функция возвращает компанию, если текущий пользователь ее владелец, иначе вернет None
    :param user: Текущий пользователь
    :param company_id: id компании
    :return: Optional: Company или None
    """
    result: QuerySet[Company] | None = (
        None, Company.objects.get(pk=company_id)
    )[verification_owner_company_service(user, company_id)]
    return result


def create_company_by_company_name_service(owner: QuerySet[User], company_name: str) -> QuerySet[Company]:
    """
    Функция создает новый объект компании и возвращает его
    :param owner: Владелец
    :param company_name: Название компании
    :return: Company
    """
    company: QuerySet[Company] = Company.objects.create(owner=owner, name=company_name)
    return company
