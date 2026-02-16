from rest_framework import serializers

from .models import TravelProject
from apps.travel_places.serializers import TravelPlaceSerializer


class TravelProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelProject
        fields = (
            "id",
            "name",
            "description",
            "owner",
        )
        read_only_fields = ("id", "owner")


class TravelProjectWithPlacesSerializer(serializers.ModelSerializer):
    places = TravelPlaceSerializer(many=True, read_only=True)

    class Meta:
        model = TravelProject
        fields = (
            "id",
            "name",
            "description",
            "owner",
            "places",
        )
        read_only_fields = ("id", "owner")
