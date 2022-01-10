# import logging
import click

from src.console_logger.console_logger import info


@click.command()
def status():   # pragma: no cover
    """Provide information about the current tracking process"""
    # TODO: Add real information
    info("Status information")
