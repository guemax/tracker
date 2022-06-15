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

from tracker.handler.entry_handler.BaseEntryHandlerClass import BaseEntryHandlerClass


class FilterHandler:
    def __init__(self) -> None:
        self.filters = {}
        self.base_entry_handler = BaseEntryHandlerClass()

    @staticmethod
    def remove_unused_filters_from(filters: dict) -> dict:
        cleaned_filters = {}

        for key, value in filters.items():
            if value != "" and value != 0:
                cleaned_filters[key] = value

        return cleaned_filters

    def filter_for(self, filters: dict) -> pandas.DataFrame:
        self.filters = self.remove_unused_filters_from(filters)

        entries = self.get_all_entries()
        # filtered_entries = entries.loc[(entries[])]

    def get_all_entries(self) -> pandas.DataFrame:
        return self.base_entry_handler.get_data()


