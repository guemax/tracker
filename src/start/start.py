import logging

import click

from ..csv_handler import TimerHandler
from ..exceptions.InvalidTimerModification import InvalidTimerModification


@click.command()
def start():
    """Start a new timer"""
    timer_handler = TimerHandler.TimerHandler()
    try:
        time = timer_handler.start_timer()
    except InvalidTimerModification:
        logging.info("Starting a new timer aborted due to an exisiting timer")
        print("A timer already exists which has not been stopped yet.\n"
              "Please stop it by typing 'tracker stop'.")
    else:
        logging.info(f"New timer started")
        print(f"New timer started at {time}\nOK")
