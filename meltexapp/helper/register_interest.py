from meltexapp.models import RegisterInterest
from meltexapp.data.listing import get_listing_by_id
from meltexapp.data.register_interest import check_register_interest_exists
from meltexapp.config.general import DEFAULT_PERMISSION_KEY
from meltexapp.helper.listing import does_user_own_listing
import uuid


def create_register_interest(
    buyer_user,
    listing,
    buyer_message_permissions=DEFAULT_PERMISSION_KEY,
    seller_message_permissions=DEFAULT_PERMISSION_KEY,
    status="pending",
):
    """
    Creates a RegisterInterest object taking in the user
    registering the interest and a listing ID or Listing object
    """
    if check_register_interest_exists(buyer_user, listing):
        # OF TODO: create custom exceptions for this
        raise Exception("You have already registered interest on this product")
    elif does_user_own_listing(buyer_user, listing):
        raise Exception(
            "You cannot register interest on a listing owned by your company"
        )

    if type(listing) in [str, uuid]:
        listing = get_listing_by_id(buyer_user, listing)
    register_interest = RegisterInterest()
    register_interest.buyer_user = buyer_user
    register_interest.seller_user = listing.owner
    register_interest.listing = listing
    register_interest.buyer_message_permissions = buyer_message_permissions
    register_interest.seller_message_permissions = seller_message_permissions
    register_interest.status = status
    register_interest.save()
    return register_interest


def is_user_permitted_reg_interest(user, register_interest):
    return (
        user.company == register_interest.buyer_user.company
        or user.company == register_interest.seller_user.company
    )
