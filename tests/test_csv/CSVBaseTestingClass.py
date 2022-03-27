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

import unittest
import os

import pandas

from src.csv.CSVHandler import CSVHandler
from src.setup_test_values.setup_test_values import SetupTestValues


class CSVBaseTestingClass(unittest.TestCase):
    def setUp(self) -> None:
        self.csv_handler = CSVHandler()
        self.set_upper = SetupTestValues()

    def check_for_correct_column_names(self) -> None:
        self.assertTrue(self.columns_names_are_correct())

    def columns_names_are_correct(self) -> bool:
        column_names = self.get_column_names()
        return column_names == self.csv_handler.get_column_names()

    def get_column_names(self) -> list:
        data_frame = pandas.read_csv(self.csv_handler.tracker_file)
        return list(data_frame.columns)

    def clean_and_init_tracker_file(self) -> None:
        self.remove_tracker_file()
        self.csv_handler.init_tracker_csv_file()

    def remove_tracker_file(self) -> None:
        try:
            os.remove(self.csv_handler.tracker_file)
        except FileNotFoundError:
            # File is not existing, that's good, nothing to do for us.
            pass

    def get_contents_of_tracker_file_with_replaced_nans(self) -> pandas.DataFrame:
        data = self.get_contents_of_tracker_file()
        data = data.fillna("")

        return data

    def get_contents_of_tracker_file(self) -> pandas.DataFrame:
        data_frame = pandas.read_csv(self.csv_handler.tracker_file)
        return data_frame

    def setup_test_values(self, number_of_entries: int = 4) -> None:
        self.set_upper.set_number_of_entries(number_of_entries)
        self.set_upper.setup()
