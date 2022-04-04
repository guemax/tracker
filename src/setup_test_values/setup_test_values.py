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
import random

import numpy
import pandas
from numpy import ndarray

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

        number_of_entries = self.get_number_of_entries_to_create()
        dates = self.get_dates_to_create(number_of_entries)

        for i in range(0, number_of_entries):
            entries += self.__build_entry(dates[i], i)

        # Remove last entry of entries if we need an odd number of entries
        if self._number_of_entries % 2 != 0:
            list_of_entries = entries.split("\n")
            entries_without_last_one = list_of_entries[:-2] + list_of_entries[-1:]
            entries = "\n".join(entries_without_last_one)

        return entries

    def get_number_of_entries_to_create(self) -> int:
        if self._number_of_entries % 2 == 0:
            return self._number_of_entries
        else:
            # Because we create two entries per date, we need an even number of entries to divide them by two
            # We remove the last entry before writing them to the tracker.csv file later
            return self._number_of_entries + 1

    @staticmethod
    def get_dates_to_create(number_of_entries: int) -> ndarray:
        # Calculate how may days we need to generate

        # Need to add one day to make sure our dates start today and not yesterday
        today = datetime.datetime.now() + datetime.timedelta(days=1)

        # Divide by two because we double the entries later do get 'number_of_entries'
        n_days_ago = today - datetime.timedelta(days=number_of_entries / 2)

        # Generate dates
        dates = pandas.date_range(n_days_ago, today - datetime.timedelta(days=1), freq="d").to_pydatetime()

        # Duplicate the dates for making two entries per day
        dates = numpy.repeat(dates, 2)

        return dates

    def __build_entry(self, date: datetime.datetime, number: int) -> str:
        message = random.choice(self.__messages)
        return self.__entry.build(date, message, number)
