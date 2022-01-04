import unittest
from src.csv_handler import CSVHandler


class TestCSVHandler(unittest.TestCase):
    def setUp(self) -> None:
        self.csv_handler = CSVHandler.CSVHandler()

    def test_inititalizing_tracker_file(self):
        self.csv_handler.init_tracker_csv_file()

        with open(self.csv_handler.tracker_file, "r") as f:
            file = f.read()
            file = file.strip()

        self.assertEqual(file, "start_time,stop_time,message")
