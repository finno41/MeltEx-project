from meltexapp.config.listing import LISTING_CONFIG
from meltexapp.helper.geography import get_geography_names
from meltexapp.helper.asset_class import get_asset_class_names
from meltexapp.helper.sub_asset_class import get_sub_asset_class_names
from meltexapp.helper.excel import number_to_column_letter
import xlsxwriter
from django.http import HttpResponse
import io
import pandas as pd


def get_listing_import_df():
    column_titles = [lc["name"] for lc in LISTING_CONFIG]
    df = pd.DataFrame(columns=column_titles)
    return df


def get_listing_import_response(user, df):
    excel_file = io.BytesIO()
    writer = pd.ExcelWriter(excel_file, engine="xlsxwriter")
    worksheet_name = "Sheet1"
    df.to_excel(writer, sheet_name=worksheet_name, index=False)
    worksheet = writer.sheets[worksheet_name]
    add_data_val_to_worksheet(user, worksheet, df, writer)
    writer.close()
    excel_file.seek(0)
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = 'attachment; filename="listings_upload.xlsx"'
    response.write(excel_file.read())
    return response


def add_data_val_to_worksheet(user, worksheet, df, writer):
    geo_names = get_geography_names(user)
    asset_classes = get_asset_class_names(user)
    sub_asset_classes = get_sub_asset_class_names(user)
    valid_options_sheet_name = "Valid Options"
    workbook = writer.book
    val_worksheet = workbook.add_worksheet(name=valid_options_sheet_name)
    geography_index = df.columns.get_loc("Geography")
    asset_class_index = df.columns.get_loc("Asset Class Name")
    sub_asset_class_index = df.columns.get_loc("Sub Asset Class Name")
    first_validation_row = 1
    validation_criteria = {
        "validate": "list",
        # "input_message": "Pick from the dropdown list",
        # "error_message": "Invalid selection. Please choose from the dropdown list.",
    }
    validation_index_sets = [
        {
            "dropdown_items": geo_names,
            "index": geography_index,
            "validation_column": "A",
            "bottom_row": len(geo_names),
        },
        {
            "dropdown_items": asset_classes,
            "index": asset_class_index,
            "validation_column": "B",
            "bottom_row": len(asset_classes),
        },
        {
            "dropdown_items": sub_asset_classes,
            "index": sub_asset_class_index,
            "validation_column": "C",
            "bottom_row": len(sub_asset_classes),
        },
    ]
    for validation in validation_index_sets:
        val_worksheet.write_column(
            f"{validation['validation_column']}1", validation["dropdown_items"]
        )
        worksheet.data_validation(
            first_validation_row,
            validation["index"],
            1000,
            validation["index"],
            validation_criteria
            | {
                "source": f"='{valid_options_sheet_name}'!${validation['validation_column']}$1:${validation['validation_column']}${validation['bottom_row']}"
            },
        )
