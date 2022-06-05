"""This file is part of tracker.
Tracker is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
Tracker is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with tracker. If not, see <http://www.gnu.org/licenses/>.
"""

import sys

from tracker.handler.entry_handler import EntryHandler
from tracker.commands.console_logger import info, warn
from tracker.exceptions.InvalidIDOfDateException import InvalidIDOfDateException


def log_entries_of_specific_date(id_of_date: int) -> None:
    entry_handler = EntryHandler.EntryHandler()
    try:
        entries_of_specific_date = entry_handler.get_entries_of_specific_date(id_of_date)
    except InvalidIDOfDateException:
        warn(f"We couldn't find a date matching the ID {id_of_date}.\n"
             f"Please double check if this was the ID you meant.\n"
             f"EXIT")
        sys.exit(-1)

    date = entries_of_specific_date[0]
    entries = entries_of_specific_date[1]

    number_of_entries = len(entries)

    info(f"Showing all entries of {date}. ({number_of_entries} in total).\n")
    info(f"{entries}\n"
         f"\nOK")
