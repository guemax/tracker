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

from tests.BaseTestingClass import BaseTestingClass

from tracker.handler.filter_handler.FilterHandler import FilterHandler


class TestFilterHandler(BaseTestingClass):
    def setUp(self) -> None:
        super(TestFilterHandler, self).setUp()

        self.filter_handler = FilterHandler()

    def test_removing_unused_filters(self) -> None:
        self.check_for_removed_filters(
            {"day": 0, "month": 0, "year": 0, "message": ""},
            {}
        )
        self.check_for_removed_filters(
            {"day": 1, "month": 0, "year": 0, "message": ""},
            {"day": 1}
        )
        self.check_for_removed_filters(
            {"day": 0, "month": 7, "year": 0, "message": ""},
            {"month": 7}
        )
        self.check_for_removed_filters(
            {"day": 0, "month": 0, "year": 2022, "message": ""},
            {"year": 2022}
        )
        self.check_for_removed_filters(
            {"day": 0, "month": 0, "year": 0, "message": "My message"},
            {"message": "My message"}
        )
        self.check_for_removed_filters(
            {"day": 1, "month": 7, "year": 0, "message": ""},
            {"day": 1, "month": 7}
        )
        self.check_for_removed_filters(
            {"day": 0, "month": 0, "year": 2022, "message": "My message"},
            {"year": 2022, "message": "My message"})
        self.check_for_removed_filters(
            {"day": 1, "month": 0, "year": 0, "message": "My message"},
            {"day": 1, "message": "My message"}
        )
        self.check_for_removed_filters(
            {"day": 0, "month": 7, "year": 2022, "message": ""},
            {"month": 7, "year": 2022}
        )
        self.check_for_removed_filters(
            {"day": 1, "month": 7, "year": 2022, "message": ""},
            {"day": 1, "month": 7, "year": 2022}
        )
        self.check_for_removed_filters(
            {"day": 0, "month": 7, "year": 2022, "message": "My message"},
            {"month": 7, "year": 2022, "message": "My message"}
        )
        self.check_for_removed_filters(
            {"day": 1, "month": 7, "year": 2022, "message": "My new message"},
            {"day": 1, "month": 7, "year": 2022, "message": "My new message"}
        )

    def check_for_removed_filters(self, filters: dict, expected_cleaned_filters) -> None:
        actual_cleaned_filters = self.filter_handler.remove_unused_filters_from(filters)

        self.assertEqual(expected_cleaned_filters, actual_cleaned_filters)

    def test_filtering_items(self) -> None:
        self.setup_test_values(10)


if __name__ == "__main__":
    unittest.main()
