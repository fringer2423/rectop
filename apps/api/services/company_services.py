from apps.core.models import Company


def verification_owner_company(user, company_id):
    company = Company.objects.get(pk=company_id)
    return company.owner == user


def get_company_by_id(user, company_id):
    if verification_owner_company(user, company_id):
        return Company.objects.get(pk=company_id)
    else:
        return False


def create_company(owner, company_name):
    company = Company.objects.create(owner=owner, name=company_name)
    return company
