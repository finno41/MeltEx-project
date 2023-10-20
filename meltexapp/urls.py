from django.urls import path

from meltexapp.views import views

urlpatterns = [
    path("", views.index, name="index"),
    path("listings", views.get_listings, name="get_listings"),
    path("listings/add_listing", views.add_listing, name="add_listing"),
]
