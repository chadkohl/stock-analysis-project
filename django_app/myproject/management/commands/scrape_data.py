from django.core.management.base import BaseCommand
import yfinance as yf
from myproject.models import StockData  # Import your model

class Command(BaseCommand):
    help = 'Scrape data from yfinance API and store it in the database'

    def handle(self, *args, **kwargs):
        # Define the list of stock symbols to scrape
        stock_symbols = ['AAPL', 'GOOGL', 'MSFT']

        for symbol in stock_symbols:
            # Fetch stock data
            stock = yf.Ticker(symbol)
            hist = stock.history(period="1d")

            # Debug: Print fetched data
            print(f"Fetched data for {symbol}:")
            print(hist)

            # Store data
            for index, row in hist.iterrows():
                try:
                    StockData.objects.create(
                        symbol=symbol,
                        date=index,
                        close=row['Close'],
                        daily_return=0.0  # Set a default value for daily_return
                    )
                    # Debug: Print stored data
                    print(f"Stored data for {symbol} on {index}: Close={row['Close']}")
                except Exception as e:
                    print(f"Error storing data for {symbol} on {index}: {e}")

        self.stdout.write(self.style.SUCCESS('Successfully scraped and stored stock data'))