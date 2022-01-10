import logging

import click

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
        print("Warning: No timer exists yet.\n"
              "Please start one before stopping it by typing \"tracker start\".\n"
              "EXIT")
    else:
        logging.info("Existing timer stopped")
        if message:
            print(f"Existing timer stopped at {time[0]} at {time[1]} (running {time[2]}).\n"
                  f"Adding message \"{message}\" to Tracker file.\n"
                  f"OK")
        else:
            print(f"Existing timer stopped at {time[0]} at {time[1]} (running {time[2]})\n"
                  f"OK")
