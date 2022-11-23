from django.db.models import QuerySet

from apps.core.models import ReviewSettings, User

from .company_services import verification_owner_company_service


def create_review_settings_by_company_id_service(
        user: QuerySet[User],
        company_id: int,
        mask: str
) -> QuerySet[ReviewSettings] | None:
    """
    Функция создает review settings если у пользователя есть доступ, иначе вернет None
    :param user: Текущий пользователь
    :param company_id: company id
    :param mask: Маска
    :return: optional: review settings
    """
    result: QuerySet[ReviewSettings] | None = (
        None,
        ReviewSettings.objects.create(
            company_id=company_id,
            mask=mask
        )
    )[verification_owner_company_service(user=user, company_id=company_id)]

    return result


def get_review_settings_by_id_service(user: QuerySet[User], review_settings_id: int) -> QuerySet[ReviewSettings] | None:
    """
    Функция возвращает review settings если у пользователя есть доступ, иначе вернет False
    :param user: Текущий пользователь
    :param review_settings_id: review settings id
    :return: optional: review settings
    """
    review_settings: QuerySet[ReviewSettings] = ReviewSettings.objects.get(pk=review_settings_id)
    result: QuerySet[ReviewSettings] | None = (
        None,
        review_settings
    )[verification_owner_company_service(user=user, company_id=review_settings.company_id)]

    return result
