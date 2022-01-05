import logging

import click

from ..csv_handler import CSVHandler
from ..exceptions.InvalidTimerModification import InvalidTimerModification


@click.command()
def start():
    """Start a new timer"""
    csv_handler = CSVHandler.CSVHandler()
    try:
        time = csv_handler.create_new_entry()
    except InvalidTimerModification:
        logging.info("Starting a new timer aborted due to an exisiting timer")
        print("A timer already exists which has not been stopped yet.\n"
              "Please stop it by typing 'tracker stop'.")
    else:
        logging.info(f"New timer started")
        print(f"New timer started at {time}\nOK")
