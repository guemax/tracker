import unittest
import os
import re

import pandas

from src.csv_handler import CSVHandler


class TestCSVHandler(unittest.TestCase):
    def setUp(self) -> None:
        self.csv_handler = CSVHandler.CSVHandler()
        self.datetime_pattern = re.compile(
            "\w{3}, \d{2} \d{4} at (\d{2}:){2}\d{2}"
        )

    def test_inititalizing_tracker_file(self) -> None:
        self.clean_and_init_tracker_file()
        self.assertTrue(self.columns_names_are_correct())

    def columns_names_are_correct(self) -> bool:
        column_names = self.get_column_names()
        return column_names == ["start_time", "stop_time", "message"]

    def test_creating_a_new_entry(self) -> None:
        self.clean_and_init_tracker_file()
        self.csv_handler.create_new_entry()

        # Check for the column names
        self.assertTrue(self.columns_names_are_correct())

        file = self.get_contents_of_tracker_file()
        # Replace pandas 'nan' with an empty string for simple assertions
        file = file.fillna("")

        self.assertTrue(self.datetime_pattern.match(file["start_time"][0]))
        self.assertEqual(file["stop_time"][0], "")
        self.assertEqual(file["message"][0], "")

    def test_finishing_a_created_entry_with_empty_message(self) -> None:
        message = ""
        self.finishing_a_created_entry(message)

    def test_finishing_a_created_entry_with_message(self) -> None:
        message = "Developed new feature for Tracker"
        self.finishing_a_created_entry(message)

    def finishing_a_created_entry(self, message: str) -> None:
        self.clean_and_init_tracker_file()

        start_time = self.csv_handler.create_new_entry()
        stop_time = self.csv_handler.finish_created_entry(message)

        # Check for the column names
        self.assertTrue(self.columns_names_are_correct())

        file = self.get_contents_of_tracker_file()
        # Replace pandas 'nan' with an empty string for simple assertions
        file = file.fillna("")

        self.assertTrue(self.datetime_pattern.match(file["start_time"][0]))
        self.assertTrue(self.datetime_pattern.match(file["stop_time"][0]))

        self.assertEqual(file["start_time"][0], start_time)
        self.assertEqual(file["stop_time"][0], stop_time)
        self.assertEqual(file["message"][0], message)

    def test_checking_if_tracker_file_exists(self) -> None:
        self.remove_tracker_file()
        self.assertFalse(self.csv_handler.tracker_file_exists())

        self.csv_handler.create_tracker_file()
        self.assertTrue(self.csv_handler.tracker_file_exists())

    def remove_tracker_file(self) -> None:
        try:
            os.remove(self.csv_handler.tracker_file)
        except FileNotFoundError:
            # File is not existing, that's good, nothing to do for us.
            pass

    def clean_and_init_tracker_file(self) -> None:
        self.remove_tracker_file()
        self.csv_handler.init_tracker_csv_file()

    def get_column_names(self) -> list:
        data_frame = pandas.read_csv(self.csv_handler.tracker_file)
        return list(data_frame.columns)

    def get_contents_of_tracker_file(self) -> pandas.DataFrame:
        data_frame = pandas.read_csv(self.csv_handler.tracker_file)
        return data_frame


if __name__ == "__main__":
    unittest.main()
