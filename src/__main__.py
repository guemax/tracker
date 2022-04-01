"""This file is part of Tracker.
Tracker is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
Tracker is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with Tracker. If not, see <http://www.gnu.org/licenses/>.
"""

import logging
import os.path
import sys

import click

from .Tracker import Tracker

from src.commands.summary import summary
from src.commands.status import status
from src.commands.start import start
from src.commands.stop import stop
from src.commands.log import log

from .version import __version__


def enable_logging_in_console():    # pragma: no cover
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))


@click.group(help="A command-line tool to track your computer usage time.")
@click.version_option(__version__, prog_name="Tracker")
def cli():
    pass


def add_subcommands_to_cli():
    cli.add_command(summary.summary)
    cli.add_command(status.status)
    cli.add_command(start.start)
    cli.add_command(stop.stop)
    cli.add_command(log.log)


def main():
    # Create files folder if it does not exist
    if not os.path.isdir("files"):
        os.mkdir("files")

    # Set up logging
    logging.basicConfig(
        level=logging.INFO,
        filename="files/tracker.log",
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
    cli(prog_name="tracker")


if __name__ == "__main__":  # pragma: no cover
    main()
