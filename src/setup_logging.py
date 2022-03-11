import logging
import sys


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        filename="src/files/tracker.log",
        filemode="w",
        format='%(asctime)s.%(msecs)03d - %(levelname)s - %(message)s',
        datefmt='%d-%b-%y %H:%M:%S'
    )


def set_debug(debug: bool = False):
    if debug:
        enable_logging_in_console()


def enable_logging_in_console():    # pragma: no cover
    logger = logging.getLogger()
    stream_handler = logging.StreamHandler(sys.stdout)

    logger.addHandler(stream_handler)
