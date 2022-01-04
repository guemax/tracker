import logging

import click

from ..csv_handler import CSVHandler


@click.command()
def start():
    """Start a new timer"""
    csv_handler = CSVHandler.CSVHandler()
    time = csv_handler.create_new_entry()

    logging.info(f"New timer started")
    print(f"New timer started at {time}\nOK")
