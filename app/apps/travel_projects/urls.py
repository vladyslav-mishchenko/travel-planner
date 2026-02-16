from rest_framework.routers import DefaultRouter

from django.urls import path, include
from .views import (
    TravelProjectViewSet,
    TravelProjectWithPlaces,
)

router = DefaultRouter()
router.register(r"travel-projects", TravelProjectViewSet)
router.register(
    r"travel-projects-with-places",
    TravelProjectWithPlaces,
    basename="travel-projects-with-places",
)

urlpatterns = [
    path("", include(router.urls)),
]
