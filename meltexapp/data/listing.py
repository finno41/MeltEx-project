from meltexapp.models import Listing
from django.db.models import Q
from meltexapp.helper.user import get_company_users


def get_permitted_listings(user):
    company_users = get_company_users(user)
    return Listing.objects.filter(
        Q(owner=user) | (Q(owner__in=company_users) & Q(public=True))
    )


def filter_listing(user, **kwargs):
    permitted_listings = get_permitted_listings(user)
    return permitted_listings.filter(**kwargs)
