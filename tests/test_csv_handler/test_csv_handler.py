import unittest
import os
import re

import pandas

from src.csv_handler import CSVHandler


class TestCSVHandler(unittest.TestCase):
    def setUp(self) -> None:
        self.csv_handler = CSVHandler.CSVHandler()

    def test_inititalizing_tracker_file(self) -> None:
        self.clean_and_init_tracker_file()
        self.assertTrue(self.columns_names_are_correct())

    def columns_names_are_correct(self) -> bool:
        column_names = self.get_column_names()
        return column_names == ["start_time", "stop_time", "message"]

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


if __name__ == "__main__":
    unittest.main()
