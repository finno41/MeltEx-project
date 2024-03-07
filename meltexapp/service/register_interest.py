from meltexapp.helper.listing import does_user_own_listing
from meltexapp.data.listing import get_listing_by_id


def get_register_interest_data(user, listing_id):
    listing = get_listing_by_id(user, listing_id)
    # check whether user is buyer or seller on the listing
    if does_user_own_listing(user, listing):
        user_type = "seller"
    # if the user is a buyer bring back a single register interest
    # if the user is a seller bring back all register interests
