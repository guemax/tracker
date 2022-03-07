import click

from .print_status_of_unfinished_entries import print_status_of_unfinished_entries
from .print_status_of_grouped_entries import print_status_of_grouped_entries
from .print_status_of_entries import print_status_of_entries

from src.console_logger.console_logger import info


@click.command()
def status():   # pragma: no cover
    """Provide information about the current tracking process"""
    info("Status information from Tracker:\n")

    print_status_of_unfinished_entries()
    print_status_of_entries()
    print_status_of_grouped_entries()

    info("\nOK")
