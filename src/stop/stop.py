import logging

import click

from ..csv_handler import CSVHandler


@click.command()
@click.option("--message", "-m", default="", type=str)
def stop(message: str) -> None:
    """Stop an exisiting timer"""
    csv_handler = CSVHandler.CSVHandler()
    time = csv_handler.finish_created_entry(message)

    logging.info("Existing timer stopped")
    if message:
        print(f"Existing timer stopped at {time} with message\nOK")
    else:
        print(f"Existing timer stopped at {time}\nOK")
