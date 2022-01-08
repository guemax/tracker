import unittest

from src.csv import CSVHandler
from .CSVBaseTestingClass import CSVBaseTestingClass


class TestCSVHandler(CSVBaseTestingClass):
    def setUp(self) -> None:
        self.csv_handler = CSVHandler.CSVHandler()

    def test_inititalizing_tracker_file(self) -> None:
        self.clean_and_init_tracker_file()
        self.assertTrue(self.columns_names_are_correct())

    def test_checking_if_tracker_file_exists(self) -> None:
        self.remove_tracker_file()
        self.assertFalse(self.csv_handler.tracker_file_exists())

        self.csv_handler.create_tracker_file()
        self.assertTrue(self.csv_handler.tracker_file_exists())


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
