from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter

from django.urls import path, include
from .views import TravelPlaceViewSet
from apps.travel_projects.views import TravelProjectViewSet

router = DefaultRouter()
router.register(r"travel-projects", TravelProjectViewSet, basename="travel-projects")

nested_router = NestedDefaultRouter(router, r"travel-projects", lookup="travel_project")
nested_router.register(
    r"travel-places",
    TravelPlaceViewSet,
    basename="travel-project-travel-places",
)

urlpatterns = [
    path("", include(router.urls)),
    path("", include(nested_router.urls)),
]
