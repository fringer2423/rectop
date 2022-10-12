from apps.core.models import Branch

from .company_services import verification_owner_company


def get_branch_by_branch_id(user, branch_id):
    """
    Функция возвращает филиал по его id. Если текущий пользователь не владелец этого филиала, вернется False
    :param user: Текущий пользователь
    :param branch_id: id филиала
    :return: Branch или False
    """
    branch = Branch.objects.get(pk=branch_id)
    if verification_owner_company(company_id=branch.company.id, user=user):
        return branch
    else:
        return False
