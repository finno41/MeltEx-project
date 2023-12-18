from meltexapp.data.listing import get_listing_by_id
from meltexapp.data.geography import get_geography_by_id
from meltexapp.data.sub_asset_class import get_sub_asset_by_id
from meltexapp.config.listing import EDITABLE_LISTING_ATTRS
from datetime import datetime


def update_listing(user, listing_id, data):
    if "geography" in data:
        data["geography"] = get_geography_by_id(user, data["geography"])
    if "sub_asset_class" in data:
        data["sub_asset_class"] = get_sub_asset_by_id(user, data["sub_asset_class"])

    listing = get_listing_by_id(user, listing_id, owned_only=True)
    for attr, val in data.items():
        if attr in EDITABLE_LISTING_ATTRS:
            setattr(listing, attr, val)
    listing.updated_on = datetime.now()
    listing.save()
    return listing
