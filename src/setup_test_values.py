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
import random

import click
import num2words

from .csv import CSVHandler
from src.console_logger.console_logger import info, warn


class SetupTestValues:
    def __init__(self) -> None:
        self.csv_handler = CSVHandler.CSVHandler()
        self.csv_handler.create_files_folder_if_not_exists()

        self.number_of_entries = 4

        self.month = "Jan"
        self.year = "2022"

        self.messages = [
            "", "Working on Tracker", "Developing new features",
            "Fixing bugs", "Adding tests", "Refactoring"
        ]

    def set_number_of_entries(self, new_number: int):
        if new_number < 0:
            raise ValueError("The number of entries to create cannot be negative.")

        self.number_of_entries = new_number

    def setup(self) -> None:
        with open(self.csv_handler.tracker_file, "w") as f:
            f.write(self.header())
            f.write(self.test_value_lines())

    def header(self) -> str:
        return ",".join(self.csv_handler.column_names) + "\n"

    def test_value_lines(self) -> str:
        lines = ""

        for i in range(1, self.number_of_entries + 1):
            lines += self.build_test_value_line(i)

        return lines

    def build_test_value_line(self, number: int) -> str:
        start_hour = number
        stop_hour = number + random.choice([0, 1])

        # Just leave it as it is
        max_start_seconds = 58

        start_minutes = random.randint(0, max_start_seconds)
        stop_minutes = start_minutes + random.randint(1, 59 - start_minutes)

        start_seconds = random.randint(0, max_start_seconds)
        stop_seconds = start_seconds + random.randint(1, 59 - start_seconds)

        if number % 2 == 0:
            date = int(number / 2)
        else:
            date = int((number + 1) / 2)

        start_date = f"\"{self.month}, {date} {self.year}\""
        start_time = f"{start_hour:02d}:{start_minutes:02d}:{start_seconds:02d}"

        stop_date = start_date
        stop_time = f"{stop_hour:02d}:{stop_minutes:02d}:{stop_seconds:02d}"

        date_format = "%H:%M:%S"
        work_hours = datetime.strptime(stop_time, date_format) - datetime.strptime(start_time, date_format)

        message = random.choice(self.messages)

        line = f"{start_date},{start_time},{stop_date},{stop_time},{work_hours},{message}\n"
        return line


def handler_invalid_number_of_entries() -> None:
    warn("The number of entries cannot be negative. Please specify a value greater than or equal zero.\n"
         "EXIT")
    exit(-1)


@click.command()
@click.option("-e", "--entries", help="Number of entries to create", type=int, default=4)
def setup_test_values(entries: int) -> None:
    set_upper = SetupTestValues()

    try:
        set_upper.set_number_of_entries(entries)
    except ValueError:
        handler_invalid_number_of_entries()

    set_upper.setup()

    entries_as_word = num2words.num2words(entries)
    message = "\nSuccesfully setup"
    if entries == 1:
        info(f"{message} one entry.")
    else:
        info(f"{message} {entries_as_word} entries.")
    info("OK")


if __name__ == "__main__":  # pragma: no cover
    setup_test_values()
