from django.http import HttpResponseNotFound
from meltexapp.service.listing.search import listing_search
from meltexapp.dto.listing import ListingDTOCollection
from meltexapp.data_format.table import format_for_table
from meltexapp.helper.asset_class import get_asset_class_options
from django.shortcuts import render
from meltexapp.config.listing import get_listing_title_map
from meltexapp.forms import ListingForm
from meltexapp.data.sub_asset_class import get_sub_acs_by_ac
from meltexapp.data.geography import get_permitted_geographies
from django.contrib.auth.decorators import login_required
from meltexapp.data.listing import get_listing_by_id
from meltexapp.helper.asset_class import get_asset_class_from_listing, get_available_ac_ids
from meltexapp.helper.geography import get_continents_countries
from meltexapp.config.listing import DEFAULT_LISTING_COLUMNS, get_listing_k_v_tuple, column_ids_names
import json


@login_required
def index(request):
    return render(request, "home.html")


@login_required
def get_listings(request):
    user = request.user
    continents, countries = get_continents_countries(user)
    params = dict(request.GET)
    asset_class_name = params.get("asset_class_name")
    sub_asset_class_name = params.get("sub_asset_class_name")
    avaliable_ac_ids = get_available_ac_ids(user)
    ac_ids = params.get("ac_id", avaliable_ac_ids)
    selected_continents = params.get("continents", [c["id"] for c in continents])
    columns = params.get("columns", DEFAULT_LISTING_COLUMNS)
    listings_data = listing_search(
        user, asset_class_name, sub_asset_class_name, selected_continents, ac_ids
    )
    listings = ListingDTOCollection(
        listings_data,
        user,
        hide_keys=[
            "geography_id",
            "owner_id",
            "public",
            "asset_class_id",
            "sub_asset_class_id",
            "created_on",
            "updated_on",
            "deleted_on",
        ],
    ).output()
    available_cols = column_ids_names()
    table_variables = format_for_table(listings, columns)
    params_present = json.dumps(bool(params))
    ac_options = get_asset_class_options(user)
    tickbox_form_config = [
        {"title": "ASSET CLASS", "options": ac_options, "param": "ac_id"},
        {"title": "COLUMNS", "options": available_cols, "param": "columns"},
        {"title": "CONTINENTS", "options": continents, "param": "continents"}
    ]
    template_vars = table_variables | {
        "params_present": params_present,
        "tickbox": tickbox_form_config,
        "page": "listings",
        "selected_filters": json.dumps([selected_continents, columns, ac_ids]),
        "countries": countries
    }
    return render(request, "listings/listings.html", template_vars)


@login_required
def my_listings(request):
    user = request.user
    params = dict(request.GET)
    continents, countries = get_continents_countries(user)
    avaliable_ac_ids = get_available_ac_ids(user)
    ac_ids = params.get("ac_id", avaliable_ac_ids)
    asset_class_name = params.get("asset_class_name")
    sub_asset_class_name = params.get("sub_asset_class_name")
    geography_id = params.get("geography_id")
    ac_id = params.get("ac_id")
    columns = params["columns"] if "columns" in params else DEFAULT_LISTING_COLUMNS
    selected_continents = params.get("continents", [c["id"] for c in continents])
    listings_data = listing_search(
        user, asset_class_name, sub_asset_class_name, geography_id, ac_id
    )
    listings = ListingDTOCollection(
        listings_data,
        user,
        hide_keys=[
            "geography_id",
            "owner_id",
            "asset_class_id",
            "sub_asset_class_id",
            "created_on",
            "updated_on",
            "deleted_on",
        ],
    ).output()
    columns = params["columns"] if "columns" in params else DEFAULT_LISTING_COLUMNS
    available_cols = column_ids_names()
    table_variables = format_for_table(listings, columns)
    params_present = json.dumps(bool(params))
    ac_options = get_asset_class_options(user)
    tickbox_form_config = [
        {"title": "ASSET CLASS", "options": ac_options, "param": "ac_id"},
        {"title": "COLUMNS", "options": available_cols, "param": "columns"},
        {"title": "CONTINENTS", "options": continents, "param": "continents"}
    ]
    template_vars = table_variables | {
        "params_present": params_present,
        "tickbox": tickbox_form_config,
        "page": "my_listings",
        "selected_filters": json.dumps([selected_continents, columns, ac_ids]),
        "countries": countries
    }
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
        request, "asset_class/sub_ac_dropdown_list_options.html", {
            "sub_acs": sub_acs}
    )


def load_geographies(request):
    user = request.user
    geographies = get_permitted_geographies(user)
    return render(
        request, "geography/geography_dropdown.html", {
            "geographies": geographies}
    )
