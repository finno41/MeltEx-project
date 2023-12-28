from django.http import HttpResponseNotFound
from meltexapp.service.listing.search import listing_search
from meltexapp.dto.listing import ListingDTOCollection
from meltexapp.data_format.table import format_for_table
from meltexapp.helper.asset_class import get_asset_class_options
from django.shortcuts import render
from meltexapp.config.listing import (
    get_listing_title_map,
    SORTABLE_LISTING_HEADERS,
    HIDDEN_LISTING_FIELDS,
)
from meltexapp.forms import ListingForm
from meltexapp.data.sub_asset_class import get_sub_acs_by_ac
from meltexapp.data.geography import get_permitted_geographies
from django.contrib.auth.decorators import login_required
from meltexapp.data.listing import get_listing_by_id
from meltexapp.helper.asset_class import (
    get_asset_class_from_listing,
    get_available_ac_ids,
)
from meltexapp.helper.geography import get_continents_countries
from meltexapp.config.listing import (
    DEFAULT_LISTING_COLUMNS,
    get_listing_k_v_tuple,
    column_ids_names,
)
from meltexapp.helper.listing import get_listing_view_data, listing_template_variables
import json


@login_required
def index(request):
    return render(request, "home.html")


@login_required
def get_listings(request):
    user = request.user
    params = dict(request.GET)
    (
        continents,
        countries,
        ac_ids,
        columns,
        selected_continents,
        listings_data,
        available_cols,
        ac_options,
    ) = get_listing_view_data(user, params)
    listings = ListingDTOCollection(
        listings_data,
        user,
        hide_keys=HIDDEN_LISTING_FIELDS,
    ).output()
    template_vars = listing_template_variables(
        listings,
        params,
        ac_options,
        available_cols,
        continents,
        selected_continents,
        columns,
        ac_ids,
        countries,
    )
    return render(request, "listings/listings.html", template_vars)


@login_required
def my_listings(request):
    user = request.user
    params = dict(request.GET)
    (
        continents,
        countries,
        ac_ids,
        columns,
        selected_continents,
        listings_data,
        available_cols,
        ac_options,
    ) = get_listing_view_data(user, params)
    listings = ListingDTOCollection(
        listings_data,
        user,
        hide_keys=HIDDEN_LISTING_FIELDS,
    ).output()
    template_vars = listing_template_variables(
        listings,
        params,
        ac_options,
        available_cols,
        continents,
        selected_continents,
        columns,
        ac_ids,
        countries,
    )
    return render(request, "listings/listings.html", template_vars)


@login_required
def add_listing(request):
    user = request.user
    form = ListingForm(user, request.POST)
    listing_added = request.GET.get("listing_added", False)
    missing_fields = request.GET.get("missing_fields", False)
    form_action_url = "/listings/create"
    return render(
        request,
        "listings/add_listing.html",
        {
            "form": form,
            "listing_added": listing_added,
            "missing_fields": missing_fields,
            "form_action_url": form_action_url,
        },
    )


@login_required
def view_listing(request, listing_id):
    user = request.user
    listing = get_listing_by_id(user, listing_id)
    if isinstance(listing, HttpResponseNotFound):
        return listing
    form = ListingForm(request.user, instance=listing)
    form_action_url = f"/listings/{listing.pk}/update"
    delete_url = f"/listings/{listing.pk}/delete"
    asset_class_id = get_asset_class_from_listing(listing).pk
    sub_asset_class_id = listing.sub_asset_class.pk

    return render(
        request,
        "listings/add_listing.html",
        {
            "form": form,
            "method": "update",
            "form_action_url": form_action_url,
            "delete_url": delete_url,
            "asset_class_id": asset_class_id,
            "sub_asset_class_id": sub_asset_class_id,
        },
    )


@login_required
def delete_listing(request, listing_id):
    user = request.user
    listing = get_listing_by_id(user, listing_id)
    listing.delete()
    form = ListingForm(request.user, instance=listing)
    form_action_url = "/listings/create"

    return render(
        request,
        "listings/add_listing.html",
        {
            "form": form,
            "method": "delete",
            "form_action_url": form_action_url,
            "banners": "listing_deleted",
        },
    )


@login_required
def load_sub_acs(request):
    ac_id = request.GET.get("ac_id")
    user = request.user
    sub_acs = get_sub_acs_by_ac(user, ac_id)
    return render(
        request, "asset_class/sub_ac_dropdown_list_options.html", {"sub_acs": sub_acs}
    )


def load_geographies(request):
    user = request.user
    geographies = get_permitted_geographies(user)
    return render(
        request, "geography/geography_dropdown.html", {"geographies": geographies}
    )
