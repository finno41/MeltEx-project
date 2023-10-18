from django.http import HttpResponse
from meltexapp.service.listing.search import listing_search
from meltexapp.dto.listing import ListingDTOCollection
from meltexapp.data_format.table import format_for_table
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world. Welcome to the meltex homepage")


def get_listings(request):
    user = request.user
    listings_data = listing_search(user)
    listings = ListingDTOCollection(listings_data, user).output()
    table_variables = format_for_table(listings)
    return render(request, "listings/listings.html", table_variables)


def add_listing(request):
    return HttpResponse("Welcome to the add listing page")
