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
        print("No timer exists yet.\n"
              "Please start one by typing 'tracker start'.")
    else:
        logging.info("Existing timer stopped")
        if message:
            print(f"Existing timer stopped at {time[0]} at {time[1]} (running {time[2]}) with message\nOK")
        else:
            print(f"Existing timer stopped at {time[0]} at {time[1]} (running {time[2]})\nOK")
