from apps.core.models import Review

from .branch_service import verification_owner_branch


def get_review_by_id(user, review_id):
    """
    Функция возвращает review по review id если у текущего пользователя есть доступ, иначе вернется False
    :param user: Текущий пользователь
    :param review_id: Review id
    :return: review или False
    """
    review = Review.objects.get(pk=review_id)
    if verification_owner_branch(user=user, branch_id=review.branch_id):
        return review
    else:
        return False


def create_review_by_branch_id(user, branch_id, full_name, link, rating):
    """
    Функция создает review, если у текущего пользователя есть доступ, иначе вернет False
    :param user: Текущий пользователь
    :param branch_id: branch id
    :param full_name: Полное имя
    :param link: Ссылка
    :param rating: Оценка
    :return: review или False
    """
    if verification_owner_branch(user=user, branch_id=branch_id):
        review = Review.objects.create(branch_id=branch_id, full_name=full_name, link=link, rating=rating)
        return review
    else:
        return False


def verification_owner_review(user, review_id):
    """
    Функция проверяет имеет ли текущий пользователь доступ к review
    :param user: текущий пользователь
    :param review_id: review id
    :return: True или False
    """
    review = Review.objects.get(pk=review_id)
    return verification_owner_branch(user, review.branch_id)
