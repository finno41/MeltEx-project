from meltexapp.data.geography import get_permitted_geographies
import pandas as pd


def get_continents_countries(user, continents_only=False):
    all_geographies = get_permitted_geographies(user)
    geo_df = pd.DataFrame(all_geographies.values())
    geo_df["id"] = geo_df["id"].apply(lambda x: x.hex)
    continents_df = geo_df[geo_df["parent_id"].isna()]
    countries_df = geo_df[geo_df["parent_id"].notna()]
    continents = continents_df.to_dict("records")
    countries = countries_df.to_dict("records")
    if continents_only:
        return continents
    return continents, countries
