import csv
import datetime
import os

import logging


class CSVHandler:
    def __init__(self):
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
        with open(self.tracker_file, "w") as f:
            writer = csv.DictWriter(f, fieldnames=self.fieldnames)
            writer.writeheader()

    def tracker_file_exists(self) -> bool:
        return os.path.isfile(self.tracker_file)

    def create_new_entry(self) -> str:
        current_time = datetime.datetime.now()
        current_time = current_time.strftime("%b, %d %Y at %H:%M:%S")

        with open(self.tracker_file, "a") as f:
            writer = csv.DictWriter(f, fieldnames=self.fieldnames)
            writer.writerow({"start_time": current_time, "stop_time": "", "message": ""})

        return current_time
