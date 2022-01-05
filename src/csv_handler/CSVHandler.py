from datetime import datetime
import os

import logging

import pandas


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

        file = pandas.DataFrame(columns=self.fieldnames)
        file.to_csv(self.tracker_file, index=False)

    def create_files_folder_if_not_exists(self):
        if not os.path.isdir(self.tracker_folder):
            os.mkdir(self.tracker_folder)

    def tracker_file_exists(self) -> bool:
        return os.path.isfile(self.tracker_file)

    def create_new_entry(self) -> str:
        current_time = datetime.now().strftime("%b, %d %Y at %H:%M:%S")

        with open(self.tracker_file, "a") as f:
            data = pandas.DataFrame({"start_time": current_time, "stop_time": None, "message": None}, index=[0])
            data.to_csv(f, header=False, index=False)

        return current_time

    def finish_created_entry(self, message: str) -> str:
        stop_time = datetime.now().strftime("%b, %d %Y at %H:%M:%S")

        data = pandas.read_csv(self.tracker_file, dtype=str)

        index = len(data) - 1
        data.at[index, "stop_time"] = stop_time
        data.at[index, "message"] = message

        data.to_csv(self.tracker_file, index=False)

        return stop_time
