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

import pandas

from tests.BaseTestingClass import BaseTestingClass


class TrackerFileBaseTestingClass(BaseTestingClass):
    def setUp(self) -> None:
        super(TrackerFileBaseTestingClass, self).setUp()

    def check_for_correct_column_names(self) -> None:
        self.assertTrue(self.columns_names_are_correct())

    def columns_names_are_correct(self) -> bool:
        actual_column_names = self.get_actual_column_names()
        expected_column_names = self.tracker_file_handler.get_column_names()

        return actual_column_names == expected_column_names

    def get_actual_column_names(self) -> list:
        data_frame = pandas.read_csv(self.tracker_file_handler.tracker_file)
        return list(data_frame.columns)

    def get_contents_of_tracker_file_with_replaced_nans(self) -> pandas.DataFrame:
        data = self.get_contents_of_tracker_file()
        return data.fillna("")

    def get_contents_of_tracker_file(self) -> pandas.DataFrame:
        data_frame = pandas.read_csv(self.tracker_file_handler.tracker_file)
        return data_frame
