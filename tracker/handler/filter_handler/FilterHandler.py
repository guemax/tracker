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
        self.filters = {}
        self.entries = None

        self.base_entry_handler = BaseEntryHandlerClass()

    def filter_for(self, filters: FilterObject) -> pandas.DataFrame:
        self.filters = filters.get_dict_of_used_filters()
        self.entries = self.get_all_entries()

        if self.filters == {}:
            return self.entries

        filtered_entries = self.entries.loc[
            (self.entries["start_date"].str.contains(str(filters.day))) &
            (self.entries["start_date"].str.contains(str(filters.month))) &
            (self.entries["start_date"].str.contains(str(filters.year))) &
            (self.entries["message"].str.contains(str(filters.message)))
        ]

        return filtered_entries

    def get_all_entries(self) -> pandas.DataFrame:
        return self.base_entry_handler.get_data()


