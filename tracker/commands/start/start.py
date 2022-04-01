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

import click

from tracker.console_logger.console_logger import info, warn
from tracker.handler.timer_handler import TimerHandler
from tracker.exceptions.InvalidTimerModification import InvalidTimerModification


@click.command()
def start():
    """Start a new timer"""
    timer_handler = TimerHandler.TimerHandler()
    try:
        time = timer_handler.start_timer()
        time = " at ".join(time)
    except InvalidTimerModification:
        logging.info("Starting a new timer aborted due to an exisiting timer")
        warn("Warning: A timer already exists which has not been stopped yet.\n"
             "Please stop it first by typing \"tracker stop\".\n"
             "EXIT")
    else:
        logging.info(f"New timer started")
        info(f"New timer started at {time}\n"
             f"OK")
