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

from tracker.commands.filter.UnifyFilters import UnifyFilters

from ..CommandBaseTestingClass import CommandBaseTestingClass


class TestFilterCommand(CommandBaseTestingClass):
    def setUp(self) -> None:
        super(TestFilterCommand, self).setUp()

        self.unifiy_filters = UnifyFilters()

    def test_unifying_filters(self) -> None:
        actual_filters = self.unifiy_filters.unify(0, "0", 0, "")
        expected_filters = {"day": 0, "month": 0, "year": 0, "message": ""}

        self.assertEqual(actual_filters, expected_filters)

        actual_filters = self.unifiy_filters.unify(0, "0", 0, "")
        expected_filters = {"day": 0, "month": 0, "year": 0, "message": ""}

        self.assertEqual(actual_filters, expected_filters)

        actual_filters = self.unifiy_filters.unify(1, "1", 2022, "My message")
        expected_filters = {"day": 1, "month": 1, "year": 2022, "message": "My message"}

        self.assertEqual(actual_filters, expected_filters)

        actual_filters = self.unifiy_filters.unify(0, "January", 0, "")
        expected_filters = {"day": 0, "month": 1, "year": 0, "message": ""}

        self.assertEqual(actual_filters, expected_filters)

        actual_filters = self.unifiy_filters.unify(0, "Jan", 0, "")
        expected_filters = {"day": 0, "month": 1, "year": 0, "message": ""}

        self.assertEqual(actual_filters, expected_filters)

        self.assertRaises(ValueError, self.unifiy_filters.unify, 0, "January...", 0, "")
        self.assertRaises(ValueError, self.unifiy_filters.unify, -1,  "-1", 2022, "")


if __name__ == "__main__":
    unittest.main()
