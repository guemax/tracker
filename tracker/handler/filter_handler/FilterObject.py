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
    def __init__(self, day: str, month: str, year: str, message: str) -> None:
        self.day, self.month, self.year, self.message = day, month, year, message

        # Don't forget to unify the filter_dict to get the right format for the filter_dict
        self.__unify()

    def empty(self) -> bool:
        if self.day == "" and self.month == "" and self.year == "" and self.message == "":
            return True

        return False

    def __unify(self) -> None:
        unified_filters = UnifyFilters().unify(self.day, self.month, self.year, self.message)

        self.day = unified_filters["day"]
        self.month = unified_filters["month"]
        self.year = unified_filters["year"]
        self.message = unified_filters["message"]

    def get_dict(self) -> dict:
        return {"day": self.day, "month": self.month, "year": self.year, "message": self.message}
