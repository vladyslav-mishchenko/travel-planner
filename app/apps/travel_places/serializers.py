from rest_framework import serializers
from .models import TravelPlace


class TravelPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelPlace
        fields = (
            "id",
            "notes",
            "travel_project",
            "place",
        )
        read_only_fields = ("id",)
