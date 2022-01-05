import logging

import click

from ..csv_handler import CSVHandler
from ..exceptions.InvalidTimerModification import InvalidTimerModification


@click.command()
@click.option("--message", "-m", default="", type=str)
def stop(message: str) -> None:
    """Stop an exisiting timer"""
    csv_handler = CSVHandler.CSVHandler()
    try:
        time = csv_handler.finish_created_entry(message)
    except InvalidTimerModification:
        logging.info("Stopping timer aborted due to a missing created timer")
        print("No timer exists yet.\n"
              "Please start one by typing 'tracker start'.")
    else:
        logging.info("Existing timer stopped")
        if message:
            print(f"Existing timer stopped at {time} with message\nOK")
        else:
            print(f"Existing timer stopped at {time}\nOK")
