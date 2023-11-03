from meltexapp.service.listing.create import create_listing as create_listing_service
from meltexapp.service.listing.update import update_listing as update_listing_service
from meltexapp.helper.asset_class import get_asset_class_from_listing
from django.shortcuts import redirect
from meltexapp.views.views import add_listing
from meltexapp.models import Listing
from django.shortcuts import render
from meltexapp.forms import ListingForm


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
