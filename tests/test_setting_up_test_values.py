import unittest

from src.setup_test_values.setup_test_values import SetupTestValues

from tests.test_csv.CSVBaseTestingClass import CSVBaseTestingClass


class TestSettingUpTestValues(CSVBaseTestingClass):
    def setUp(self) -> None:
        super(TestSettingUpTestValues, self).setUp()
        self.set_upper = SetupTestValues()

    def test_creating_the_header(self):
        self.clean_and_init_tracker_file()
        self.set_upper.setup()

        with open(self.csv_handler.tracker_file, "r") as f:
            header_actual = f.readline().strip()
            header_exspected = ",".join(self.csv_handler.column_names)

            self.assertEqual(header_exspected, header_actual)

    def test_number_of_entries_to_create(self):
        self.clean_and_init_tracker_file()
        self.set_upper.setup()

        self.check_if_number_of_entries_have_been_created()

    def check_if_number_of_entries_have_been_created(self):
        with open(self.csv_handler.tracker_file, "r") as f:
            content = f.read().strip()
            number_of_lines = len(content.split("\n"))

            # Remove the line for the header
            number_of_entries = number_of_lines - 1
            self.assertEqual(self.set_upper._number_of_entries, number_of_entries)

    def test_creating_no_entries(self):
        self.clean_and_init_tracker_file()

        self.check_for_changed_number_of_entries(0)

    def test_changing_the_number_of_entries_to_create(self):
        self.clean_and_init_tracker_file()

        for i in range(1, 21):
            self.check_for_changed_number_of_entries(i)

    def check_for_changed_number_of_entries(self, number_of_entries: int):
        self.set_upper.set_number_of_entries(number_of_entries)
        self.set_upper.setup()

        self.check_if_number_of_entries_have_been_created()

        # Reset the values for the set upper
        self.set_upper.__init__()

    def test_invalid_number_of_entries_to_create(self):
        self.clean_and_init_tracker_file()

        self.assertRaises(ValueError, self.set_upper.set_number_of_entries, -1)


if __name__ == "__main__":
    unittest.main()
