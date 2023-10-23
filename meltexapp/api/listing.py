from meltexapp.service.listing.create import create_listing as create_listing_service
from django.shortcuts import redirect
from meltexapp.views.views import add_listing
from meltexapp.models import Listing


def create_listing(request):
    data = request.POST
    user = request.user
    url = f"/listings/add_listing?listing_added=true"
    listing = create_listing_service(user, data)
    if not isinstance(listing, Listing):
        return listing
    return redirect(url)
