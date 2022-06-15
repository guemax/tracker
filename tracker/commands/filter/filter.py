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

import click

from tracker.handler.filter_handler.FilterHandler import FilterHandler

from tracker.commands.console_logger import info, warn


@click.command()
@click.option("-d", "--day", "day", help="Filter entries by given day", type=int, default=0)
@click.option("-m", "--month", "month", help="Filter entries by given month", type=int, default=0)
@click.option("-y", "--year", "year", help="Filter entries by given year", type=int, default=0)
@click.option("--message", type=str, default="")
def filter(day, month, year, message) -> None:
    """Filter entries by the given specifier"""
    info("Showing entries by filter")

    filters = {"day": day, "month": month, "year": year, "message": message}

    filtered_entries = FilterHandler().filter_for(filters)
