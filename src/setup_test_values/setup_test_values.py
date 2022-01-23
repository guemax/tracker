import datetime
import random

import numpy
import pandas

from src.csv import CSVHandler
from .entry import Entry


class SetupTestValues:
    def __init__(self) -> None:
        self.__csv_handler = CSVHandler.CSVHandler()
        self.__csv_handler.create_files_folder_if_not_exists()

        self._number_of_entries = 4

        self.__messages = [
            "", "Working on Tracker", "Developing new features",
            "Fixing bugs", "Adding tests", "Refactoring"
        ]

        self.__entry = Entry()

    def set_number_of_entries(self, new_number: int):
        if new_number < 0:
            raise ValueError("The number of entries to create cannot be negative.")

        self._number_of_entries = new_number

    def setup(self) -> None:
        with open(self.__csv_handler.tracker_file, "w") as f:
            f.write(self.__header())
            f.write(self.__entries())

    def __header(self) -> str:
        return ",".join(self.__csv_handler.column_names) + "\n"

    def __entries(self) -> str:
        entries = ""
        number_of_entries = self._number_of_entries

        if number_of_entries % 2 != 0:
            number_of_entries += 1

        # Two entries per date, so two times fewer dates
        number_of_entries /= 2

        # Number of days in the past
        today = datetime.datetime.now()
        n_days_ago = today - datetime.timedelta(days=number_of_entries)

        # Generate dates
        dates = pandas.date_range(n_days_ago, today - datetime.timedelta(days=1), freq="d").to_pydatetime()

        # Duplicate the dates
        dates = numpy.repeat(dates, 2)

        for i in range(0, len(dates)):
            entries += self.__build_entry(dates[i], i)

        if self._number_of_entries % 2 != 0:
            entries = "\n".join(entries.split("\n")[:-2])
            entries += "\n"

        return entries

    def __build_entry(self, date: datetime.datetime, number: int) -> str:
        message = random.choice(self.__messages)
        return self.__entry.build(date, message, number)
