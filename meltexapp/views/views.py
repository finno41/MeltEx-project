from django.http import HttpResponse
from meltexapp.service.listing.search import listing_search
from meltexapp.dto.listing import ListingDTOCollection
from meltexapp.data_format.table import format_for_table
from meltexapp.helper.asset_class import get_asset_class_options
from django.shortcuts import render
from meltexapp.config.listing import get_listing_title_map
from meltexapp.forms import ListingForm


def index(request):
    return render(request, "home.html")


def get_listings(request):
    user = request.user
    params = dict(request.GET)
    listings_data = listing_search(user, **params)
    listings = ListingDTOCollection(listings_data, user).output()
    table_variables = (
        format_for_table(listings)
        if listings
        else format_for_table(
            listings, col_headers=list(get_listing_title_map().values())
        )
    )
    ac_options = get_asset_class_options(user)
    template_vars = table_variables | {"ac_options": ac_options}
    return render(request, "listings/listings.html", template_vars)


def add_listing(request):
    form = ListingForm(request.POST)
    return render(request, "listings/add_listing.html", {"form": form})
