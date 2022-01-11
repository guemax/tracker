import logging

import click

from src.console_logger.console_logger import info, warn
from src.handler.timer_handler import TimerHandler
from src.exceptions.InvalidTimerModification import InvalidTimerModification


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
             "Please start one before stopping it by typing \"tracker start\".\n"
             "EXIT")
    else:
        logging.info("Existing timer stopped")
        if message:
            info(f"Existing timer stopped at {time[0]} at {time[1]}. (running {time[2]})\n"
                 f"Added message \"{message}\" to Tracker file.\n"
                 f"OK")
        else:
            info(f"Existing timer stopped at {time[0]} at {time[1]}. (running {time[2]})\n"
                 f"OK")
