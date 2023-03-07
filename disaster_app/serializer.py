from rest_framework import serializers
from .models import Disaster


class DisasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disaster
        fields = ["id", "api", "source", "name", "category", "reference", "country",
                  "date", "description", "status", "longitudinal", "latitudinal"]
