from rest_framework import serializers
from .models import TravelProject


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
