import logging
import os


class Tracker:
    def __init__(self):
        self.tracker_file = "files/tracker.csv"

    def init(self):
        logging.info("Initializing Tracker")
        if self.tracker_file_exists():
            return
        else:
            self.create_tracker_file()

    def create_tracker_file(self) -> None:
        logging.debug("Create tracker file")
        with open(self.tracker_file, "w") as f:
            pass

    def tracker_file_exists(self) -> bool:
        return os.path.isfile(self.tracker_file)
