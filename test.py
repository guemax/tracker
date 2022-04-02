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
import shutil
import unittest

from tracker.csv.CSVHandler import CSVHandler

# Clean the tracker files before testing
csv_handler = CSVHandler()
shutil.rmtree(csv_handler.tracker_folder)

# Removes annoying log messages when running the tests
logging.disable(logging.CRITICAL)

loader = unittest.TestLoader()
start_directory = "./tests"
suite = loader.discover(start_directory)

runner = unittest.TextTestRunner()
runner.run(suite)
