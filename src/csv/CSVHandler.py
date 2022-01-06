import logging
import os

import pandas

from .CSVAttributes import CSVAttributes


class CSVHandler(CSVAttributes):
    def __init__(self):
        super(CSVHandler, self).__init__()

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
