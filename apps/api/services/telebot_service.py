from apps.core.models import Telebot
from .branch_service import get_branch_by_id_service
from .company_services import verification_owner_company_service


def create_telebot_by_branch_id_service(user: object, tg_id: int, branch_id: int) -> object | None:
    """
    Функция создает telebot по id филиала, если у пользователя есть доступ.
    :param user: Текущий пользователь
    :param tg_id: Идентификатор telegram
    :param branch_id: id филиала
    :return: optional: telebot
    """
    branch: object = get_branch_by_id_service(user, branch_id)
    telebot: object | None = None
    if branch:
        telebot = Telebot.objects.create(branch=branch, tg_id=tg_id)

    return telebot


def get_telebot_by_id_service(user: object, telebot_id: int) -> object | None:
    """
    Функция возвращает telebot, если текущий пользователь имеет к нему доступ, иначе вернется False
    :param user: Текущий пользователь
    :param telebot_id: id telebot
    :return: optional: telebot
    """
    telebot: object = Telebot.objects.get(pk=telebot_id)
    result: object | None = (
        None,
        telebot
    )[verification_owner_company_service(company_id=telebot.branch.company.id, user=user)]

    return result
