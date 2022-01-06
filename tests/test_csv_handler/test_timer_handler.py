import unittest
import re

from src.csv_handler.TimerHandler import TimerHandler
from src.exceptions.InvalidTimerModification import InvalidTimerModification

from .CSVBaseTestingClass import CSVBaseTestingClass


class TestTimerHandler(CSVBaseTestingClass):
    def setUp(self) -> None:
        super(TestTimerHandler, self).setUp()

        self.timer_handler = TimerHandler()
        self.datetime_pattern = re.compile(
            "\w{3}, \d{2} \d{4} at (\d{2}:){2}\d{2}"
        )
    
    def test_starting_a_new_timer(self) -> None:
        self.clean_and_init_tracker_file()
        start_time = self.timer_handler.start_timer()

        self.check_for_correct_column_names()

        file = self.get_contents_of_tracker_file_with_replaced_nans()

        self.assertTrue(self.datetime_pattern.match(file["start_time"][0]))

        self.assertEqual(file["start_time"][0], start_time)
        self.assertEqual(file["stop_time"][0], "")
        self.assertEqual(file["message"][0], "")

    def test_stopping_a_timer_with_empty_message(self) -> None:
        message = ""
        self.stop_created_timer(message)

    def test_stopping_a_timer_with_message(self) -> None:
        message = "Developed new feature for Tracker"
        self.stop_created_timer(message)

    def stop_created_timer(self, message: str) -> None:
        self.clean_and_init_tracker_file()

        start_time = self.timer_handler.start_timer()
        stop_time = self.timer_handler.stop_timer(message)

        self.check_for_correct_column_names()

        file = self.get_contents_of_tracker_file_with_replaced_nans()

        self.assertTrue(self.datetime_pattern.match(file["start_time"][0]))
        self.assertTrue(self.datetime_pattern.match(file["stop_time"][0]))

        self.assertEqual(file["start_time"][0], start_time)
        self.assertEqual(file["stop_time"][0], stop_time)
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


if __name__ == "__main__":
    unittest.main()
