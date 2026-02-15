from rest_framework import viewsets
from rest_framework.exceptions import ValidationError

from .models import TravelPlace
from .serializers import TravelPlaceSerializer
from .services import ensure_place_exists


class TravelPlaceViewSet(viewsets.ModelViewSet):
    serializer_class = TravelPlaceSerializer
    lookup_field = "id"

    def get_queryset(self):
        project_id = self.kwargs.get("travel_project_id")
        return TravelPlace.objects.filter(travel_project_id=project_id)

    def perform_create(self, serializer):

        # TODO: Implement external API check in `ensure_place_exists`.
        # Currently just a placeholder.
        # Validate if the place exists in the third-party API.
        if not ensure_place_exists("place"):
            raise ValidationError("This place is currently unavailable")

        serializer.save(travel_project_id=self.kwargs.get("travel_project_id"))
