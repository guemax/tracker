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

from tracker.commands.console_logger import info_deprecated
from tracker.handler.entry_handler import GroupedEntryHandler


def log_all_entries_grouped_by_date() -> None:
    entry_handler = GroupedEntryHandler.GroupedEntryHandler()

    entries = entry_handler.get_entries_grouped_by_date()
    number_of_entries = len(entries)

    if number_of_entries == 0:
        info_deprecated("Nothing to see yet.\n"
             "  (use \"tracker start\" to create an entry)")
        info_deprecated("\nOK")
    else:
        info_deprecated(f"Showing all entries grouped by date. ({number_of_entries} in total).\n"
             f"  (use \"tracker log <ID>\" to show all entries of the date with the ID <ID>.\n")
        info_deprecated(f"{entries}\n"
             f"\nOK")
