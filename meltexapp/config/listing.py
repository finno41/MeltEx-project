def get_listing_title_map():
    return {
        "impl_approach": "Implementation Approach",
        "fund_levr": "Fund Leverage",
        "fund_struc": "Fund Structure",
        "fund_inc_year": "Fund Inception Year",
        "fund_targ_clos_yr": "Fund Target Closing Year",
        "fund_vehi_type": "Fund Vehicle Type",
        "nav": "Nav (£m)",
        "nav_dis_avl": "Nav Discount Available",
        "expr_int_ddline": "Expression of Interest Deadline",
        "targ_irr": "Targ IRR p/a",
        "risk_prof": "Risk Profile",
        "fund_ter": "Fund TER",
        "comments": "Comments",
        "geography": "Geography",
        "asset_class_name": "Asset Class Name",
        "sub_asset_class_name": "Sub Asset Class Name",
        "sub_asset_class": "Sub Asset Class",
    }


def get_column_titles():
    return list(get_listing_title_map().values())


def get_listing_title(listing_key):
    title_map = get_listing_title_map()
    return title_map.get(listing_key, listing_key)


LISTING_REQUIRED_FIELDS = ["geography", "sub_asset_class"]
