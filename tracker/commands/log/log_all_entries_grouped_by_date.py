"""This file is part of tracker.
tracker is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
tracker is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with tracker. If not, see <http://www.gnu.org/licenses/>.
"""

from tracker.console_logger.console_logger import info
from tracker.handler.entry_handler import GroupedEntryHandler


def log_all_entries_grouped_by_date() -> None:
    entry_handler = GroupedEntryHandler.GroupedEntryHandler()

    entries = entry_handler.get_entries_grouped_by_date()
    number_of_entries = len(entries)

    if number_of_entries == 0:
        info("Nothing to see yet.\n"
             "  (use \"tracker start\" to create an entry)")
        info("\nOK")
    else:
        info(f"Showing all entries grouped by date. ({number_of_entries} in total).\n"
             f"  (use \"tracker log <ID>\" to show all entries of the date with the ID <ID>.\n")
        info(f"{entries}\n"
             f"\nOK")
