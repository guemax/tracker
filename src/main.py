import logging
import sys

import click

from .Tracker import Tracker

from src.commands.summary import summary
from src.commands.status import status
from src.commands.start import start
from src.commands.stop import stop
from src.commands.log import log


def enable_logging_in_console():    # pragma: no cover
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))


@click.group(help="A command-line tool to track your computer usage time.")
def cli():
    pass


def add_subcommands_to_cli():
    cli.add_command(summary.summary)
    cli.add_command(status.status)
    cli.add_command(start.start)
    cli.add_command(stop.stop)
    cli.add_command(log.log)


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

    add_subcommands_to_cli()

    # Start click
    cli()
