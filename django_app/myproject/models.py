from django.db import models

class StockData(models.Model):
    symbol = models.CharField(max_length=10)
    date = models.DateField()
    close = models.FloatField()
    daily_return = models.FloatField()

    def __str__(self):
        return f"{self.symbol} - {self.date}"

class StockMetrics(models.Model):
    ticker = models.CharField(max_length=10)
    date = models.DateField()
    sales_growth = models.FloatField()
    equity_growth = models.FloatField()
    eps_growth = models.FloatField()
    fcf_growth = models.FloatField()
    roic = models.FloatField()

    def __str__(self):
        return f'{self.ticker} - {self.date}'