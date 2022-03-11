"""This file is part of Tracker.

Tracker is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Tracker is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Tracker. If not, see <http://www.gnu.org/licenses/>.
"""

import click

from .print_status_of_unfinished_entries import print_status_of_unfinished_entries
from .print_status_of_grouped_entries import print_status_of_grouped_entries
from .print_status_of_entries import print_status_of_entries

from tracker.console_logger.console_logger import info


@click.command()
def status():   # pragma: no cover
    """Provide information about the current tracking process"""
    info("Status information from Tracker:\n")

    print_status_of_unfinished_entries()
    print_status_of_entries()
    print_status_of_grouped_entries()

    info("\nOK")
