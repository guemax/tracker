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
        self.month = self.__convert_month_value_to_number()

        if self.__day_or_month_are_invalid():
            raise ValueError
        else:
            return self.__create_dict_with_filters()

    def __convert_month_value_to_number(self) -> int:
        if self.__month_has_not_been_specified():
            return 0

        if self.__month_format_is_number():
            return int(self.month)

        # Month has letters in it, translate it into the month number
        if self.__month_format_is_abbrevation():
            return self.__translate_abbrevation_of_month_into_month_number()
        elif self.__month_format_is_name():
            return self.__translate_full_name_of_month_into_month_number()
        else:
            # Month has no valid format, e.g. "January..."
            raise ValueError

    def __month_format_is_number(self) -> bool:
        try:
            self.__translate_number_of_month_into_month_number()
            return True
        except ValueError:
            return False

    def __month_format_is_abbrevation(self) -> bool:
        try:
            self.__translate_abbrevation_of_month_into_month_number()
            return True
        except ValueError:
            return False

    def __month_format_is_name(self) -> bool:
        try:
            self.__translate_full_name_of_month_into_month_number()
            return True
        except ValueError:
            return False

    def __translate_number_of_month_into_month_number(self) -> int:
        return int(self.month)  # E.g. "4" for april (translates to 4)

    def __translate_abbrevation_of_month_into_month_number(self) -> int:
        return int(datetime.strptime(self.month, "%b").strftime("%m"))  # E.g. "Apr" for april

    def __translate_full_name_of_month_into_month_number(self) -> int:
        return int(datetime.strptime(self.month, "%B").strftime("%m"))  # E.g. "April" for april

    def __month_has_not_been_specified(self) -> bool:
        return self.month == "0" or self.month == ""

    def __day_or_month_are_invalid(self) -> bool:
        if self.day < 0 or self.month < 0:
            return True

        return False

    def __create_dict_with_filters(self) -> dict:
        return {"day": self.day, "month": self.month, "year": self.year, "message": self.message}
