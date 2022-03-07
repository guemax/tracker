import logging
import sys

import click

from src.handler.summary_handler.week_summary_handler import WeekSummaryHandler
from src.handler.summary_handler.month_summary_handler import MonthSummaryHandler

from src.console_logger.console_logger import info, warn


@click.command()
@click.option("-tw", "--this-week", "summary_range", help="Range: this week", flag_value="week", required=True)
@click.option("-tm", "--this-month", "summary_range", help="Range: this month", flag_value="month", required=True)
@click.option("-ty", "--this-year", "summary_range", help="Range: this year", flag_value="year", required=True)
def summary(summary_range: str) -> None:
    """Show the summary of work hours per day in a given range"""
    if summary_range == "week":
        summary_handler = WeekSummaryHandler()
    elif summary_range == "month":
        summary_handler = MonthSummaryHandler()
    else:
        # Filter all entries for the ones created in this year
        raise NotImplementedError

    entries_as_summary = summary_handler.summary()

    if len(entries_as_summary) == 0:
        logging.info("Showing summary: No entries created this week.")

        info(f"Nothing to show yet. There have been no entries created this {summary_range}.\n"
             f"Create one using \"tracker start\".\n"
             f"\nOK")
        sys.exit(0)

    # Else: There have been some entries created this week
    logging.info("Showing summary...")
    info(f"Showing entries as summary ({len(entries_as_summary)} in total).\n"
         f"Range is \"this-{summary_range}\".\n")
    info(f"{entries_as_summary}\n"
         f"\nOK")
