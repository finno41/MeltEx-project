from django.urls import path

from meltexapp.views import views
from meltexapp.api.listing import create_listing, update_listing
from django.contrib.auth import views as auth_views
from meltexapp.forms import UserLoginForm

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "listings/load_listings_table/<str:listings_type>",
        views.load_listings_table,
        name="load_listings_table",
    ),
    path(
        "listings/add_listing",
        views.add_listing,
        name="add_listing",
    ),
    path("listings/<str:listings_type>", views.get_listings, name="get_listings"),
    path("ajax/load-subacs/", views.load_sub_acs, name="load_sub_acs"),
    path("load-geographies", views.load_geographies, name="load_geographies"),
    path("listing/create", create_listing, name="create_listing"),
    path("listing/<str:listing_id>", views.view_listing, name="view_listing"),
    path("listing/<str:listing_id>/update", update_listing, name="update_listing"),
    path(
        "listing/<str:listing_id>/delete", views.delete_listing, name="delete_listing"
    ),
    path(
        "accounts/login/",
        auth_views.LoginView.as_view(
            template_name="registration/login.html", authentication_form=UserLoginForm
        ),
        name="login",
    ),
]
