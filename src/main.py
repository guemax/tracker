import logging
import sys

from Tracker import Tracker


def enable_logging_in_console():
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))


if __name__ == "__main__":
    # Set up logging
    logging.basicConfig(
        level=logging.INFO,
        filename="files/tracker.log",
        filemode="w",
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%d-%b-%y %H:%M:%S'
    )
    debug = True
    if debug:
        enable_logging_in_console()

    # Set up tracker
    tracker = Tracker()
    tracker.init()
