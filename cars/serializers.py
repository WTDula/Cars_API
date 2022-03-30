from rest_framework import serializers
from . import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ["id", "make", "model", "year", "price"]