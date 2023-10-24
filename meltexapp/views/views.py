from django.http import HttpResponse
from meltexapp.service.listing.search import listing_search
from meltexapp.dto.listing import ListingDTOCollection
from meltexapp.data_format.table import format_for_table
from meltexapp.helper.asset_class import get_asset_class_options
from django.shortcuts import render
from meltexapp.config.listing import get_listing_title_map
from meltexapp.forms import ListingForm
from meltexapp.data.sub_asset_class import get_sub_acs_by_ac


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
    form = ListingForm(request.user, request.POST)
    listing_added = request.GET.get("listing_added", False)
    missing_fields = request.GET.get("missing_fields", False)
    return render(
        request,
        "listings/add_listing.html",
        {
            "form": form,
            "listing_added": listing_added,
            "missing_fields": missing_fields,
        },
    )


def load_sub_acs(request):
    ac_id = request.GET.get("ac_id")
    user = request.user
    sub_acs = get_sub_acs_by_ac(user, ac_id)
    return render(
        request, "asset_class/sub_ac_dropdown_list_options.html", {"sub_acs": sub_acs}
    )
