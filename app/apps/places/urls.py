from django.urls import path
from .views import PlaceListCreateView, PlaceDetailView

app_name = "places"

urlpatterns = [
    path("places/", PlaceListCreateView.as_view(), name="place-list-create"),
    path("places/<uuid:id>/", PlaceDetailView.as_view(), name="place-detail"),
]
