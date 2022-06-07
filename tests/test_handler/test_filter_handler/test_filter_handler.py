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
        filters = [1, 7, 2022, "My new message"]
        self.filter_handler.__init__(filters)
        cleaned_filters = self.filter_handler.remove_unused_filters()

        self.assertEqual(filters, cleaned_filters)
        self.assertEqual(len(cleaned_filters), 4)

        filters = [0, 0, 0, ""]
        self.filter_handler.__init__(filters)
        cleaned_filters = self.filter_handler.remove_unused_filters()

        self.assertNotEqual(filters, cleaned_filters)
        self.assertEqual(cleaned_filters, [])
        self.assertEqual(len(cleaned_filters), 0)

        filters = [1, 0, 0, ""]
        self.filter_handler.__init__(filters)
        cleaned_filters = self.filter_handler.remove_unused_filters()

        self.assertNotEqual(filters, cleaned_filters)
        self.assertEqual(cleaned_filters, [1])
        self.assertEqual(len(cleaned_filters), 1)

        filters = [0, 7, 0, ""]
        self.filter_handler.__init__(filters)
        cleaned_filters = self.filter_handler.remove_unused_filters()

        self.assertNotEqual(filters, cleaned_filters)
        self.assertEqual(cleaned_filters, [7])
        self.assertEqual(len(cleaned_filters), 1)

        filters = [0, 0, 2022, ""]
        self.filter_handler.__init__(filters)
        cleaned_filters = self.filter_handler.remove_unused_filters()

        self.assertNotEqual(filters, cleaned_filters)
        self.assertEqual(cleaned_filters, [2022])
        self.assertEqual(len(cleaned_filters), 1)

        filters = [0, 0, 0, "My message"]
        self.filter_handler.__init__(filters)
        cleaned_filters = self.filter_handler.remove_unused_filters()

        self.assertNotEqual(filters, cleaned_filters)
        self.assertEqual(cleaned_filters, ["My message"])
        self.assertEqual(len(cleaned_filters), 1)

        filters = [1, 7, 0, ""]
        self.filter_handler.__init__(filters)
        cleaned_filters = self.filter_handler.remove_unused_filters()

        self.assertNotEqual(filters, cleaned_filters)
        self.assertEqual(cleaned_filters, [1, 7])
        self.assertEqual(len(cleaned_filters), 2)

        filters = [0, 0, 2022, "My message"]
        self.filter_handler.__init__(filters)
        cleaned_filters = self.filter_handler.remove_unused_filters()

        self.assertNotEqual(filters, cleaned_filters)
        self.assertEqual(cleaned_filters, [2022, "My message"])
        self.assertEqual(len(cleaned_filters), 2)

        filters = [1, 0, 0, "My message"]
        self.filter_handler.__init__(filters)
        cleaned_filters = self.filter_handler.remove_unused_filters()

        self.assertNotEqual(filters, cleaned_filters)
        self.assertEqual(cleaned_filters, [1, "My message"])
        self.assertEqual(len(cleaned_filters), 2)

        filters = [0, 7, 2022, ""]
        self.filter_handler.__init__(filters)
        cleaned_filters = self.filter_handler.remove_unused_filters()

        self.assertNotEqual(filters, cleaned_filters)
        self.assertEqual(cleaned_filters, [7, 2022])
        self.assertEqual(len(cleaned_filters), 2)

        filters = [1, 7, 2022, ""]
        self.filter_handler.__init__(filters)
        cleaned_filters = self.filter_handler.remove_unused_filters()

        self.assertNotEqual(filters, cleaned_filters)
        self.assertEqual(cleaned_filters, [1, 7, 2022])
        self.assertEqual(len(cleaned_filters), 3)

        filters = [0, 7, 2022, "My message"]
        self.filter_handler.__init__(filters)
        cleaned_filters = self.filter_handler.remove_unused_filters()

        self.assertNotEqual(filters, cleaned_filters)
        self.assertEqual(cleaned_filters, [7, 2022, "My message"])
        self.assertEqual(len(cleaned_filters), 3)


if __name__ == "__main__":
    unittest.main()
