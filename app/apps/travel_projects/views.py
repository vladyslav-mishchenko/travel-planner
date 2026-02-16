from django.db import transaction

from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from drf_spectacular.utils import extend_schema, OpenApiExample

from .models import TravelProject
from apps.travel_places.models import TravelPlace
from apps.places.models import Place

from .serializers import (
    TravelProjectSerializer,
    TravelProjectWithPlacesSerializer,
)


class TravelProjectViewSet(viewsets.ModelViewSet):
    queryset = TravelProject.objects.all()
    serializer_class = TravelProjectSerializer
    lookup_field = "id"

    def perform_destroy(self, instance):
        if instance.places.filter(is_visited=True).exists():
            raise ValidationError("Your project has visited places!")

        instance.delete()


class TravelProjectWithPlaces(viewsets.ModelViewSet):
    queryset = TravelProject.objects.all()
    serializer_class = TravelProjectWithPlacesSerializer
    lookup_field = "id"
    http_method_names = ["post"]

    @extend_schema(
        examples=[
            OpenApiExample(
                "Project with Places",
                summary="Create TravelProject and TravelPlaces",
                description="One request to create project and multiple places",
                value={
                    "name": "Europe Trip",
                    "description": "Summer vacation",
                    "places": [
                        {
                            "notes": "Eiffel Tower",
                            "is_visited": False,
                            "place": "place pk",
                        },
                        {
                            "notes": "Colosseum",
                            "is_visited": False,
                            "place": "place pk",
                        },
                    ],
                },
                request_only=True,
            )
        ]
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        places_data = self.request.data.get("places", [])

        with transaction.atomic():
            project = serializer.save(owner=self.request.user)

            for place_data in places_data:
                place_id = place_data.get("place")
                place_instance = Place.objects.get(id=place_id)

                TravelPlace.objects.create(
                    travel_project=project,
                    notes=place_data.get("notes", ""),
                    is_visited=place_data.get("is_visited", False),
                    place=place_instance,
                )
