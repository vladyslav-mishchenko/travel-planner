from rest_framework import serializers

from .models import TravelPlace


class TravelPlaceSerializer(serializers.ModelSerializer):
    is_visited = serializers.BooleanField(default=False)
    travel_project = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = TravelPlace
        fields = (
            "id",
            "notes",
            "is_visited",
            "travel_project",
            "place",
        )
        read_only_fields = ("id",)
