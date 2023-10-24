from meltexapp.models import Listing
from django.db.models import Q
from meltexapp.helper.user import get_company_users


def get_permitted_listings(user):
    return Listing.objects.filter(public=True)


def get_listing_by_id(user, listing_id):
    perm_listings = get_permitted_listings(user)
    return perm_listings.get(id=listing_id)


def get_company_listings(user):
    company_users = get_company_users(user)
    return Listing.objects.filter(
        Q(owner=user) | (Q(owner__in=company_users) & Q(public=True))
    )


def filter_listing(user, company_only=False, **kwargs):
    listings = (
        get_company_listings(user) if company_only else get_permitted_listings(user)
    )
    return listings.filter(**kwargs)
