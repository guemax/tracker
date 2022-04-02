"""This file is part of tracker.
tracker is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
tracker is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with tracker. If not, see <http://www.gnu.org/licenses/>.
"""

import shutil
import unittest

from tracker.csv.CSVHandler import CSVHandler
from tracker.setup_test_values.setup_test_values import SetupTestValues


class BaseTestingClass(unittest.TestCase):
    def setUp(self) -> None:
        self.csv_handler = CSVHandler()
        self.set_upper = SetupTestValues()

    def remove_files_folder_and_init_tracker_file(self) -> None:
        self.remove_files_folder_and_its_contents()
        self.csv_handler.init_tracker_csv_file()

    def remove_files_folder_and_its_contents(self) -> None:
        shutil.rmtree(self.csv_handler.tracker_folder, ignore_errors=True)

    def setup_test_values(self, number_of_entries: int = 4) -> None:
        self.set_upper.set_number_of_entries(number_of_entries)
        self.set_upper.setup()
