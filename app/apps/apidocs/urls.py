from django.urls import path
from .views import (
    AdminOnlySpectacularAPIView,
    AdminOnlySwaggerView,
    AdminOnlyRedocView,
)

app_name = "apidocs"

urlpatterns = [
    path("schema/", AdminOnlySpectacularAPIView.as_view(), name="schema"),
    path(
        "swagger/",
        AdminOnlySwaggerView.as_view(url_name="apidocs:schema"),
        name="swagger",
    ),
    path("redoc/", AdminOnlyRedocView.as_view(url_name="apidocs:schema"), name="redoc"),
]
