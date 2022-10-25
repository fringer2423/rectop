from apps.core.models import ReviewSettings

from .company_services import verification_owner_company_service


def create_review_settings_by_company_id_service(user, company_id, mask):
    """
    Функция создает review settings если у пользователя есть доступ, иначе вернет False
    :param user: Текущий пользователь
    :param company_id: company id
    :param mask: Маска
    :return: review или False
    """
    if verification_owner_company_service(user=user, company_id=company_id):
        review_settings = ReviewSettings.objects.create(
            company_id=company_id,
            mask=mask
        )
        return review_settings
    else:
        return False


def get_review_settings_by_id_service(user, review_settings_id):
    """
    Функция возвращает review settings если у пользователя есть доступ, иначе вернет False
    :param user: Текущий пользователь
    :param review_settings_id: review settings id
    :return: review settings или False
    """
    review_settings = ReviewSettings.objects.get(pk=review_settings_id)
    if verification_owner_company_service(user=user, company_id=review_settings.company_id):
        return review_settings
    else:
        return False
