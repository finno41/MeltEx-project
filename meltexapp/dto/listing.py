from meltexapp.helper.base_dto import BaseDTOCollection, BaseDTO
from meltexapp.data.geography import get_geographies_by_ids
from meltexapp.data.sub_asset_class import get_sub_assets_by_ids
import pandas as pd


class ListingDTO(BaseDTO):
    def __init__(self, data, user, geog_df=pd.DataFrame(), ac_df=pd.DataFrame()):
        geog_id = data["geography_id"]
        sub_ac_id = data["sub_asset_class_id"]
        if geog_df.empty:
            geographies = get_geographies_by_ids(user, [geog_id]).values()
            geog_df = pd.DataFrame(geographies).set_index("id")
            geog_df = pd.DataFrame(geographies).set_index("id")
        geog_info = geog_df.loc[[geog_id]]
        self.geography = geog_info["name"][0]
        if ac_df.empty:
            sub_acs = get_sub_assets_by_ids(user, [sub_ac_id]).values(
                "id", "name", "asset_class__name"
            )
            ac_df = pd.DataFrame(sub_acs).set_index("id")
        ac_info = ac_df.loc[[sub_ac_id]]
        self.asset_class_name = ac_info["asset_class__name"][0]
        self.sub_asset_class_name = ac_info["name"][0]

        super().__init__(
            data,
            user,
            hide_keys=[
                "id",
                "geography_id",
                "owner_id",
                "public",
                "asset_class_id",
                "sub_asset_class_id",
                "created_on",
                "updated_on",
                "deleted_on",
            ],
        )


class ListingDTOCollection(BaseDTOCollection):
    def __init__(self, data, user):
        if not isinstance(data, list):
            data = list(data.values())
        if not data:
            super().__init__(data, user, base_dto=ListingDTO)
        else:
            geography_ids = [d["geography_id"].hex for d in data]
            geographies = get_geographies_by_ids(user, geography_ids).values()
            geog_df = pd.DataFrame(geographies).set_index("id")
            sub_ac_ids = [d["sub_asset_class_id"].hex for d in data]
            sub_acs = get_sub_assets_by_ids(user, sub_ac_ids).values(
                "id", "name", "asset_class__name"
            )
            ac_df = pd.DataFrame(sub_acs).set_index("id")
            super().__init__(
                data, user, base_dto=ListingDTO, geog_df=geog_df, ac_df=ac_df
            )
