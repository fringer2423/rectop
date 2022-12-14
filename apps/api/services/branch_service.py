from django.db.models import QuerySet

from apps.core.models import Branch, User

from .company_services import verification_owner_company_service


def get_branch_by_id_service(user: QuerySet[User], branch_id: int) -> QuerySet[Branch] | None:
    """
    Функция возвращает филиал по его id. Если текущий пользователь не владелец этого филиала, вернется None
    :param user: Текущий пользователь
    :param branch_id: id филиала
    :return: optional: branch
    """
    branch: QuerySet[Branch] = Branch.objects.get(pk=branch_id)
    result: QuerySet[Branch] | None = (
        None,
        branch
    )[
        verification_owner_company_service(
            company_id=branch.company.id,
            user=user
        )
    ]
    return result


def verification_owner_branch_service(user: QuerySet[User], branch_id: int) -> bool:
    """
    Функция проверяет, имеет ли текущий пользователь доступ к branch
    :param user: текущий пользователь
    :param branch_id: id branch
    :return: True или False
    """
    branch: QuerySet[Branch] = Branch.objects.get(pk=branch_id)
    return verification_owner_company_service(user=user, company_id=branch.company_id)


def get_all_not_detected_branch_service() -> QuerySet[Branch]:
    """
    Функция возвращает все branch, которые еще не обработаны системой.
    :return: branch_list
    """
    branch_list: QuerySet[Branch] = Branch.objects.filter(is_detected=False)
    return branch_list


def get_branch_service(branch_id: int) -> QuerySet[Branch]:
    """
    Функция возвращает branch по id
    :param branch_id: id branch
    :return: branch
    """
    return Branch.objects.get(pk=branch_id)


def create_branch_by_company(
        user: QuerySet[User],
        company_id: int,
        name: str,
        address: str = '',
        phone_number: str = '',
        email: str = None,
        description: str = '',
        short_description: str = ''
) -> QuerySet[Branch] | None:
    """
    Функция создает branch, если у текущего пользователя есть доступ
    :param user: Текущий пользователь
    :param company_id: id company
    :param name: название company
    :param address: адрес
    :param phone_number: мобильный номер
    :param email: email
    :param description: описание
    :param short_description: короткое описание
    :return: optional: branch
    """
    result: QuerySet[Branch] | None = (
        None,
        _create_branch_service(
            company_id=company_id,
            name=name,
            address=address,
            phone_number=phone_number,
            email=email,
            description=description,
            short_description=short_description
        )
    )[verification_owner_company_service(user=user, company_id=company_id)]
    return result


def _create_branch_service(
        company_id: int,
        name: str,
        address: str,
        phone_number: str,
        email: str,
        description: str,
        short_description: str
) -> QuerySet[Branch]:
    branch: QuerySet[Branch] = Branch.objects.create(
        company_id=company_id,
        name=name,
        address=address,
        phone_number=phone_number,
        email=email,
        description=description,
        short_description=short_description
    )
    return branch
