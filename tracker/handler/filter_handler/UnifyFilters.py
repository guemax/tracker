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

import datetime


class UnifyFilters:
    def __init__(self) -> None:
        self.day, self.month, self.year, self.message = None, None, None, None

    def unify(self, day: str, month: str, year: str, message: str) -> dict:
        self.day, self.month, self.year, self.message = day, month, year, message
        self.month = self.__convert_month_value_to_abbrevation()

        if self.__day_is_invalid():
            raise ValueError
        else:
            return self.__create_dict_with_filters()

    def __convert_month_value_to_abbrevation(self) -> str:
        if self.__month_has_not_been_specified():
            return ""
        elif self.__month_format_is_number():
            return self.__translate_number_of_month_into_month_abbrevation()
        elif self.__month_format_is_abbrevation():
            return self.__translate_abbrevation_of_month_into_month_abbrevation()
        elif self.__month_format_is_name():
            return self.__translate_full_name_of_month_into_month_abbrevation()
        else:
            # Month has no valid format, e.g. "January..."
            raise ValueError

    def __month_format_is_number(self) -> bool:
        try:
            self.__translate_number_of_month_into_month_abbrevation()
            return True
        except ValueError:
            return False

    def __month_format_is_abbrevation(self) -> bool:
        try:
            self.__translate_abbrevation_of_month_into_month_abbrevation()
            return True
        except ValueError:
            return False

    def __month_format_is_name(self) -> bool:
        try:
            self.__translate_full_name_of_month_into_month_abbrevation()
            return True
        except ValueError:
            return False

    def __translate_number_of_month_into_month_abbrevation(self) -> str:
        return datetime.date(1, int(self.month), 1).strftime("%b")  # E.g. translate "4" to "apr" for april

    def __translate_abbrevation_of_month_into_month_abbrevation(self) -> str:
        return datetime.datetime.strptime(self.month, "%b").strftime("%b")  # E.g. translate "Apr" to "apr" for april

    def __translate_full_name_of_month_into_month_abbrevation(self) -> str:
        return datetime.datetime.strptime(self.month, "%B").strftime("%b")  # E.g. translate "April" to "apr" for april

    def __month_has_not_been_specified(self) -> bool:
        return self.month == "0" or self.month == ""

    def __day_is_invalid(self) -> bool:
        if self.__day_has_not_been_specified():
            return False

        if int(self.day) < 0:
            return True

        return False

    def __day_has_not_been_specified(self) -> bool:
        return True if self.day == "" or self.day == "0" else False

    def __create_dict_with_filters(self) -> dict:
        return {"day": self.day, "month": self.month, "year": self.year, "message": self.message}
