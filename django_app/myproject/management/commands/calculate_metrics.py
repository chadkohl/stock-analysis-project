# filepath: /home/sigma/stock_analysis_project/django_app/myproject/management/commands/calculate_metrics.py
from django.core.management.base import BaseCommand
from myproject.models import StockMetrics
from datetime import date
from sales_growth import get_sales_growth_rate
from equity_growth import get_equity_growth_rate
from eps_growth import get_eps_growth_rate
from fcf_growth import get_fcf_growth_rate
from roic_calc import calculate_roic

class Command(BaseCommand):
    help = 'Perform calculations and store the results in the database'

    def handle(self, *args, **kwargs):
        ticker = 'MSFT'  # Example stock
        try:
            # Sales Growth Rate
            sales_growth, overall_sales_growth = get_sales_growth_rate(ticker)
            # Equity Growth Rate
            equity_growth, overall_equity_growth = get_equity_growth_rate(ticker)
            # EPS Growth Rate
            eps_growth, overall_eps_growth = get_eps_growth_rate(ticker)
            # Free Cash Flow Growth Rate
            fcf_growth, overall_fcf_growth = get_fcf_growth_rate(ticker)
            # ROIC
            roic_results, overall_roic = calculate_roic(ticker)

            # Create a new database entry
            new_entry = StockMetrics(
                ticker=ticker,
                date=date.today(),
                sales_growth=overall_sales_growth,
                equity_growth=overall_equity_growth,
                eps_growth=overall_eps_growth,
                fcf_growth=overall_fcf_growth,
                roic=overall_roic
            )

            # Add and commit the new entry to the database
            new_entry.save()

            self.stdout.write(self.style.SUCCESS(f'Metrics for {ticker} stored in the database successfully.'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Failed to calculate metrics for {ticker}: {e}'))