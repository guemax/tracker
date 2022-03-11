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
import re

from tracker.handler.timer_handler.TimerHandler import TimerHandler
from tracker.exceptions.InvalidTimerModification import InvalidTimerModification

from tests.test_csv.CSVBaseTestingClass import CSVBaseTestingClass


class TestTimerHandler(CSVBaseTestingClass):
    def setUp(self) -> None:
        super(TestTimerHandler, self).setUp()

        self.timer_handler = TimerHandler()
        self.date_pattern = re.compile("\w{3}, \d{2} \d{4}")
        self.time_pattern = re.compile("(\d{2}:){2}\d{2}")
        self.work_hour_pattern = re.compile("(\d{1,2}:){2}\d{2}")

    def test_starting_a_new_timer(self) -> None:
        self.clean_and_init_tracker_file()

        time = self.timer_handler.start_timer()
        start_date = time[0]
        start_time = time[1]

        self.check_for_correct_column_names()

        file = self.get_contents_of_tracker_file_with_replaced_nans()

        self.assertTrue(self.date_pattern.match(file["start_date"][0]))
        self.assertTrue(self.time_pattern.match(file["start_time"][0]))

        self.assertEqual(file["start_date"][0], start_date)
        self.assertEqual(file["start_time"][0], start_time)
        self.assertEqual(file["stop_time"][0], "")
        self.assertEqual(file["work_hours"][0], "")
        self.assertEqual(file["message"][0], "")

    def test_stopping_a_timer_with_empty_message(self) -> None:
        message = ""
        self.stop_created_timer(message)

    def test_stopping_a_timer_with_message(self) -> None:
        message = "Developed new feature for Tracker"
        self.stop_created_timer(message)

    def stop_created_timer(self, message: str) -> None:
        self.clean_and_init_tracker_file()

        time_1 = self.timer_handler.start_timer()
        time_2 = self.timer_handler.stop_timer(message)

        start_date = time_1[0]
        start_time = time_1[1]
        stop_date = time_2[0]
        stop_time = time_2[1]

        work_hours = time_2[2]

        self.check_for_correct_column_names()

        file = self.get_contents_of_tracker_file_with_replaced_nans()

        self.assertTrue(self.date_pattern.match(file["start_date"][0]))
        self.assertTrue(self.date_pattern.match(file["stop_date"][0]))

        self.assertTrue(self.time_pattern.match(file["start_time"][0]))
        self.assertTrue(self.time_pattern.match(file["stop_time"][0]))
        self.assertTrue(self.work_hour_pattern.match(file["work_hours"][0]))

        self.assertEqual(file["start_date"][0], start_date)
        self.assertEqual(file["start_time"][0], start_time)
        self.assertEqual(file["stop_date"][0], stop_date)
        self.assertEqual(file["stop_time"][0], stop_time)
        self.assertEqual(file["work_hours"][0], work_hours)
        self.assertEqual(file["message"][0], message)

    def test_unfinished_entry_present(self):
        self.clean_and_init_tracker_file()

        self.assertFalse(self.timer_handler.unfinished_entry_present())

        self.timer_handler.start_timer()
        self.assertTrue(self.timer_handler.unfinished_entry_present())

        self.timer_handler.stop_timer(message="")
        self.assertFalse(self.timer_handler.unfinished_entry_present())
    
    def test_starting_timer_when_one_already_exists(self) -> None:
        self.clean_and_init_tracker_file()

        # Should not throw an exception
        self.timer_handler.start_timer()

        # There is already an existing timer!
        self.assertRaises(InvalidTimerModification, self.timer_handler.start_timer)

        # That should not work either if you try it again ;-)
        self.assertRaises(InvalidTimerModification, self.timer_handler.start_timer)

    def test_stopping_timer_when_no_one_already_exists(self) -> None:
        self.clean_and_init_tracker_file()

        # There is no timer yet, throws an exception
        self.assertRaises(InvalidTimerModification, self.timer_handler.stop_timer, "")

        # Should not throw an exception
        self.timer_handler.start_timer()
        self.timer_handler.stop_timer(message="")

        # Timer has already been stopped
        self.assertRaises(InvalidTimerModification, self.timer_handler.stop_timer, "")

        # That should not work either if you try it again ;-)
        self.assertRaises(InvalidTimerModification, self.timer_handler.stop_timer, "")


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
