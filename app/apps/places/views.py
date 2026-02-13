from rest_framework import viewsets
from .models import Place
from .serializers import PlaceSerializer
from .permissions import IsSuperUserOrReadOnly


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = [IsSuperUserOrReadOnly]
