from django.urls import path
from .views import (
    AdminOnlySpectacularAPIView,
    AdminOnlySwaggerView,
    AdminOnlyRedocView,
)

app_name = "apidocs"

urlpatterns = [
    path("docs/schema/", AdminOnlySpectacularAPIView.as_view(), name="schema"),
    path(
        "docs/swagger/",
        AdminOnlySwaggerView.as_view(url_name="apidocs:schema"),
        name="swagger-ui",
    ),
    path(
        "docs/redoc/",
        AdminOnlyRedocView.as_view(url_name="apidocs:schema"),
        name="redoc",
    ),
]
