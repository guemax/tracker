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

from tracker.handler.tracker_file_handler.TrackerFileAttributes import TrackerFileAttributes


class TestTrackerFileAttributes(unittest.TestCase):
    def setUp(self) -> None:
        self.tracker_file_atrributes = TrackerFileAttributes()
        self.tracker_file_atrributes.__init__()

    def test_column_names_not_none(self) -> None:
        self.assertIsNotNone(self.tracker_file_atrributes.column_names)

    def test_column_names_is_list(self) -> None:
        self.assertIsInstance(self.tracker_file_atrributes.column_names, list)

    def test_column_names_is_list_with_lenght_greater_than_zero(self) -> None:
        self.assertGreater(len(self.tracker_file_atrributes.column_names), 0)

    def test_column_names_have_right_type(self) -> None:
        for name in self.tracker_file_atrributes.column_names:
            self.assertIsInstance(name, str)

    def test_tracker_folder_name_is_correct(self) -> None:
        self.assertEqual(self.tracker_file_atrributes.tracker_folder, "files")

    def test_tracker_file_is_correct(self) -> None:
        self.assertEqual(self.tracker_file_atrributes.tracker_file, "files/tracker.csv")


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
