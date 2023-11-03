from meltexapp.data.listing import filter_listing
from meltexapp.data.geography import get_geo_children_with_parent
from meltexapp.data.sub_asset_class import get_sub_acs_by_ac, get_sub_acs_by_acs


def listing_search(
    user,
    asset_class_name=None,
    sub_asset_class_name=None,
    geography_id=None,
    ac_id=None,
    company_only=False,
):
    geos = (
        list(get_geo_children_with_parent(user, geography_id)) if geography_id else None
    )
    ac_id = None if ac_id == ["all"] else ac_id
    sub_asset_class_ids = (
        list(get_sub_acs_by_acs(user, ac_id).values_list("id", flat=True))
        if ac_id
        else None
    )
    filters = {
        "asset_class_name": asset_class_name,
        "sub_asset_class_name": sub_asset_class_name,
        "geography__in": geos,
        "sub_asset_class__in": sub_asset_class_ids,
    }
    filters = {k: v for k, v in filters.items() if v}
    return filter_listing(user, company_only, **filters).order_by("-created_on", "-updated_on")
