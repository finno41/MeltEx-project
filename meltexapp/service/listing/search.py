from meltexapp.data.listing import filter_listing
from meltexapp.data.geography import get_geo_children_with_parents
from meltexapp.data.sub_asset_class import get_sub_acs_by_ac, get_sub_acs_by_acs
from meltexapp.config.listing import SORTABLE_LISTING_HEADERS_LOOKUP
from datetime import datetime


def listing_search(
    user,
    asset_class_name=None,
    sub_asset_class_name=None,
    geography_ids=None,
    ac_ids=None,
    company_only=False,
    valid_exp_int_ddline=True,
    sort_columns=["expr_int_ddline"],
    ascending=[False],
):
    geos = (
        list(get_geo_children_with_parents(user, geography_ids))
        if geography_ids
        else None
    )
    sub_asset_class_ids = (
        list(get_sub_acs_by_acs(user, ac_ids).values_list("id", flat=True))
        if ac_ids
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
        user,
        valid_exp_int_ddline=valid_exp_int_ddline,
        company_only=company_only,
        **filters
    )
    sort_columns = [SORTABLE_LISTING_HEADERS_LOOKUP[sc] for sc in sort_columns]
    sort_columns = [
        sc if ascending[i] else "-" + sc for i, sc in enumerate(sort_columns)
    ]
    sort_columns.append("id")
    filter_listings = filter_listings.order_by(*sort_columns)
    return filter_listings
