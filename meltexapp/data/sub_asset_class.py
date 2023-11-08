from meltexapp.models import SubAssetClass
from meltexapp.global_variables import MASTER_USER_ID
from meltexapp.helper.user import get_company_users
from django.db.models import Q


def get_permitted_sub_asset_classes(user):
    company_users = get_company_users(user)
    return SubAssetClass.objects.filter(
        Q(owner__in=company_users) | Q(owner=MASTER_USER_ID)
    )


def get_sub_asset_by_id(user, sub_id):
    perm_sub_acs = get_permitted_sub_asset_classes(user)
    return perm_sub_acs.get(id=sub_id)


def get_sub_assets_by_ids(user, sub_ids):
    perm_sub_acs = get_permitted_sub_asset_classes(user)
    return perm_sub_acs.filter(id__in=sub_ids)


def get_sub_acs_by_ac(user, asset_class_id):
    if asset_class_id == "":
        return SubAssetClass.objects.none()
    perm_sub_acs = get_permitted_sub_asset_classes(user)
    return perm_sub_acs.filter(asset_class_id=asset_class_id)


def get_sub_acs_by_acs(user, asset_class_ids):
    perm_sub_acs = get_permitted_sub_asset_classes(user)
    return perm_sub_acs.filter(asset_class_id__in=asset_class_ids)
