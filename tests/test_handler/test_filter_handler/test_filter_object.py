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

from tracker.handler.filter_handler.FilterObject import FilterObject


class TestFilterHandler(BaseTestingClass):
    def setUp(self) -> None:
        super(TestFilterHandler, self).setUp()

        self.filter_handler = FilterObject()

    def test_creating_dict(self) -> None:
        self.check_created_dict(
            {"day": 0, "month": "", "year": 0, "message": ""},
            {"day": 0, "month": "", "year": 0, "message": ""}
        )

        self.check_created_dict(
            {"day": 1, "month": "", "year": 0, "message": ""},
            {"day": 1, "month": "", "year": 0, "message": ""}
        )

        self.check_created_dict(
            {"day": 0, "month": "1", "year": 0, "message": ""},
            {"day": 0, "month": "Jan", "year": 0, "message": ""}
        )

        self.check_created_dict(
            {"day": 0, "month": "January", "year": 0, "message": ""},
            {"day": 0, "month": "Jan", "year": 0, "message": ""}
        )

        self.check_created_dict(
            {"day": 0, "month": "Jan", "year": 0, "message": ""},
            {"day": 0, "month": "Jan", "year": 0, "message": ""}
        )

        self.check_created_dict(
            {"day": 0, "month": "", "year": 2022, "message": ""},
            {"day": 0, "month": "", "year": 2022, "message": ""}
        )

        self.check_created_dict(
            {"day": 0, "month": "", "year": 0, "message": "My message"},
            {"day": 0, "month": "", "year": 0, "message": "My message"}
        )

        self.check_created_dict(
            {"day": 1, "month": "1", "year": 2022, "message": "My message"},
            {"day": 1, "month": "Jan", "year": 2022, "message": "My message"}
        )

    def check_created_dict(self, filters: dict, expected_dict: dict) -> None:
        day = filters["day"]
        month = filters["month"]
        year = filters["year"]
        message = filters["message"]

        self.filter_handler.__init__(day, month, year, message)
        actual_dict = self.filter_handler.get_dict()

        self.assertEqual(actual_dict, expected_dict)


if __name__ == "__main__":
    unittest.main()
