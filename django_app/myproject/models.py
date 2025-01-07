from django.db import models

class StockData(models.Model):
    symbol = models.CharField(max_length=10)
    date = models.DateField()
    close = models.FloatField()
    daily_return = models.FloatField()

    def __str__(self):
        return f"{self.symbol} - {self.date}"