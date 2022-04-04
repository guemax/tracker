"""This file is part of tracker.

Tracker is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Tracker is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with tracker. If not, see <http://www.gnu.org/licenses/>.
"""

import logging
import os

import pandas

from .CSVAttributes import CSVAttributes


class CSVHandler(CSVAttributes):
    def __init__(self):
        super(CSVHandler, self).__init__()

    def init_tracker_csv_file(self) -> None:
        if self.tracker_file_exists():
            return
        else:
            logging.info("Initializing tracker CSV file")
            self.create_tracker_file()

    def create_tracker_file(self) -> None:
        logging.debug("Create tracker CSV file")

        self.create_files_folder_if_not_exists()

        file = pandas.DataFrame(columns=self.column_names)
        file.to_csv(self.tracker_file, index=False)

    def create_files_folder_if_not_exists(self):
        if not os.path.isdir(self.tracker_folder):
            os.mkdir(self.tracker_folder)

    def tracker_file_exists(self) -> bool:
        return os.path.isfile(self.tracker_file)

    def get_column_names(self) -> list:
        return self.column_names
