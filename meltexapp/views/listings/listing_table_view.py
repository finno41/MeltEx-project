from django.shortcuts import render
from meltexapp.helper.asset_class import get_available_ac_ids

def get_listing_contents(request):
    params = dict(request.GET)
    user = request.user
    ac_ids = params.get("ac_id", get_available_ac_ids(user))
    asset_class_name = params.get("asset_class_name")
    sub_asset_class_name = params.get("sub_asset_class_name")
    geography_id = params.get("geography_id")
    ac_id = params.get("ac_id")
