import random

from src.csv import CSVHandler
from .entry import Entry


class SetupTestValues:
    def __init__(self) -> None:
        self.csv_handler = CSVHandler.CSVHandler()
        self.csv_handler.create_files_folder_if_not_exists()

        self.number_of_entries = 4

        self.messages = [
            "", "Working on Tracker", "Developing new features",
            "Fixing bugs", "Adding tests", "Refactoring"
        ]

        self.entry = Entry()

    def set_number_of_entries(self, new_number: int):
        if new_number < 0:
            raise ValueError("The number of entries to create cannot be negative.")

        self.number_of_entries = new_number

    def setup(self) -> None:
        with open(self.csv_handler.tracker_file, "w") as f:
            f.write(self.header())
            f.write(self.entries())

    def header(self) -> str:
        return ",".join(self.csv_handler.column_names) + "\n"

    def entries(self) -> str:
        entries = ""

        for i in range(1, self.number_of_entries + 1):
            entries += self.build_entry(i)

        return entries

    def build_entry(self, number: int) -> str:
        message = random.choice(self.messages)
        return self.entry.build(message, number)
