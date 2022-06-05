"""This file is part of tracker.
Tracker is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
Tracker is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with tracker. If not, see <http://www.gnu.org/licenses/>.
"""
import click


def debug(message: str) -> None:
    colored_message = click.style(message, fg="white")
    click.echo(colored_message)


def info(message: str) -> None:
    colored_message = click.style(message, fg="white")
    click.echo(colored_message)


def warn(message: str) -> None:
    colored_message = click.style(message, fg="yellow")
    click.echo(colored_message, err=True)


def error(message: str) -> None:
    colored_message = click.style(message, fg="red")
    click.echo(colored_message, err=True)


def fatal(message: str) -> None:
    colored_message = click.style(message, fg="red")
    click.echo(colored_message, err=True)

