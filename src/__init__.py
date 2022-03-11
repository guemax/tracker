"""Set up logging and init the tracker file"""
from .Tracker import Tracker
from .setup_logging import setup_logging


setup_logging(debug=False)

tracker = Tracker()
tracker.init_tracker_file()
