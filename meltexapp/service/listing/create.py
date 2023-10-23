from meltexapp.helper.listing import create_listing as create_listing_helper
from meltexapp.config.listing import LISTING_REQUIRED_FIELDS


def create_listing(user, data):
    for rf in LISTING_REQUIRED_FIELDS:
        if not data.get(rf, False):
            raise Exception(f"{rf} is a required field")
    geography_id = data.get("geography")
    sub_asset_class_id = data.get("sub_asset_class")
    impl_approach = data.get("impl_approach")
    fund_levr = data.get("fund_levr")
    fund_struc = data.get("fund_struc")
    fund_inc_year = data.get("fund_inc_year")
    fund_targ_clos_yr = data.get("fund_targ_clos_yr")
    fund_vehi_type = data.get("fund_vehi_type")
    nav = data.get("nav")
    nav_dis_avl = data.get("nav_dis_avl")
    expr_int_ddline = data.get("expr_int_ddline")
    targ_irr = data.get("targ_irr")
    risk_prof = data.get("risk_prof")
    fund_ter = data.get("fund_ter")
    owner = user
    comments = data.get("comments")
    public = data.get("public", True)

    return create_listing_helper(
        user,
        geography_id,
        sub_asset_class_id,
        impl_approach,
        fund_levr,
        fund_struc,
        fund_inc_year,
        fund_targ_clos_yr,
        fund_vehi_type,
        nav,
        nav_dis_avl,
        expr_int_ddline,
        targ_irr,
        risk_prof,
        fund_ter,
        owner,
        comments,
        public,
    )
