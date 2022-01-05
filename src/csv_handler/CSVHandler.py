import csv
import datetime
import os

import logging


class CSVHandler:
    def __init__(self):
        self.tracker_folder = "src/files"
        self.tracker_file = "src/files/tracker.csv"
        self.fieldnames = ["start_time", "stop_time", "message"]

    def init_tracker_csv_file(self) -> None:
        logging.info("Initializing Tracker CSV file")
        if self.tracker_file_exists():
            return
        else:
            self.create_tracker_file()

    def create_tracker_file(self) -> None:
        logging.debug("Create tracker CSV file")

        self.create_files_folder_if_not_exists()
        with open(self.tracker_file, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=self.fieldnames)
            writer.writeheader()

    def create_files_folder_if_not_exists(self):
        if not os.path.isdir(self.tracker_folder):
            os.mkdir(self.tracker_folder)

    def tracker_file_exists(self) -> bool:
        return os.path.isfile(self.tracker_file)

    def create_new_entry(self) -> str:
        current_time = datetime.datetime.now()
        current_time = current_time.strftime("%b, %d %Y at %H:%M:%S")

        with open(self.tracker_file, "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=self.fieldnames)
            writer.writerow({"start_time": current_time, "stop_time": "", "message": ""})

        return current_time
