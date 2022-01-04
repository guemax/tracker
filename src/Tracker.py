import logging
import csv
import os


class Tracker:
    def __init__(self):
        self.tracker_file = "src/files/tracker.csv"
        self.fieldnames = ["id", "start_time", "stop_time", "message"]

    def init(self):
        logging.info("Initializing Tracker")
        if self.tracker_file_exists():
            return
        else:
            self.create_tracker_file()

    def create_tracker_file(self) -> None:
        logging.debug("Create tracker file")
        with open(self.tracker_file, "w") as f:
            writer = csv.DictWriter(f, fieldnames=self.fieldnames)
            writer.writeheader()

    def tracker_file_exists(self) -> bool:
        return os.path.isfile(self.tracker_file)
