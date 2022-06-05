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
along with tracker. If not, see <http://www.gnu.org/licenses/>.
"""

import logging
import sys

import click

from tracker.commands.console_logger import info, warn
from tracker.handler.timer_handler import TimerHandler
from tracker.exceptions.InvalidTimerModification import InvalidTimerModification


@click.command()
@click.option("--message", "-m", default="", type=str)
def stop(message: str) -> None:
    """Stop an exisiting timer"""
    timer_handler = TimerHandler.TimerHandler()
    message = message.strip()
    try:
        datetime = timer_handler.stop_timer(message)
        date = datetime[0]
        time = datetime[1]
        work_hours = datetime[2]
    except InvalidTimerModification:
        logging.warning("InvalidTimerModification: No timer exists yet which could be stopped.")
        warn("Warning: No timer exists yet.\n"
             "  (use \"tracker start\" to create one)\n"
             "\nEXIT")
        sys.exit(-1)

    logging.info(f"Existing timer successfully stopped at {date} at {time} (running {work_hours})")
    info(f"Existing timer stopped at {date} at {time}. (running {work_hours})")
    if message:
        logging.info(f"Added message \"{message}\" to tracker file.")
        info(f"Added message \"{message}\" to tracker file.")
    info("\nOK")
