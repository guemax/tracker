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

from .cli import cli

from .setup_cli import setup_cli
from .setup_logging import setup_logging
from .setup_tracker_files import setup_tracker_files

from .version import __version__


def start_tracker():
    program_name = "tracker"
    cli(prog_name=program_name)


def main():
    setup_tracker_files()   # Needs to be done first to ensure a 'files'-folder exists for the log file!
    setup_logging()

    logging.info("Initialising tracker")
    setup_cli(cli)

    logging.info(f"Starting tracker {__version__}")
    start_tracker()

    # TODO: Show exit information
    # logging.info(f"Closing tracker {__version__}")


if __name__ == "__main__":  # pragma: no cover
    main()
