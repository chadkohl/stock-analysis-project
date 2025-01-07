# filepath: /home/sigma/stock_analysis_project/django_app/myproject/views.py
from rest_framework import generics
from .models import StockData
from .serializers import StockDataSerializer

class StockDataList(generics.ListAPIView):
    queryset = StockData.objects.all()
    serializer_class = StockDataSerializer