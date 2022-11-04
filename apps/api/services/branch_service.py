from apps.core.models import Branch

from .company_services import verification_owner_company_service


def get_branch_by_id_service(user, branch_id):
    """
    Функция возвращает филиал по его id. Если текущий пользователь не владелец этого филиала, вернется False
    :param user: Текущий пользователь
    :param branch_id: id филиала
    :return: Branch или False
    """
    branch = Branch.objects.get(pk=branch_id)
    if verification_owner_company_service(company_id=branch.company.id, user=user):
        return branch
    else:
        return False


def verification_owner_branch_service(user, branch_id):
    """
    Функция проверяет, имеет ли текущий пользователь доступ к branch
    :param user: текущий пользователь
    :param branch_id: id branch
    :return: True или False
    """
    branch = Branch.objects.get(pk=branch_id)
    return verification_owner_company_service(user=user, company_id=branch.company_id)


def get_all_not_detected_branch_service():
    """
    Функция возвращает все branch, которые еще не обработаны системой.
    :return: branch_list
    """
    branch_list = Branch.objects.filter(is_detected=False)
    return branch_list


def get_branch_service(branch_id):
    """
    Функция возвращает branch по id
    :param branch_id: id branch
    :return: branch
    """
    return Branch.objects.get(pk=branch_id)


def create_branch_by_company(user, company_id, name, address='', phone_number='', email=None, description='',
                             short_description=''):
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
    :return: branch или False
    """
    if verification_owner_company_service(user=user, company_id=company_id):
        branch = Branch.objects.create(
            company_id=company_id,
            name=name,
            address=address,
            phone_number=phone_number,
            email=email,
            description=description,
            short_description=short_description
        )
        return branch
    else:
        return False
