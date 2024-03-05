from meltexapp.global_variables import MASTER_USER_ID
from meltexapp.models import Geography
from meltexapp.helper.user import get_company_users
from meltexapp.helper.general import convert_strings_to_uuids
from django.db.models import Q


def get_permitted_geographies(user):
    company_users = get_company_users(user)
    return Geography.objects.filter(
        Q(owner__in=company_users) | Q(owner=MASTER_USER_ID)
    )


def get_geography_by_id(user, geog_id, type="object"):
    perm_geos = get_permitted_geographies(user)
    if type == "object":
        return perm_geos.get(id=geog_id)
    elif type == "queryset":
        return perm_geos.filter(id=geog_id)


def get_geography_children(user, parent_id):
    perm_geos = get_permitted_geographies(user)
    geos = perm_geos.filter(parent_id=parent_id)
    return geos


def get_geo_children_with_parents(user, parent_ids):
    perm_geos = get_permitted_geographies(user)
    geos = perm_geos.filter(Q(parent__in=parent_ids) | Q(id__in=parent_ids))
    return geos


def get_geographies_by_ids(user, ids):
    perm_geos = get_permitted_geographies(user)
    geos = perm_geos.filter(id__in=ids)
    return geos


def get_geographies_by_parents(user, geographies):
    perm_geos = get_permitted_geographies(user)
    geos = perm_geos.filter(parent__in=geographies)
    return geos


def get_geographies_by_type(user, type):
    geographies = get_permitted_geographies(user)
    return geographies.filter(type=type)
