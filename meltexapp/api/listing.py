from meltexapp.service.listing.create import create_listing as create_listing_service
from django.shortcuts import redirect
from meltexapp.views.views import add_listing


def create_listing(request):
    data = request.POST
    user = request.user
    create_listing_service(user, data)
    redirect(add_listing, listing_added=True)
