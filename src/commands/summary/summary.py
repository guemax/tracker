import logging

import click

from src.handler.summary_handler.week_summary_handler import WeekSummaryHandler
from src.console_logger.console_logger import info, warn


@click.command()
@click.option("-tw", "--this-week", "summary_range", help="Range: this week", flag_value="this-week", required=True)
@click.option("-tm", "--this-month", "summary_range", help="Range: this month", flag_value="this-month", required=True)
@click.option("-ty", "--this-year", "summary_range", help="Range: this year", flag_value="this-year", required=True)
def summary(summary_range: str) -> None:
    """Show the summary of work hours per day in a given range"""
    if summary_range == "this-week":
        summary_handler = WeekSummaryHandler()
    elif summary_range == "this-month":
        # Filter for the current month of this year
        raise NotImplementedError
    else:
        # Filter all entries for the ones created in this year
        raise NotImplementedError

    entries_as_summary = summary_handler.summary()

    logging.info("Showing summary...")
    info(f"Showing entries as summary ({len(entries_as_summary)} in total).\n"
         f"Range is \"{summary_range}\".\n")
    info(f"{entries_as_summary}\n"
         f"\nOK")
