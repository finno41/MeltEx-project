from meltexapp.service.listing.create import create_listing as create_listing_service
from meltexapp.service.listing.update import update_listing as update_listing_service
from django.core.serializers import serialize
from meltexapp.helper.asset_class import get_asset_class_from_listing
from meltexapp.helper.listing import bulk_create_listing
from django.shortcuts import redirect
from django.http import JsonResponse
from meltexapp.views.views import add_listing
from meltexapp.models import Listing
from django.shortcuts import render
from meltexapp.forms import ListingForm, ExcelListingUploadForm
from meltexapp.helper.bulk_import_listing import (
    get_listing_import_df,
    get_listing_import_response,
)
import pandas as pd


def create_listing(request):
    data = request.POST
    user = request.user
    url = f"/listings/add_listing?listing_added=true"
    listing = create_listing_service(user, data)
    if not isinstance(listing, Listing):
        return listing
    return redirect(url)


def update_listing(request, listing_id):
    data = request.POST.dict()
    user = request.user
    listing = update_listing_service(user, listing_id, data)
    delete_url = f"/listings/{listing.pk}/delete"
    form_action_url = f"/listings/{listing.pk}/update"
    form = ListingForm(request.user, instance=listing)
    asset_class_id = get_asset_class_from_listing(listing).pk
    sub_asset_class_id = listing.sub_asset_class.pk

    return render(
        request,
        "listings/add_listing.html",
        {
            "form": form,
            "method": "update",
            "form_action_url": form_action_url,
            "banners": "listing_updated",
            "delete_url": delete_url,
            "asset_class_id": asset_class_id,
            "sub_asset_class_id": sub_asset_class_id,
        },
    )


def get_excel_listing_template(request):
    user = request.user
    listing_template_df = get_listing_import_df()
    response = get_listing_import_response(user, listing_template_df)
    return response


def upload_excel_listings(request):
    user = request.user
    excel_upload = request.FILES["excel_file"].file
    df = pd.read_excel(excel_upload, sheet_name="Sheet1")
    try:
        listings = bulk_create_listing(user, df)
    except Exception as e:
        return JsonResponse({"success": False, "message": str(e)})
    serialized_data = serialize("json", listings)
    return JsonResponse({"success": True, "data": serialized_data})
