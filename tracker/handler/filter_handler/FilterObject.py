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

from .UnifyFilters import UnifyFilters


class FilterObject:
    def __init__(self, day: int, month: str, year: int, message: str) -> None:
        self.day, self.month, self.year, self.message = day, month, year, message

        # Don't forget to unify the filters to get the right format for the filters
        self.__unify()

    def __unify(self) -> None:
        unified_filters = UnifyFilters().unify(self.day, self.month, self.year, self.message)

        self.day = unified_filters["day"]
        self.month = unified_filters["month"]
        self.year = unified_filters["year"]
        self.message = unified_filters["message"]

    def get_dict_of_used_filters(self) -> dict:
        return self.__remove_unused_filters_from_all_filters()

    def __remove_unused_filters_from_all_filters(self) -> dict:
        original_filters = self.__get_dict()
        cleaned_filters = {}

        for key, value in original_filters.items():
            if value != "" and value != 0:
                cleaned_filters[key] = value

        return cleaned_filters

    def __get_dict(self) -> dict:
        return {"day": self.day, "month": self.month, "year": self.year, "message": self.message}
