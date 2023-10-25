from meltexapp.models import Listing
from django.db.models import Q
from meltexapp.helper.user import get_company_users
from django.http import HttpResponseNotFound


def get_permitted_listings(user):
    company_users = get_company_users(user)
    return Listing.objects.filter(Q(public=True) | Q(owner__in=company_users))


def get_editable_listings(user):
    company_users = get_company_users(user)
    return Listing.objects.filter(owner__in=company_users)


def get_listing_by_id(user, listing_id, owned_only=False):
    perm_listings = (
        get_editable_listings(user) if owned_only else get_permitted_listings(user)
    )
    try:
        return perm_listings.get(id=listing_id)
    except:
        return HttpResponseNotFound(
            "<h1>You do not have permission to view this listing</h1>"
        )


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
