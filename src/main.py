import logging
import sys

from .Tracker import Tracker
from .cli import cli


def enable_logging_in_console():    # pragma: no cover
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))


if __name__ == "__main__":  # pragma: no cover
    # Set up logging
    logging.basicConfig(
        level=logging.INFO,
        filename="src/files/tracker.log",
        filemode="w",
        format='%(asctime)s.%(msecs)03d - %(levelname)s - %(message)s',
        datefmt='%d-%b-%y %H:%M:%S'
    )
    debug = False
    if debug:
        enable_logging_in_console()

    # Set up tracker
    tracker = Tracker()
    tracker.init()

    # Start click
    cli()
