import unittest
import shutil
import os

from src.csv import CSVHandler
from .CSVBaseTestingClass import CSVBaseTestingClass


class TestCSVHandler(CSVBaseTestingClass):
    def setUp(self) -> None:
        self.csv_handler = CSVHandler.CSVHandler()

    def test_inititalizing_tracker_file(self) -> None:
        self.clean_and_init_tracker_file()
        self.assertTrue(self.columns_names_are_correct())

    def test_inititalizing_tracker_file_if_it_already_exists(self) -> None:
        self.clean_and_init_tracker_file()
        self.csv_handler.init_tracker_csv_file()
        self.assertTrue(self.columns_names_are_correct())

    def test_creating_the_files_folder(self):
        self.remove_files_folder()
        self.assertFalse(os.path.isdir(self.csv_handler.tracker_folder))

        self.csv_handler.create_files_folder_if_not_exists()
        self.assertTrue(os.path.isdir(self.csv_handler.tracker_folder))

    def remove_files_folder(self):
        try:
            shutil.rmtree(self.csv_handler.tracker_folder)
        except FileNotFoundError:
            # File (folder) is not existing, that's good, nothing to do for us.
            pass

    def test_checking_if_tracker_file_exists(self) -> None:
        self.remove_tracker_file()
        self.assertFalse(self.csv_handler.tracker_file_exists())

        self.csv_handler.create_tracker_file()
        self.assertTrue(self.csv_handler.tracker_file_exists())


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
