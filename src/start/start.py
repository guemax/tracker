import click

from ..csv_handler import CSVHandler


@click.command()
def start():
    """Start a new timer"""
    csv_handler = CSVHandler.CSVHandler()
    csv_handler.create_new_entry()
