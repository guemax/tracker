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
import shutil
import os

from src.csv import CSVHandler
from .CSVBaseTestingClass import CSVBaseTestingClass


class TestCSVHandler(CSVBaseTestingClass):
    def setUp(self) -> None:
        self.csv_handler = CSVHandler.CSVHandler()

    def test_inititalizing_tracker_file(self) -> None:
        self.clean_and_init_tracker_file()
        self.assertTrue(self.columns_names_are_correct())

    def test_inititalizing_tracker_file_if_it_already_exists(self) -> None:
        self.clean_and_init_tracker_file()
        self.csv_handler.init_tracker_csv_file()
        self.assertTrue(self.columns_names_are_correct())

    def test_creating_the_files_folder(self):
        self.remove_files_folder()
        self.assertFalse(os.path.isdir(self.csv_handler.tracker_folder))

        self.csv_handler.create_files_folder_if_not_exists()
        self.assertTrue(os.path.isdir(self.csv_handler.tracker_folder))

    def remove_files_folder(self):
        # Ignore errors, so it won't raise an exception if the folder does not exist.
        shutil.rmtree(self.csv_handler.tracker_folder, ignore_errors=True)

    def test_checking_if_tracker_file_exists(self) -> None:
        self.remove_tracker_file()
        self.assertFalse(self.csv_handler.tracker_file_exists())

        self.csv_handler.create_tracker_file()
        self.assertTrue(self.csv_handler.tracker_file_exists())


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
