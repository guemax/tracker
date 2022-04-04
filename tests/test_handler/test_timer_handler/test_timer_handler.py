"""This file is part of tracker.
Tracker is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
Tracker is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with tracker. If not, see <http://www.gnu.org/licenses/>.
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

    def test_starting_the_first_timer(self) -> None:
        self.remove_files_folder_and_init_tracker_file()

        self.check_for_started_timer()

    def check_for_started_timer(self) -> None:
        start_datetime = self.timer_handler.start_timer()
        expected_start_date = start_datetime[0]
        expected_start_time = start_datetime[1]

        self.check_for_correct_column_names()

        dataframe = self.get_contents_of_tracker_file_with_replaced_nans()
        last_row = dataframe.iloc[-1]

        actual_start_date = last_row["start_date"]
        actual_start_time = last_row["start_time"]

        actual_stop_time = last_row["stop_time"]
        actual_work_hours = last_row["work_hours"]
        actual_message = last_row["message"]

        self.assertTrue(self.date_pattern.match(actual_start_date))
        self.assertTrue(self.time_pattern.match(actual_start_time))

        self.assertEqual(actual_start_date, expected_start_date)
        self.assertEqual(actual_start_time, expected_start_time)
        self.assertEqual(actual_stop_time, "")
        self.assertEqual(actual_work_hours, "")
        self.assertEqual(actual_message, "")

    def test_starting_the_second_timer(self) -> None:
        self.remove_files_folder_and_init_tracker_file()

        self.set_upper.set_number_of_entries(1)
        self.set_upper.setup()

        self.check_for_started_timer()

    def test_stopping_first_timer_with_empty_message(self) -> None:
        self.remove_files_folder_and_init_tracker_file()

        message = ""
        self.check_for_stopped_timer(message)

    def check_for_stopped_timer(self, message: str) -> None:
        start_datetime = self.timer_handler.start_timer()
        stop_datetime = self.timer_handler.stop_timer(message)

        expected_start_date = start_datetime[0]
        expected_start_time = start_datetime[1]
        expected_stop_date = stop_datetime[0]
        expected_stop_time = stop_datetime[1]
        expected_work_hours = stop_datetime[2]
        expected_message = message

        self.check_for_correct_column_names()

        dataframe = self.get_contents_of_tracker_file_with_replaced_nans()
        last_row = dataframe.iloc[-1]

        actual_start_date = last_row["start_date"]
        actual_start_time = last_row["start_time"]
        actual_stop_date = last_row["stop_date"]
        actual_stop_time = last_row["stop_time"]
        actual_work_hours = last_row["work_hours"]
        actual_message = last_row["message"]

        self.assertTrue(self.date_pattern.match(actual_start_date))
        self.assertTrue(self.date_pattern.match(actual_stop_date))
        self.assertTrue(self.time_pattern.match(actual_start_time))
        self.assertTrue(self.time_pattern.match(actual_stop_time))

        self.assertTrue(self.work_hour_pattern.match(actual_work_hours))

        self.assertEqual(actual_start_date, expected_start_date)
        self.assertEqual(actual_start_time, expected_start_time)
        self.assertEqual(actual_stop_date, expected_stop_date)
        self.assertEqual(actual_stop_time, expected_stop_time)

        self.assertEqual(actual_work_hours, expected_work_hours)
        self.assertEqual(actual_message, expected_message)

    def test_stopping_first_timer_with_message(self) -> None:
        self.remove_files_folder_and_init_tracker_file()

        message = "Developed a new feature for tracker"
        self.check_for_stopped_timer(message)

    def test_stopping_second_timer_with_empty_message(self) -> None:
        self.remove_files_folder_and_init_tracker_file()

        self.set_upper.set_number_of_entries(1)
        self.set_upper.setup()

        message = ""
        self.check_for_stopped_timer(message)

    def test_stopping_second_timer_with_message(self) -> None:
        self.remove_files_folder_and_init_tracker_file()

        self.set_upper.set_number_of_entries(1)
        self.set_upper.setup()

        message = "Developed a new feature for tracker"
        self.check_for_stopped_timer(message)

    def test_unfinished_entry_present(self):
        self.remove_files_folder_and_init_tracker_file()

        self.assertFalse(self.timer_handler.unfinished_entry_present())

        self.timer_handler.start_timer()
        self.assertTrue(self.timer_handler.unfinished_entry_present())

        self.timer_handler.stop_timer(message="")
        self.assertFalse(self.timer_handler.unfinished_entry_present())
    
    def test_starting_timer_when_one_already_exists(self) -> None:
        self.remove_files_folder_and_init_tracker_file()

        # Should not throw an exception
        self.timer_handler.start_timer()

        # There is already an existing timer!
        self.assertRaises(InvalidTimerModification, self.timer_handler.start_timer)

        # That should not work either if you try it again ;-)
        self.assertRaises(InvalidTimerModification, self.timer_handler.start_timer)

    def test_stopping_timer_when_no_one_already_exists(self) -> None:
        self.remove_files_folder_and_init_tracker_file()

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
