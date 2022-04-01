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

import sys

import click

from tracker.console_logger.console_logger import info, warn
from tracker.handler.entry_handler import GroupedEntryHandler
from tracker.handler.entry_handler import EntryHandler
from tracker.exceptions.InvalidIDOfDateException import InvalidIDOfDateException


@click.command()
@click.option("-i", "--id", "id_of_date", help="ID of a specific day", type=int)
def log(id_of_date: int):
    """Show old entries grouped by date"""
    if id_of_date is not None:
        entry_handler = EntryHandler.EntryHandler()
        try:
            entries_of_specific_date = entry_handler.get_entries_of_specific_date(id_of_date)
        except InvalidIDOfDateException:
            warn(f"We couldn't find a date matching the ID {id_of_date}.\n"
                 f"Please double check if this was the ID you meant.\n"
                 f"EXIT")
            sys.exit(-1)

        date = entries_of_specific_date[0]
        entries_of_specific_date = entries_of_specific_date[1]

        number_of_entries = len(entries_of_specific_date)

        info(f"Showing all entries of {date}. ({number_of_entries} in total).\n")
        info(f"{entries_of_specific_date}\n"
             f"\nOK")
    else:
        entry_handler = GroupedEntryHandler.GroupedEntryHandler()
        entries_grouped_by_date = entry_handler.get_entries_grouped_by_date()
        number_of_grouped_entries = len(entries_grouped_by_date)

        if number_of_grouped_entries == 0:
            info("Nothing to see yet.\n"
                 "  (use \"tracker start\" to create an entry)")
            info("\nOK")
        else:
            info(f"Showing all entries grouped by date. ({number_of_grouped_entries} in total).\n"
                 f"  (use \"tracker log <ID>\" to show all entries of the date with the ID <ID>.\n")
            info(f"{entries_grouped_by_date}\n"
                 f"\nOK")
