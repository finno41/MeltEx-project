from meltexapp.config.listing import column_ids_names
from meltexapp.helper.asset_class import get_asset_class_options
from meltexapp.helper.geography import get_continents_countries
from meltexapp.helper.general import bulk_manipulate_dict_list
import pandas as pd


def get_filter_options(user):
    columns = column_ids_names()
    asset_classes = get_asset_class_options(user)
    asset_class_filter_data = bulk_manipulate_dict_list(
        asset_classes,
        add_keys={"default": True},
    )
    continents = get_continents_countries(user, continents_only=True)
    continents_filter_data = bulk_manipulate_dict_list(
        continents,
        add_keys={"default": True},
    )
    return asset_class_filter_data, continents_filter_data, columns


def add_filter_formatting(asset_class_filter, continents_filter, columns_filter):
    return [
        {
            "name": "Columns",
            "key": "columns",
            "type": "tickbox",
            "options": columns_filter,
        },
        {
            "name": "Continents",
            "key": "continents",
            "type": "tickbox",
            "options": continents_filter,
        },
        {
            "name": "Asset Class",
            "key": "ac_id",
            "type": "tickbox",
            "options": asset_class_filter,
        },
    ]
