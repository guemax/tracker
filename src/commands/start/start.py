import logging

import click

from src.handler.timer_handler import TimerHandler
from src.exceptions.InvalidTimerModification import InvalidTimerModification


@click.command()
def start():
    """Start a new timer"""
    timer_handler = TimerHandler.TimerHandler()
    try:
        time = timer_handler.start_timer()
        time = " at ".join(time)
    except InvalidTimerModification:
        logging.info("Starting a new timer aborted due to an exisiting timer")
        print("Warning: A timer already exists which has not been stopped yet.\n"
              "Please stop it first by typing \"tracker stop\".\n"
              "EXIT")
    else:
        logging.info(f"New timer started")
        print(f"New timer started at {time}\n"
              f"OK")
