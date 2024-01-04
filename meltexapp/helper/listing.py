from meltexapp.models import Listing, User
from meltexapp.data.geography import get_geography_by_id
from meltexapp.data.sub_asset_class import get_sub_asset_by_id
from meltexapp.service.listing.search import listing_search
from meltexapp.helper.asset_class import get_available_ac_ids, get_asset_class_options
from meltexapp.helper.geography import get_continents_countries
from meltexapp.config.listing import (
    get_default_listing_columns,
    SORTABLE_LISTING_HEADERS_LOOKUP,
    column_ids_names,
)
from meltexapp.data_format.table import format_for_table
import json


def create_listing(
    user,
    geography_id,
    sub_asset_class_id,
    impl_approach,
    fund_levr,
    fund_struc,
    fund_inc_year,
    fund_targ_clos_yr,
    fund_vehi_type,
    nav,
    nav_dis_avl,
    expr_int_ddline,
    targ_irr,
    risk_prof,
    fund_ter,
    owner,
    comments,
    public=True,
):
    geography = get_geography_by_id(user, geography_id)
    sub_asset_class = get_sub_asset_by_id(user, sub_asset_class_id)
    listing = Listing()
    listing.geography = geography
    listing.sub_asset_class = sub_asset_class
    listing.impl_approach = impl_approach
    listing.fund_levr = fund_levr
    listing.fund_struc = fund_struc
    listing.fund_inc_year = fund_inc_year
    listing.fund_targ_clos_yr = fund_targ_clos_yr
    listing.fund_vehi_type = fund_vehi_type
    listing.nav = nav
    listing.nav_dis_avl = nav_dis_avl
    listing.expr_int_ddline = expr_int_ddline
    listing.targ_irr = targ_irr
    listing.risk_prof = risk_prof
    listing.fund_ter = fund_ter
    listing.owner = owner
    listing.comments = comments
    listing.public = public
    listing.save()
    return listing


def get_listing_view_data(user: User, params: dict) -> tuple:
    continents, countries = get_continents_countries(user)
    avaliable_ac_ids = get_available_ac_ids(user)
    ac_ids = params.get("ac_id", avaliable_ac_ids)
    asset_class_name = params.get("asset_class_name")
    sub_asset_class_name = params.get("sub_asset_class_name")
    geography_ids = params.get("continents")
    columns = params.get("columns", get_default_listing_columns())
    selected_continents = params.get("continents", [c["id"] for c in continents])
    sort_columns = params.get("sort", ["expr_int_ddline"])
    ascending = params.get("ascending", [False])
    listings_data = listing_search(
        user,
        asset_class_name,
        sub_asset_class_name,
        geography_ids,
        ac_ids,
        sort_columns=sort_columns,
        ascending=ascending,
    )
    available_cols = column_ids_names()
    ac_options = get_asset_class_options(user)

    return (
        continents,
        countries,
        ac_ids,
        columns,
        selected_continents,
        listings_data,
        available_cols,
        ac_options,
    )


def get_listing_template_variables(
    listings,
    params,
    ac_options,
    available_cols,
    continents,
    selected_continents,
    columns,
    ac_ids,
    countries,
):
    table_variables = format_for_table(listings, columns)
    tickbox_form_config = [
        {"title": "ASSET CLASS", "options": ac_options, "param": "ac_id"},
        {"title": "COLUMNS", "options": available_cols, "param": "columns"},
        {"title": "CONTINENTS", "options": continents, "param": "continents"},
    ]
    return table_variables | {
        "params_present": params,
        "json_params": json.dumps(params),
        "tickbox": tickbox_form_config,
        "page": "listings",
        "selected_filters": json.dumps([selected_continents, columns, ac_ids]),
        "countries": countries,
        "sortable_headers": list(SORTABLE_LISTING_HEADERS_LOOKUP.keys()),
    }
