from apps.core.models import Telebot
from .branch_service import get_branch_by_id
from .company_services import verification_owner_company


def create_telebot_by_branch_id(user, tg_id, branch_id):
    """
    Функция создает telebot по id филиала. Если владельцем этого филиала является не текущий пользователь, вернется False.
    :param user: Текущий пользователь
    :param tg_id: Идентификатор telegram
    :param branch_id: id филиала
    :return: telebot или False
    """
    branch = get_branch_by_id(user, branch_id)
    if branch:
        telebot = Telebot.objects.create(branch=branch, tg_id=tg_id)
        return telebot
    else:
        return False


def get_telebot_by_id(user, telebot_id):
    """
    Функция возвращает telebot, если текущий пользователь имеет к нему доступ, иначе вернется False
    :param user: Текущий пользователь
    :param telebot_id: id telebot
    :return: telebot или False
    """
    telebot = Telebot.objects.get(pk=telebot_id)
    if verification_owner_company(company_id=telebot.branch.company.id, user=user):
        return telebot
    else:
        return False
