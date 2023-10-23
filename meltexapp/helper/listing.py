from meltexapp.models import Listing
from meltexapp.data.geography import get_geography_by_id
from meltexapp.data.sub_asset_class import get_sub_asset_by_id


def create_listing(
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
    public=True,
):
    geography = get_geography_by_id(user, geography_id)
    sub_asset_class = get_sub_asset_by_id(user, sub_asset_class_id)
    listing = Listing()
    listing.geography = geography
    listing.sub_asset_class = sub_asset_class
    listing.impl_approach = impl_approach
    listing.fund_levr = fund_levr
    listing.fund_struc = fund_struc
    listing.fund_inc_year = fund_inc_year
    listing.fund_targ_clos_yr = fund_targ_clos_yr
    listing.fund_vehi_type = fund_vehi_type
    listing.nav = nav
    listing.nav_dis_avl = nav_dis_avl
    listing.expr_int_ddline = expr_int_ddline
    listing.targ_irr = targ_irr
    listing.risk_prof = risk_prof
    listing.fund_ter = fund_ter
    listing.owner = owner
    listing.comments = comments
    listing.public = public
    listing.save()
    return listing
