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

import os
import shutil
import logging
import unittest
import webbrowser

import click
import coverage as coverage_lib

from tracker.csv.CSVHandler import CSVHandler
from tracker.setup_test_values.setup_test_values import SetupTestValues


@click.command()
def clean() -> None:
    """Remove the files folder and all its content"""
    print("Cleaning tracker folder ... ", end="")
    try:
        csv_handler = CSVHandler()
        shutil.rmtree(csv_handler.tracker_folder)
    except FileNotFoundError:
        # File has already been deleted. Nothing to do for us now.
        pass

    print("done")


@click.command()
def log() -> None:
    """Print the content of the log file"""
    print("Printing content of log file ... ")

    try:
        with open("files/tracker.log") as f:
            content = f.readlines()
    except FileNotFoundError:
        print("Error: log file has been deleted. Regenerate it by running tracker.")
    else:
        print()
        for line in content:
            print(line, end="")
        print("\n... done")


@click.command()
@click.option("-e", "--entries", help="Number of entries to setup", type=int, default=4)
def setup(entries: int) -> None:
    """Set up the given number of test entries"""
    print(f"Setting up {entries} test entries ... ", end="")
    set_upper = SetupTestValues()
    set_upper.set_number_of_entries(entries)

    set_upper.setup()

    print("done")


@click.command()
def test() -> None:
    """Run the tracker test suite"""
    # Clean the tracker files before testing
    csv_handler = CSVHandler()
    shutil.rmtree(csv_handler.tracker_folder, ignore_errors=True)

    # Removes annoying log messages when running the tests
    logging.disable(logging.CRITICAL)

    loader = unittest.TestLoader()
    start_directory = "./tests"
    suite = loader.discover(start_directory)

    runner = unittest.TextTestRunner()
    runner.run(suite)


@click.command()
@click.option("-b", "--badge", help="Generate the coverage badge for the README",
              is_flag=True, default=False, type=bool)
@click.option("-w", "--webbrowser", "open_in_browser", help="Open html report in default webbrowser",
              is_flag=True, default=False, type=bool)
@click.pass_context
def coverage(ctx: click.Context, badge: bool, open_in_browser: bool) -> None:
    """Calculate the coverage (and generate the coverage badge if reuested)"""
    print("Calculating coverage ...\n")

    cov = coverage_lib.Coverage(omit=["/usr/*", "*__init__.py"])
    cov.start()

    ctx.invoke(test)

    cov.stop()
    cov.save()
    cov.html_report()

    if open_in_browser:
        path = "file://" + os.path.realpath(os.getcwd() + "/htmlcov/index.html")
        webbrowser.open(path, new=2)

    if badge:
        print("")
        os.system("coverage-badge -o ./docs/coverage-badge/coverage.svg -f")

    print("\n... done")


@click.command()
def count() -> None:
    """Count number of code and comment lines of this project"""
    os.system("pygount --format=summary --suffix=\"py\" --folders-to-skip=\"venv,htmlcov,build,dist\"")


@click.group(help="A python script running useful commands for developing")
def cli() -> None:
    pass


def main() -> None:
    cli.add_command(log)
    cli.add_command(test)
    cli.add_command(clean)
    cli.add_command(count)
    cli.add_command(setup)
    cli.add_command(coverage)

    cli(prog_name="make")


if __name__ == "__main__":
    main()
