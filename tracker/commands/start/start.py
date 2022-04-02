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

import sys
import logging

import click

from tracker.handler.timer_handler import TimerHandler
from tracker.console_logger.console_logger import info, warn
from tracker.exceptions.InvalidTimerModification import InvalidTimerModification


@click.command()
def start():
    """Start a new timer"""
    timer_handler = TimerHandler.TimerHandler()
    try:
        datetime = timer_handler.start_timer()
        date = datetime[0]
        time = datetime[1]
    except InvalidTimerModification:
        logging.warning(
            "InvalidTimerModification: A timer already exists which must be stopped before starting another one."
        )
        warn("Warning: A timer already exists which has not been stopped yet.\n"
             "  (use \"tracker stop\" to stop it first)\n"
             "\nEXIT")
        sys.exit(-1)

    logging.info(f"New timer successfully started at {date} at {time}.")
    info(f"New timer started at {date} at {time}\n"
         f"\nOK")
