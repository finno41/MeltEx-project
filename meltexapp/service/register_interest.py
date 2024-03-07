from meltexapp.helper.listing import does_user_own_listing
from meltexapp.data.listing import get_listing_by_id
from meltexapp.data.register_interest import (
    get_register_interest_by_buyer,
    get_register_interest_by_seller,
)


def get_register_interest_data(user, listing_id):
    listing = get_listing_by_id(user, listing_id)
    # check whether user is buyer or seller on the listing
    user_type = "seller" if does_user_own_listing(user, listing) else "buyer"
    if user_type == "seller":
        register_interests = get_register_interest_by_seller(user, listing)
    else:
        register_interests = get_register_interest_by_buyer(user, listing)
    return user_type, register_interests
