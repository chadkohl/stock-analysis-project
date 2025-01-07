# filepath: /home/sigma/stock_analysis_project/django_app/myproject/serializers.py
from rest_framework import serializers
from .models import StockData
import math

class StockDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockData
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        for key, value in representation.items():
            if isinstance(value, float) and (math.isnan(value) or math.isinf(value)):
                representation[key] = None
        return representation