from django.urls import path

from meltexapp.views import views
from meltexapp.api.listing import (
    create_listing,
    update_listing,
    get_excel_listing_template,
    upload_excel_listings,
)
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
    path(
        "listings/show_listing/<str:listing_id>",
        views.show_listing,
        name="show_listing",
    ),
    path("listings/filter", views.filter_listings, name="filter_listings"),
    path("listings/<str:listings_type>", views.get_listings, name="get_listings"),
    path("ajax/load-subacs/", views.load_sub_acs, name="load_sub_acs"),
    path("load-geographies", views.load_geographies, name="load_geographies"),
    path("listing/create", create_listing, name="create_listing"),
    path("listing/<str:listing_id>", views.view_listing, name="view_listing"),
    path(
        "listing/<str:listing_id>/register_interest",
        views.register_interest,
        name="register_interest",
    ),
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
    path(
        "listings/import/excel/template",
        get_excel_listing_template,
        name="excel_listing_template",
    ),
    path(
        "listings/import/excel",
        upload_excel_listings,
        name="upload_excel_listings",
    ),
]
