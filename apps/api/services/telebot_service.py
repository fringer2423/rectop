from apps.core.models import Telebot
from .branch_service import get_branch


def create_telebot(user, tg_id, branch_id):
    branch = get_branch(user, branch_id)
    if branch:
        telebot = Telebot.objects.create(branch=branch, tg_id=tg_id)
        return telebot
    else:
        return False


def get_telebot(user, telebot_id):
    telebot = Telebot.objects.get(pk=telebot_id)
    if telebot.branch.company.owner != user:
        return False
    else:
        return telebot
