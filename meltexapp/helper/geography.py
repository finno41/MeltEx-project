from meltexapp.data.geography import get_permitted_geographies
import pandas as pd

def get_continents_countries(user):
    all_geographies = get_permitted_geographies(user)
    geo_df = pd.DataFrame(all_geographies.values())
    continents = "test"
