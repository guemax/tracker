import datetime
import calendar
import click

from src.handler.summary_handler.summary_handler import SummaryHandler
from src.console_logger.console_logger import info, warn


@click.command()
@click.option("-lw", "--last-week", "summary_range", help="Range: last week", flag_value="last-week", required=True)
@click.option("-lm", "--last-month", "summary_range", help="Range: last month", flag_value="last-month", required=True)
@click.option("-ly", "--last-year", "summary_range", help="Range: last year", flag_value="last-year", required=True)
def summary(summary_range: str) -> None:
    """Show the summary of work hours per day in a given range"""
    print(summary_range)

    nth_day_ago: int = 0
    if summary_range == "last-week":
        nth_day_ago = 7
    elif summary_range == "last-month":
        today = datetime.datetime.now()
        nth_day_ago = calendar.monthrange(today.year, today.month)[1]
    else:
        today = datetime.datetime.now()
        nth_day_ago = 366 if calendar.isleap(today.year) else 365

    # summary_handler = SummaryHandler(nth_day_ago)
