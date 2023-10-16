from meltexapp.data.listing import filter_listing
from meltexapp.data.geography import get_geo_children_with_parent


def listing_search(
    user, asset_class_name=None, sub_asset_class_name=None, geography_id=None
):
    geos = (
        list(get_geo_children_with_parent(user, geography_id)) if geography_id else None
    )
    filters = {
        "asset_class_name": asset_class_name,
        "sub_asset_class_name": sub_asset_class_name,
        "geography__in": geos,
    }
    filters = {k: v for k, v in filters.items() if v}
    return filter_listing(user, **filters)
