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
import num2words

from tracker.console_logger.console_logger import info, warn
from tracker.setup_test_values.setup_test_values import SetupTestValues


class SetupTestValuesForConsole:
    def __init__(self):
        self.__set_upper = SetupTestValues()

        self.__number_of_entries = 0
        self.__number_of_entries_as_word = ""

    def setup(self, number_of_entries: int):
        self.__number_of_entries = number_of_entries
        self.__try_to_set_new_number_of_entries()

        self.__set_upper.setup()

        self.__convert_number_of_entries_into_word()
        self.__print_success_message()

    def __try_to_set_new_number_of_entries(self) -> None:
        try:
            self.__set_upper.set_number_of_entries(self.__number_of_entries)
        except ValueError:
            self.__handle_invalid_number_of_entries()

    def __handle_invalid_number_of_entries(self) -> None:
        warn(f"The number of entries cannot be negative (was {self.__number_of_entries}). "
             f"Please specify a value greater than or equal zero.\n"
             "EXIT")
        exit(-1)

    def __convert_number_of_entries_into_word(self):
        self.__number_of_entries_as_word = num2words.num2words(self.__number_of_entries)

    def __print_success_message(self) -> None:
        if self.__number_of_entries == 1:
            message_of_created_entries = "one entry"
        else:
            message_of_created_entries = f"{self.__number_of_entries_as_word} entries"

        info(f"\nSuccesfully setup {message_of_created_entries}.\n"
             f"OK")


@click.command()
@click.option("-e", "--entries", "number_of_entries", help="Number of entries to create", type=int, default=4)
def main(number_of_entries: int) -> None:
    """This script sets up test values. It fills the Tracker file with the given number of entries."""
    console_set_upper = SetupTestValuesForConsole()
    console_set_upper.setup(number_of_entries)


if __name__ == "__main__":  # pragma: no cover
    main()
