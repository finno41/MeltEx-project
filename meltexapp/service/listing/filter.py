from meltexapp.config.listing import column_ids_names
from meltexapp.helper.asset_class import get_asset_class_options
from meltexapp.helper.geography import get_available_geographies
from meltexapp.helper.general import bulk_manipulate_dict_list
import pandas as pd


def get_filter_options(user):
    columns = column_ids_names()
    asset_classes = get_asset_class_options(user)
    asset_class_filter_data = bulk_manipulate_dict_list(
        asset_classes,
        add_keys={"default": True},
    )
    geographies = get_available_geographies(user)
    geography_filter_data = bulk_manipulate_dict_list(
        geographies,
        add_keys={"default": True},
    )
    return asset_class_filter_data, geography_filter_data, columns


def add_filter_formatting(
    asset_class_filter=False, geography_filter=False, columns_filter=False
):
    filter_settings = [
        {
            "name": "Columns",
            "key": "columns",
            "type": "tickbox",
            "options": columns_filter,
        },
        {
            "name": "Region",
            "key": "geography",
            "type": "tickbox",
            "options": geography_filter,
        },
        {
            "name": "Asset Class",
            "key": "ac_id",
            "type": "tickbox",
            "options": asset_class_filter,
        },
    ]
    return [
        filter_setting
        for filter_setting in filter_settings
        if filter_setting["options"] is not False
    ]
