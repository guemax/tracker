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

        self._month = "Jan"
        self._year = "2022"

    def build(self, message: str, number: int) -> str:
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
        # Count the date in double steps, makes two entries per day
        if self.__is_first_entry_of_day():
            # 1 -> 1 + 1 / 2 = 1
            # 3 -> 3 + 1 / 2 = 2
            # 5 -> 5 + 1 / 2 = 3
            number = (self._number + 1) / 2
        elif self.__is_second_entry_of_day():
            # 2 -> 1
            # 4 -> 2
            # 6 -> 3
            number = self._number / 2

        date = int(number / 2)

        self._start_date = f"\"{self._month}, {date} {self._year}\""
        self._stop_date = self._start_date

    def __is_first_entry_of_day(self) -> bool:
        return not self.__is_second_entry_of_day()

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
