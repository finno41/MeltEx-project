from django.urls import path

from meltexapp.views import views
from meltexapp.api.listing import create_listing

urlpatterns = [
    path("", views.index, name="index"),
    path("listings", views.get_listings, name="get_listings"),
    path(
        "listings/add_listing",
        views.add_listing,
        name="add_listing",
    ),
    path("ajax/load-subacs/", views.load_sub_acs, name="load_sub_acs"),
    path("listings/create", create_listing, name="create_listing"),
]
