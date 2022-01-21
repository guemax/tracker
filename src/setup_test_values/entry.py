import random
from datetime import datetime, time


class Entry:
    def __init__(self) -> None:
        self.start_date = ""
        self.stop_date = ""

        self.start_time = None
        self.stop_time = None
        self.start_time_dict = {}
        self.stop_time_dict = {}

        self.work_hours = ""
        self.message = ""

        self.number = 0

        self.month = "Jan"
        self.year = "2022"

    def build(self, message: str, number: int) -> str:
        self.number = number
        self.message = message

        self.create_datetime()
        self.create_work_hours()

        line = f"{self.start_date},{self.start_time}," \
               f"{self.stop_date},{self.stop_time}," \
               f"{self.work_hours},{self.message}" \
               f"\n"

        return line

    def create_datetime(self) -> None:
        self.create_date()
        self.create_time()

    def create_date(self) -> None:
        # Count the date in double steps, makes two entries per day
        if self.is_first_entry_of_day():
            # 1 -> 1 + 1 / 2 = 1
            # 3 -> 3 + 1 / 2 = 2
            # 5 -> 5 + 1 / 2 = 3
            number = (self.number + 1) / 2
        elif self.is_second_entry_of_day():
            # 2 -> 1
            # 4 -> 2
            # 6 -> 3
            number = self.number / 2
        else:
           number = 0

        date = int(number / 2)

        self.start_date = f"\"{self.month}, {date} {self.year}\""
        self.stop_date = self.start_date

    def is_first_entry_of_day(self) -> bool:
        return not self.is_second_entry_of_day()

    def is_second_entry_of_day(self) -> bool:
        return self.number % 2 == 0

    def create_time(self) -> None:
        self.create_time_dict()

        self.start_time = time(**self.start_time_dict)
        self.stop_time = time(**self.stop_time_dict)

    def create_time_dict(self) -> None:
        hours = self.calculate_hours()
        minutes = self.calculate_minutes()
        seconds = self.calculate_seconds()

        self.create_start_time_dict(hours, minutes, seconds)
        self.create_stop_time_dict(hours, minutes, seconds)

    def create_start_time_dict(self, hours: dict, minutes: dict, seconds: dict) -> None:
        start_hour = hours["start"]
        start_minutes = minutes["start"]
        start_seconds = seconds["start"]

        self.start_time_dict = {"hour": start_hour, "minute": start_minutes, "second": start_seconds}

    def create_stop_time_dict(self, hours: dict, minutes: dict, seconds: dict) -> None:
        stop_hour = hours["stop"]
        stop_minutes = minutes["stop"]
        stop_seconds = seconds["stop"]

        self.stop_time_dict = {"hour": stop_hour, "minute": stop_minutes, "second": stop_seconds}

    def calculate_hours(self) -> dict:
        start_hour = random.randint(0, 11)
        stop_hour = random.randint(start_hour, 12)

        if self.is_second_entry_of_day():
            # Second entry of day should be in the afternoon, cannot add 12 to prevent times like 24:10:00 -> invalid
            start_hour += 11
            stop_hour += 11

        return {"start": start_hour, "stop": stop_hour}

    @staticmethod
    def calculate_minutes() -> dict:
        # Needs to be this low to prevent times like 00:60:14 -> invalid
        max_minutes = 58

        start_minutes = random.randint(0, max_minutes)
        stop_minutes = start_minutes + random.randint(1, 59 - start_minutes)

        return {"start": start_minutes, "stop": stop_minutes}

    @staticmethod
    def calculate_seconds() -> dict:
        # Needs to be this low to prevent times like 00:00:60 -> invalid
        max_seconds = 58

        start_seconds = random.randint(0, max_seconds)
        stop_seconds = start_seconds + random.randint(1, 59 - start_seconds)

        return {"start": start_seconds, "stop": stop_seconds}

    def create_work_hours(self) -> None:
        start_time = datetime.combine(datetime.min, self.start_time)
        stop_time = datetime.combine(datetime.min, self.stop_time)

        time_delta = stop_time - start_time
        self.work_hours = time_delta
