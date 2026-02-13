from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PlaceViewSet

router = DefaultRouter()
router.register(r"places", PlaceViewSet, basename="place")

urlpatterns = [
    path("", include(router.urls)),
]
