from meltexapp.global_variables import MASTER_USER_ID
from meltexapp.models import Geography
from meltexapp.helper.user import get_company_users
from django.db.models import Q


def get_permitted_geographies(user):
    company_users = get_company_users(user)
    return Geography.objects.filter(
        Q(owner__in=company_users) | Q(owner=MASTER_USER_ID)
    )


def get_geography_by_id(user, geog_id):
    perm_geos = get_permitted_geographies(user)
    return perm_geos.get(id=geog_id)


def get_geography_children(user, parent_id):
    perm_geos = get_permitted_geographies(user)
    geos = perm_geos.filter(parent_id=parent_id)
    return geos


def get_geo_children_with_parent(user, parent_id):
    perm_geos = get_permitted_geographies(user)
    geos = perm_geos.filter(Q(parent_id=parent_id) | Q(id=parent_id))
    return geos


def get_geographies_by_ids(user, ids):
    perm_geos = get_permitted_geographies(user)
    geos = perm_geos.filter(id__in=ids)
    return geos
