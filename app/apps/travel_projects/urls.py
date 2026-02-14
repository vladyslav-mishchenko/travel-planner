from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TravelProjectViewSet

router = DefaultRouter()
router.register(r"travel-projects", TravelProjectViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
