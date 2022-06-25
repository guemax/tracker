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
import colorama

from colorama import Fore, Back


def debug_deprecated(message: str) -> None:
    colored_message = Fore.LIGHTBLUE_EX + message
    click.echo(colored_message)


def info_deprecated(message: str) -> None:
    colored_message = Fore.WHITE + message
    click.echo(colored_message)


def warn_deprecated(message: str) -> None:
    colored_message = Fore.YELLOW + message
    click.echo(colored_message, err=True)


def error_deprecated(message: str) -> None:
    colored_message = Fore.RED + message
    click.echo(colored_message, err=True)


def fatal_deprecated(message: str) -> None:
    colored_message = Fore.BLACK + Back.RED + message
    click.echo(colored_message, err=True)


# This part will be run when this file has been loaded
colorama.init(autoreset=True)

