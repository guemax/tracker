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
along with tracker. If not, see <http://www.gnu.org/licenses/>.
"""

import random
from datetime import datetime, time


class Entry:
    def __init__(self) -> None:
        self._start_date = ""
        self._stop_date = ""

        self._start_time = None
        self._stop_time = None
        self._start_time_dict = {}
        self._stop_time_dict = {}

        self._work_hours = ""
        self._message = ""

        self._number = 0
        self._date = datetime.min

    def build(self, date: datetime, message: str, number: int) -> str:
        self._date = date
        self._number = number
        self._message = message

        self.__create_datetime()
        self.__create_work_hours()

        line = f"{self._start_date},{self._start_time}," \
               f"{self._stop_date},{self._stop_time}," \
               f"{self._work_hours},{self._message}" \
               f"\n"

        return line

    def __create_datetime(self) -> None:
        self.__create_date()
        self.__create_time()

    def __create_date(self) -> None:
        self._start_date = datetime.strftime(self._date, "\"%b, %d %Y\"")
        self._stop_date = self._start_date

    def __is_second_entry_of_day(self) -> bool:
        return self._number % 2 == 0

    def __create_time(self) -> None:
        self.__create_time_dict()

        self._start_time = time(**self._start_time_dict)
        self._stop_time = time(**self._stop_time_dict)

    def __create_time_dict(self) -> None:
        hours = self.__calculate_hours()
        minutes = self.__calculate_minutes()
        seconds = self.__calculate_seconds()

        self.__create_start_time_dict(hours, minutes, seconds)
        self.__create_stop_time_dict(hours, minutes, seconds)

    def __create_start_time_dict(self, hours: dict, minutes: dict, seconds: dict) -> None:
        start_hour = hours["start"]
        start_minutes = minutes["start"]
        start_seconds = seconds["start"]

        self._start_time_dict = {"hour": start_hour, "minute": start_minutes, "second": start_seconds}

    def __create_stop_time_dict(self, hours: dict, minutes: dict, seconds: dict) -> None:
        stop_hour = hours["stop"]
        stop_minutes = minutes["stop"]
        stop_seconds = seconds["stop"]

        self._stop_time_dict = {"hour": stop_hour, "minute": stop_minutes, "second": stop_seconds}

    def __calculate_hours(self) -> dict:
        start_hour = random.randint(0, 11)
        stop_hour = random.randint(start_hour, 12)

        if self.__is_second_entry_of_day():
            # Second entry of day should be in the afternoon, cannot add 12 to prevent times like 24:10:00 -> invalid
            start_hour += 11
            stop_hour += 11

        return {"start": start_hour, "stop": stop_hour}

    @staticmethod
    def __calculate_minutes() -> dict:
        # Needs to be this low to prevent times like 00:60:14 -> invalid
        max_minutes = 58

        start_minutes = random.randint(0, max_minutes)
        stop_minutes = start_minutes + random.randint(1, 59 - start_minutes)

        return {"start": start_minutes, "stop": stop_minutes}

    @staticmethod
    def __calculate_seconds() -> dict:
        # Needs to be this low to prevent times like 00:00:60 -> invalid
        max_seconds = 58

        start_seconds = random.randint(0, max_seconds)
        stop_seconds = start_seconds + random.randint(1, 59 - start_seconds)

        return {"start": start_seconds, "stop": stop_seconds}

    def __create_work_hours(self) -> None:
        start_time = datetime.combine(datetime.min, self._start_time)
        stop_time = datetime.combine(datetime.min, self._stop_time)

        time_delta = stop_time - start_time
        self._work_hours = time_delta
