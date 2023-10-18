from meltexapp.helper.base_dto import BaseDTOCollection, BaseDTO
from meltexapp.data.geography import get_geographies_by_ids
import pandas as pd


class ListingDTO(BaseDTO):
    def __init__(self, data, user, geog_df=None):
        geog_id = data["geography_id"]
        geog_info = geog_df.loc[[geog_id]]
        self.geography = geog_info["name"][0]
        super().__init__(data, user, hide_keys=["id", "geography_id"])


class ListingDTOCollection(BaseDTOCollection):
    def __init__(self, data, user):
        if not isinstance(data, list):
            data = list(data.values())
        geography_ids = [d["geography_id"].hex for d in data]
        geographies = get_geographies_by_ids(user, geography_ids).values()
        geog_df = pd.DataFrame(geographies).set_index("id")
        super().__init__(data, user, base_dto=ListingDTO, geog_df=geog_df)
