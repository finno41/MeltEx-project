from meltexapp.models import Listing
from django.db.models import Q
from meltexapp.helper.user import get_company_users
from django.http import HttpResponseNotFound
from datetime import date
from meltexapp.global_variables import MASTER_USER_ID


def get_permitted_listings(user, valid_exp_int_ddline=True):
    company_users = get_company_users(user)
    listings = Listing.objects.filter(
        Q(public=True) | (Q(owner__in=company_users) | Q(owner=MASTER_USER_ID))
    )
    # if valid_exp_int_ddline:
    #     listings = listings.filter(expr_int_ddline__lte=date.today())
    return listings


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


def filter_listing(user, valid_exp_int_ddline=True, company_only=False, **kwargs):
    listings = (
        get_company_listings(user)
        if company_only
        else get_permitted_listings(user, valid_exp_int_ddline=valid_exp_int_ddline)
    )
    return listings.filter(**kwargs)
