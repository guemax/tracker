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

import pandas

from tracker.handler.filter_handler.FilterObject import FilterObject
from tracker.handler.entry_handler.BaseEntryHandlerClass import BaseEntryHandlerClass


class FilterHandler:
    def __init__(self) -> None:
        self.entries = None
        self.base_entry_handler = BaseEntryHandlerClass()

    def filter_for(self, filters: FilterObject) -> pandas.DataFrame:
        self.entries = self.__get_all_entries()

        if filters.empty():
            return self.entries

        # Necessary to match the right number; not showing entries of 25th when searching for 5 contained by start_date
        day = f" {filters.day} "
        month = f"{filters.month}, "
        year = f" {filters.year}"
        message = filters.message

        # TODO: Add support to filter for entries with no message
        filtered_entries = self.entries.loc[
            (self.entries["start_date"].str.contains(day)) &
            (self.entries["start_date"].str.contains(month)) &
            (self.entries["start_date"].str.contains(year)) &
            (self.entries["message"].str.contains(message))
            ]

        return filtered_entries

    def __get_all_entries(self) -> pandas.DataFrame:
        return self.base_entry_handler.get_data()


