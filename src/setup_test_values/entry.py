import random
from datetime import datetime


class Entry:
    def __init__(self) -> None:
        self.start_date = ""
        self.start_time = ""

        self.stop_date = ""
        self.stop_time = ""

        self.work_hours = ""

        self.message = ""

        self.number = 0

        self.month = "Jan"
        self.year = "2022"

    def create_datetime(self) -> None:
        # CREATE HOURS
        start_hour = random.randint(0, 11)
        stop_hour = random.randint(start_hour, 12)

        if self.number % 2 == 0:
            # Second entry of day
            start_hour += 11
            stop_hour += 11

        # Just leave them as they are
        max_minutes = 58
        max_seconds = 58

        # CREATE MINUTES
        start_minutes = random.randint(0, max_minutes)
        stop_minutes = start_minutes + random.randint(1, 59 - start_minutes)

        # CREATE SECONDS
        start_seconds = random.randint(0, max_seconds)
        stop_seconds = start_seconds + random.randint(1, 59 - start_seconds)

        # CREATE DAY NUMBER
        if self.number % 2 == 0:
            date = int(self.number / 2)
        else:
            date = int((self.number + 1) / 2)

        # BUILD FULL DATE/TIME
        self.start_date = f"\"{self.month}, {date} {self.year}\""
        self.start_time = f"{start_hour:02d}:{start_minutes:02d}:{start_seconds:02d}"

        self.stop_date = self.start_date
        self.stop_time = f"{stop_hour:02d}:{stop_minutes:02d}:{stop_seconds:02d}"

    def build(self, messages: list, number: int) -> str:
        self.number = number

        self.create_datetime()
        self.create_work_hours()
        # BUILD MESSAGE
        self.message = random.choice(messages)

        # BUILD FINAL ENTRY
        line = f"{self.start_date},{self.start_time},{self.stop_date},{self.stop_time},{self.work_hours},{self.message}\n"
        return line

    def create_work_hours(self) -> None:
        time_format = "%H:%M:%S"

        start_time = datetime.strptime(self.start_time, time_format)
        stop_time = datetime.strptime(self.stop_time, time_format)

        time_delta = stop_time - start_time
        self.work_hours = time_delta
