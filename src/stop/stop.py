import logging

import click

from ..csv_handler import CSVHandler


@click.command()
def stop():
    """Stop an exisiting timer"""
    csv_handler = CSVHandler.CSVHandler()
    time = csv_handler.finish_created_entry()

    logging.info("Existing timer stopped")
    print(f"Existing timer stopped at {time}\nOK")
