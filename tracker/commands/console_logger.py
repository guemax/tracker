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
import sys

import click
import colorama

from colorama import Fore, Back


def debug(message: str, print_status: bool = False) -> None:
    if print_status:
        message += "\n\nOK"

    colored_message = Fore.LIGHTBLUE_EX + message
    click.echo(colored_message)


def info(message: str, print_status: bool = True, exit_tracker: bool = False) -> None:
    if print_status:
        message += "\n\nOK"

    colored_message = Fore.WHITE + message
    click.echo(colored_message)

    if exit_tracker:
        sys.exit(0)


def warn(message: str, print_status: bool = False, exit_tracker: bool = False) -> None:
    if print_status:
        message += "\n\nEXIT"

    colored_message = Fore.YELLOW + message
    click.echo(colored_message, err=True)

    if exit_tracker:
        sys.exit(-1)


def error(message: str, print_status: bool = False, exit_tracker: bool = False) -> None:
    if print_status:
        message += "\n\nEXIT"

    colored_message = Fore.RED + message
    click.echo(colored_message, err=True)

    if exit_tracker:
        sys.exit(-1)


def fatal(message: str, print_status: bool = False, exit_tracker: bool = False) -> None:
    if print_status:
        message += "\n\nEXIT"

    colored_message = Fore.BLACK + Back.RED + message
    click.echo(colored_message, err=True)

    if exit_tracker:
        sys.exit(-1)


# This part will be run when this file has been loaded
colorama.init(autoreset=True)

