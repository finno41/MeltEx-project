from django.urls import path

from meltexapp.views import views
from meltexapp.api.listing import create_listing, update_listing

urlpatterns = [
    path("", views.index, name="index"),
    path("listings", views.get_listings, name="get_listings"),
    path("listings/my_listings", views.my_listings, name="get_listings"),
    path(
        "listings/add_listing",
        views.add_listing,
        name="add_listing",
    ),
    path("ajax/load-subacs/", views.load_sub_acs, name="load_sub_acs"),
    path("load-geographies", views.load_geographies, name="load_geographies"),
    path("listings/create", create_listing, name="create_listing"),
    path("listings/<str:listing_id>", views.view_listing, name="view_listing"),
    path("listings/<str:listing_id>/update", update_listing, name="update_listing"),
    path(
        "listings/<str:listing_id>/delete", views.delete_listing, name="delete_listing"
    ),
]
