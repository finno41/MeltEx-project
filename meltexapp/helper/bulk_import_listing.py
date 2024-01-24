from meltexapp.config.listing import LISTING_CONFIG
from django.http import HttpResponse
import pandas as pd


def get_listing_import_df():
    column_titles = [lc["name"] for lc in LISTING_CONFIG]
    df = pd.DataFrame(columns=column_titles)
    return df


def get_listing_import_response(df):
    csv_file = df.to_csv(index=False)
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="listing_import.csv"'
    response.write(csv_file)
    return response
