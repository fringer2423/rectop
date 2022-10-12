from apps.core.models import Connect
from .company_services import verification_owner_company


def get_connect_by_id(user, connect_id):
    connect = Connect.objects.get(pk=connect_id)
    if verification_owner_company(company_id=connect.company.id, user=user):
        return connect
    else:
        return False


def create_connect_by_company_id(user, company_id, connect_type, key):
    if verification_owner_company(user=user, company_id=company_id):
        return Connect.objects.create(company_id=company_id, type=connect_type, key=key)
    else:
        return False
