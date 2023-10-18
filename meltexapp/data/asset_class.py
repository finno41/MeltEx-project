from meltexapp.models import AssetClass
from meltexapp.global_variables import MASTER_USER_ID
from meltexapp.helper.user import get_company_users
from django.db.models import Q


def get_permitted_asset_classes(user):
    company_users = get_company_users(user)
    return AssetClass.objects.filter(
        Q(owner__in=company_users) | Q(owner=MASTER_USER_ID)
    )
