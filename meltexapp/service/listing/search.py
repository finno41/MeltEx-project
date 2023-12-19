from meltexapp.data.listing import filter_listing
from meltexapp.data.geography import get_geo_children_with_parent
from meltexapp.data.sub_asset_class import get_sub_acs_by_ac, get_sub_acs_by_acs
from datetime import datetime


def listing_search(
    user,
    asset_class_name=None,
    sub_asset_class_name=None,
    geography_id=None,
    ac_id=None,
    company_only=False,
    valid_exp_int_ddline=True,
):
    geos = (
        list(get_geo_children_with_parent(
            user, geography_id)) if geography_id else None
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
    filter_listings = filter_listing(
        user, valid_exp_int_ddline=valid_exp_int_ddline, company_only=company_only **filters)
    filter_listings = filter_listings.order_by("expr_int_ddline", "id")
    return filter_listings
