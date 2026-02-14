from rest_framework import viewsets

from .models import TravelPlace
from .serializers import TravelPlaceSerializer


class TravelPlaceViewSet(viewsets.ModelViewSet):
    serializer_class = TravelPlaceSerializer
    lookup_field = "id"

    def get_queryset(self):
        project_id = self.kwargs.get("travel_project_id")
        return TravelPlace.objects.filter(travel_project_id=project_id)

    def perform_create(self, serializer):
        serializer.save(travel_project_id=self.kwargs.get("travel_project_id"))
