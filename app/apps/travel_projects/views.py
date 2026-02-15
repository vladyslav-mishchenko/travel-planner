from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from .models import TravelProject
from .serializers import TravelProjectSerializer


class TravelProjectViewSet(viewsets.ModelViewSet):
    queryset = TravelProject.objects.all()
    serializer_class = TravelProjectSerializer
    lookup_field = "id"

    def perform_destroy(self, instance):
        if instance.places.filter(is_visited=True).exists():
            raise ValidationError("Your project has visited places!")

        instance.delete()
