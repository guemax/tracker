import unittest
import os
import re

from src.csv_handler import CSVHandler


class NotAllowed(Exception):
    pass


class TestCSVHandler(unittest.TestCase):
    def setUp(self) -> None:
        self.csv_handler = CSVHandler.CSVHandler()
        self.pattern_new_entry = re.compile(
            "start_time,stop_time,message\n\"\w{3}, \d{2} \d{4} at (\d{2}:){2}\d{2}\",,"
        )

    def test_inititalizing_tracker_file(self):
        self.clean_and_init_tracker_file()

        file = self.get_contents_of_tracker_file()
        self.assertEqual(file, "start_time,stop_time,message")

    def test_creating_a_new_entry(self):
        self.clean_and_init_tracker_file()

        self.csv_handler.create_new_entry()

        file = self.get_contents_of_tracker_file()
        self.assertTrue(self.pattern_new_entry.match(file))

    def test_checking_if_tracker_file_exists(self):
        self.remove_tracker_file()
        self.assertFalse(self.csv_handler.tracker_file_exists())

        self.csv_handler.create_tracker_file()
        self.assertTrue(self.csv_handler.tracker_file_exists())

    def remove_tracker_file(self):
        try:
            os.remove(self.csv_handler.tracker_file)
        except FileNotFoundError:
            # File is not existing, that's good, nothing to do for us.
            pass

    def clean_and_init_tracker_file(self):
        self.remove_tracker_file()
        self.csv_handler.init_tracker_csv_file()

    def get_contents_of_tracker_file(self) -> str:
        with open(self.csv_handler.tracker_file, "r") as f:
            file = f.read()
            file = file.strip()

        return file


if __name__ == "__main__":
    unittest.main()
