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

from tracker.handler.filter_handler.FilterObject import FilterObject
from tracker.handler.filter_handler.FilterHandler import FilterHandler

from tracker.commands.console_logger import info, warn


@click.command()
@click.option("-d", "--day", "day", help="Filter entries by given day", type=str, default="")
@click.option("-m", "--month", "month", help="Filter entries by given month", type=str, default="")
@click.option("-y", "--year", "year", help="Filter entries by given year", type=str, default="")
@click.option("--message", "message", help="Filter entries by given message", type=str, default="")
def filter(day: str, month: str, year: str, message: str) -> None:
    """Filter entries by the given specifier"""
    try:
        filters = FilterObject(day, month, year, message)
    except ValueError:
        warn("Warning: One of the passed values is not matching the type. Please double check them and try again.",
             print_status=True, exit_tracker=True)
    else:
        if filters.empty():
            info("No filter passed. Showing all entries.", print_status=False)
        else:
            info("Following filter_dict passed:\n", print_status=False)
            for key, value in filters.get_dict().items():
                if value != "" and value != 0:
                    info(f"{key.title()}: {value}", print_status=False)
                else:
                    info(f"{key.title()}: -", print_status=False)

        filtered_entries = FilterHandler().filter_for(filters)

        info("", print_status=False)
        print(filtered_entries)
