"""This file is part of Tracker.
Tracker is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
Tracker is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with Tracker. If not, see <http://www.gnu.org/licenses/>.
"""

import logging
import sys

import click

from tracker.handler.summary_handler.week_summary_handler import WeekSummaryHandler
from tracker.handler.summary_handler.month_summary_handler import MonthSummaryHandler
from tracker.handler.summary_handler.year_summary_handler import YearSummaryHandler

from tracker.commands.console_logger import info_deprecated


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
        summary_handler = YearSummaryHandler()

    entries = summary_handler.summary()
    number_of_entries = len(entries)

    if number_of_entries == 0:
        logging.info(f"Showing all entries (0) as summary of this {summary_range}.")
        info_deprecated(f"Nothing to show yet. There have been no entries created this {summary_range}.\n"
             f"  (use \"Tracker start\" to create one)\n"
             f"\nOK")
        sys.exit(0)

    # Else: There have been some entries created this week
    logging.info(f"Showing all entries ({number_of_entries}) as summary of this {summary_range}.")
    info_deprecated(f"Showing entries as summary ({number_of_entries} in total).\n"
         f"Range is \"this-{summary_range}\".\n")
    info_deprecated(f"{entries}\n"
         f"\nOK")
