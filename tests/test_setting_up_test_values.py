import unittest

from src.setup_test_values import setup_test_values

from tests.test_csv.CSVBaseTestingClass import CSVBaseTestingClass


class TestSettingUpTestValues(CSVBaseTestingClass):
    def setUp(self) -> None:
        super(TestSettingUpTestValues, self).setUp()

    def test_creating_the_header(self):
        self.clean_and_init_tracker_file()
        setup_test_values()

        with open(self.csv_handler.tracker_file, "r") as f:
            header_actual = f.readline().strip()
            header_exspected = ",".join(self.csv_handler.column_names)

            self.assertEqual(header_exspected, header_actual)

    def test_number_of_created_items(self):
        pass


if __name__ == "__main__":
    unittest.main()
