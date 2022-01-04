import logging
import sys

import click

from .Tracker import Tracker
from .status import status


def enable_logging_in_console():
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))


@click.group(help="A command-line tool to track your computer usage time.")
def cli():
    pass


if __name__ == "__main__":
    # Set up logging
    logging.basicConfig(
        level=logging.INFO,
        filename="src/files/tracker.log",
        filemode="w",
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%d-%b-%y %H:%M:%S'
    )
    debug = False
    if debug:
        enable_logging_in_console()

    # Set up tracker
    tracker = Tracker()
    tracker.init()

    # Add subcommands
    cli.add_command(status.status)

    # Start click
    cli()
