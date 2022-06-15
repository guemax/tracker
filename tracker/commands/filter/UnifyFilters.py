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

from datetime import datetime


class UnifyFilters:
    def __init__(self) -> None:
        self.day, self.month, self.year, self.message = None, None, None, None

    def unify(self, day: int, month: str, year: int, message: str) -> dict:
        self.day, self.month, self.year, self.message = day, month, year, message

        if self.month_has_not_been_specified():
            self.month = 0
            return self.filter_object_if_day_or_month_are_not_invalid()

        try:
            self.month = int(self.month)  # E.g. "4" for april (translates to 4)
        except ValueError:
            # We will handle this down below
            pass
        else:
            return self.filter_object_if_day_or_month_are_not_invalid()

        try:
            self.month = int(datetime.strptime(self.month, "%b").strftime("%m"))  # E.g. "Apr" for april
        except ValueError:
            self.month = int(datetime.strptime(self.month, "%B").strftime("%m"))  # E.g. "April" for april

        # Month is now a number just as day and year
        return self.filter_object_if_day_or_month_are_not_invalid()

    def month_has_not_been_specified(self) -> bool:
        return self.month == "0" or self.month == ""

    def filter_object_if_day_or_month_are_not_invalid(self) -> dict:
        if self.day < 0 or self.month < 0:
            raise ValueError

        return {"day": self.day, "month": self.month, "year": self.year, "message": self.message}
