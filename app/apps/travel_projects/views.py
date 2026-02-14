from rest_framework import viewsets
from .models import TravelProject
from .serializers import TravelProjectSerializer


class TravelProjectViewSet(viewsets.ModelViewSet):
    queryset = TravelProject.objects.all()
    serializer_class = TravelProjectSerializer
    lookup_field = "id"
