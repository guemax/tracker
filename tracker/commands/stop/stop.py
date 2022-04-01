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
@click.option("--message", "-m", default="", type=str)
def stop(message: str) -> None:
    """Stop an exisiting timer"""
    timer_handler = TimerHandler.TimerHandler()
    try:
        time = timer_handler.stop_timer(message)
    except InvalidTimerModification:
        logging.info("Stopping timer aborted due to a missing created timer")
        warn("Warning: No timer exists yet.\n"
             "  (use \"tracker start\" to create one)\n"
             "\nEXIT")
    else:
        logging.info("Existing timer stopped")
        if message:
            info(f"Existing timer stopped at {time[0]} at {time[1]}. (running {time[2]})\n"
                 f"Added message \"{message}\" to Tracker file.\n"
                 f"\nOK")
        else:
            info(f"Existing timer stopped at {time[0]} at {time[1]}. (running {time[2]})\n"
                 f"\nOK")
