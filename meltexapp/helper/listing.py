from meltexapp.models import Listing, User
from meltexapp.data.geography import get_geography_by_id
from meltexapp.data.sub_asset_class import (
    get_sub_asset_by_id,
    get_permitted_sub_asset_classes,
)
from meltexapp.service.listing.search import listing_search
from meltexapp.helper.asset_class import get_available_ac_ids, get_asset_class_options
from meltexapp.helper.geography import (
    get_available_geographies,
    get_geography_ids,
    get_permitted_geographies,
)
from meltexapp.config.listing import (
    get_config_by_key,
    get_title_listing_map,
    get_default_listing_columns,
    SORTABLE_LISTING_HEADERS_LOOKUP,
    column_ids_names,
)
from meltexapp.helper.general import convert_uuids_to_str
from meltexapp.data_format.table import format_for_table
from meltexapp.data.asset_class import get_permitted_asset_classes
import json
import pandas as pd


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


def get_listing_view_data(user: User, listings_type: str, params: dict) -> tuple:
    geographies = get_available_geographies(user)
    avaliable_ac_ids = get_available_ac_ids(user)
    ac_ids = params.get("ac_id", avaliable_ac_ids)
    asset_class_name = params.get("asset_class_name")
    sub_asset_class_name = params.get("sub_asset_class_name")
    geography_ids = params.get("meltex_regions")
    selected_geographies = params.get("geographies", [c["id"].hex for c in geographies])
    sort_columns = params.get("sort", ["expr_int_ddline"])
    ascending = params.get("ascending", [False])
    listings_data = listing_search(
        user,
        listings_type,
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
        geographies,
        ac_ids,
        selected_geographies,
        listings_data,
        available_cols,
        ac_options,
    )


def get_listing_template_variables(
    available_geographies,
    listings,
    params,
    ac_options,
    available_cols,
    selected_geographies,
    ac_ids,
    listings_type,
    user,
):
    # table_variables = format_for_table(listings, columns)
    tickbox_form_config = [
        {"title": "ASSET CLASS", "options": ac_options, "param": "ac_id"},
        {
            "title": "REGION",
            "options": available_geographies,
            "param": "meltex_regions",
        },
    ]
    return {
        "listings": listings,
        "params_present": params,
        "json_params": json.dumps(params),
        "tickbox": tickbox_form_config,
        "page": listings_type,
        "selected_filters": json.dumps([selected_geographies, ac_ids]),
        "sortable_headers": list(SORTABLE_LISTING_HEADERS_LOOKUP.keys()),
        "user": user,
    }


def bulk_create_listing(user, df: pd.DataFrame):
    title_listing_map = get_title_listing_map()
    df.columns = [title_listing_map[col] for col in df.columns]
    sub_asset_classes = get_permitted_sub_asset_classes(user)
    sub_asset_class_map = [
        {
            "asset_class_name": sub_ac.asset_class.name,
            "sub_asset_class_name": sub_ac.name,
            "sub_asset_class": sub_ac,
        }
        for sub_ac in sub_asset_classes
    ]
    geographies = get_permitted_geographies(user)
    geography_map = {geography.name: geography for geography in geographies}
    listings = []
    for i, row in df.iterrows():
        model_dict = {
            k: v
            for k, v in dict(row).items()
            if get_config_by_key(k).get("model_key", True)
        }
        sub_asset_class = next(
            (
                sub_ac_data["sub_asset_class"]
                for sub_ac_data in sub_asset_class_map
                if sub_ac_data["asset_class_name"] == row["asset_class_name"]
                and sub_ac_data["sub_asset_class_name"] == row["sub_asset_class_name"]
            ),
            row,
        )
        if isinstance(sub_asset_class, pd.Series):
            raise Exception(f"there is an issue with row {i+1} in the upload document")
        geography = geography_map[row["geography"]]
        model_dict |= {
            "sub_asset_class": sub_asset_class,
            "geography": geography,
            "owner": user,
        }
        listings.append(Listing(**model_dict))
    Listing.objects.bulk_create(listings)
    return listings


def can_edit_listing(user, listing):
    if user.is_authenticated:
        listing_user = listing.owner
        return listing_user.company == user.company
    else:
        return False


def get_selected_filters(user, combined_list=False, hex=False):
    asset_class_ids = list(
        get_permitted_asset_classes(user).values_list("id", flat=True)
    )
    column_keys = get_default_listing_columns()
    geography_ids = get_geography_ids(user)
    if hex:
        asset_class_ids = convert_uuids_to_str(asset_class_ids)
        column_keys = convert_uuids_to_str(column_keys)
        geography_ids = convert_uuids_to_str(geography_ids)
    if combined_list:
        return asset_class_ids + column_keys + geography_ids
    return asset_class_ids, column_keys, geography_ids
