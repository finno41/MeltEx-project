from meltexapp.helper.base_dto import BaseDTOCollection, BaseDTO
from meltexapp.data.geography import get_geographies_by_ids, get_geography_by_id
from meltexapp.data.sub_asset_class import get_sub_assets_by_ids
from meltexapp.config.listing import (
    HIDDEN_LISTING_FIELDS,
)
from meltexapp.config.geography import COUNTRY_CODE_LOOKUP
import pandas as pd


class ListingDTO(BaseDTO):
    def __init__(
        self,
        data,
        user,
        hide_keys=HIDDEN_LISTING_FIELDS,
        geog_df=pd.DataFrame(),
        ac_df=pd.DataFrame(),
    ):
        if not isinstance(data, dict):
            data = data.__dict__
        geog_id = data["geography_id"]
        sub_ac_id = data["sub_asset_class_id"]
        if geog_df.empty:
            geography = get_geography_by_id(user, geog_id)
            all_geography_ids = geography.get_ancestor_ids()
            geographies = get_geographies_by_ids(user, all_geography_ids).values()
            geog_df = pd.DataFrame(geographies).set_index("id")
            self.geography_info = {
                geography["type"].capitalize(): geography["name"]
                for geography in geographies
            }
            self.country_code = COUNTRY_CODE_LOOKUP.get(geography.name, None)
        else:
            geog_info = geog_df.loc[[geog_id]]
            self.geography = geog_info["name"].iloc[0]
        if ac_df.empty:
            sub_acs = get_sub_assets_by_ids(user, [sub_ac_id]).values(
                "id", "name", "asset_class__name"
            )
            ac_df = pd.DataFrame(sub_acs).set_index("id")
        ac_info = ac_df.loc[[sub_ac_id]]
        self.asset_class_name = ac_info["asset_class__name"].iloc[0]
        self.sub_asset_class_name = ac_info["name"].iloc[0]

        super().__init__(
            data,
            user,
            hide_keys=hide_keys,
        )


class ListingDTOCollection(BaseDTOCollection):
    def __init__(self, data, user, hide_keys=HIDDEN_LISTING_FIELDS):
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
                data,
                user,
                base_dto=ListingDTO,
                hide_keys=hide_keys,
                geog_df=geog_df,
                ac_df=ac_df,
            )
