from meltexapp.service.listing.create import create_listing as create_listing_service
from meltexapp.service.listing.update import update_listing as update_listing_service
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
    form_action_url = f"/listings/{listing.pk}/update"
    form = ListingForm(request.user, instance=listing)

    return render(
        request,
        "listings/add_listing.html",
        {
            "form": form,
            "method": "update",
            "form_action_url": form_action_url,
            "banners": "listing_updated",
        },
    )
