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

from tracker.handler.filter_handler.FilterHandler import FilterHandler


class TestFilterHandler(unittest.TestCase):
    def setUp(self) -> None:
        super(TestFilterHandler, self).setUp()

        self.filter_handler = FilterHandler(filters=[])

    def test_removing_unused_filters(self) -> None:
        self.check_for_removed_filters([0, 0, 0, ""], [])
        self.check_for_removed_filters([1, 0, 0, ""], [1])
        self.check_for_removed_filters([0, 7, 0, ""], [7])
        self.check_for_removed_filters([0, 0, 2022, ""], [2022])
        self.check_for_removed_filters([0, 0, 0, "My message"], ["My message"])
        self.check_for_removed_filters([1, 7, 0, ""], [1, 7])
        self.check_for_removed_filters([0, 0, 2022, "My message"], [2022, "My message"])
        self.check_for_removed_filters([1, 0, 0, "My message"], [1, "My message"])
        self.check_for_removed_filters([0, 7, 2022, ""], [7, 2022])
        self.check_for_removed_filters([1, 7, 2022, ""], [1, 7, 2022])
        self.check_for_removed_filters([0, 7, 2022, "My message"], [7, 2022, "My message"])
        self.check_for_removed_filters([1, 7, 2022, "My new message"], [1, 7, 2022, "My new message"])

    def check_for_removed_filters(self, filters: list, expected_cleaned_filters) -> None:
        self.filter_handler.__init__(filters)
        actual_cleaned_filters = self.filter_handler.remove_unused_filters()

        self.assertEqual(expected_cleaned_filters, actual_cleaned_filters)




if __name__ == "__main__":
    unittest.main()
