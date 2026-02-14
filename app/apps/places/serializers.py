from rest_framework import serializers
from .models import Place


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = (
            "id",
            "name",
            "description",
        )
        read_only_fields = ("id",)

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Name cannot be empty")
        return value
