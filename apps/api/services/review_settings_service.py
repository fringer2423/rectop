from apps.core.models import ReviewSettings

from .company_services import verification_owner_company


def create_review_settings_by_company_id(user, company_id, mask):
    if verification_owner_company(user=user, company_id=company_id):
        review_settings = ReviewSettings.objects.create(
            company_id=company_id,
            mask=mask
        )
        return review_settings
    else:
        return False


def get_review_settings_by_id(user, review_settings_id):
    review_settings = ReviewSettings.objects.get(pk=review_settings_id)
    if verification_owner_company(user=user, company_id=review_settings.company_id):
        return review_settings
    else:
        return False
