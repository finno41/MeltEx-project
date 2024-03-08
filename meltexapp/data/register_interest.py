from meltexapp.models import RegisterInterest
from django.db.models import Q
from meltexapp.helper.user import get_company_users
from meltexapp.helper.listing import does_user_own_listing


def get_permitted_register_interest(user):
    user_company = user.company
    # OF TODO: Would be a faster query to get the user type and search either for the buyer user or the seller user
    permitted = RegisterInterest.objects.filter(
        Q(buyer_user__company=user_company) | Q(seller_user__company=user_company)
    )
    return permitted


def check_register_interest_exists(buyer_user, listing) -> bool:
    permitted = get_permitted_register_interest(buyer_user)
    company_users = get_company_users(buyer_user)
    return permitted.filter(
        Q(listing=listing) & Q(buyer_user__in=company_users)
    ).exists()


def get_register_interest_by_buyer(buyer_user, listing):
    permitted = get_permitted_register_interest(buyer_user)
    company_users = get_company_users(buyer_user)
    return permitted.get(Q(listing=listing) & Q(buyer_user__in=company_users))


def get_register_interest_by_seller(seller_user, listing):
    if not does_user_own_listing(seller_user, listing):
        raise Exception("Access to these messages is forbidden")
    else:
        permitted = get_permitted_register_interest(seller_user)
        return permitted.filter(listing=listing)
