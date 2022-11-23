from django.db.models import QuerySet

from apps.core.models import Telebot, User, Branch
from .branch_service import get_branch_by_id_service
from .company_services import verification_owner_company_service


def create_telebot_by_branch_id_service(user: QuerySet[User], tg_id: int, branch_id: int) -> QuerySet[Telebot] | None:
    """
    Функция создает telebot по id филиала, если у пользователя есть доступ.
    :param user: Текущий пользователь
    :param tg_id: Идентификатор telegram
    :param branch_id: id филиала
    :return: optional: telebot
    """
    branch: QuerySet[Branch] = get_branch_by_id_service(user, branch_id)
    telebot: QuerySet[Telebot] | None = None
    if branch:
        telebot = Telebot.objects.create(branch=branch, tg_id=tg_id)

    return telebot


def get_telebot_by_id_service(user: QuerySet[User], telebot_id: int) -> QuerySet[Telebot] | None:
    """
    Функция возвращает telebot, если текущий пользователь имеет к нему доступ, иначе вернется False
    :param user: Текущий пользователь
    :param telebot_id: id telebot
    :return: optional: telebot
    """
    telebot: QuerySet[Telebot] = Telebot.objects.get(pk=telebot_id)
    result: QuerySet[Telebot] | None = (
        None,
        telebot
    )[verification_owner_company_service(company_id=telebot.branch.company.id, user=user)]

    return result
