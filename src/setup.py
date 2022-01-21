import click
import num2words

from src.console_logger.console_logger import info, warn
from src.setup_test_values.setup_test_values import SetupTestValues


class SetupTestValuesForConsole:
    def __init__(self):
        self.set_upper = SetupTestValues()

        self.number_of_entries = 0
        self.number_of_entries_as_word = ""

    def setup(self, number_of_entries: int):
        self.number_of_entries = number_of_entries
        self.try_to_set_new_number_of_entries()

        self.set_upper.setup()

        self.convert_number_of_entries_into_word()
        self.print_success_message()

    def try_to_set_new_number_of_entries(self) -> None:
        try:
            self.set_upper.set_number_of_entries(self.number_of_entries)
        except ValueError:
            self.handle_invalid_number_of_entries()

    def handle_invalid_number_of_entries(self) -> None:
        warn(f"The number of entries cannot be negative (was {self.number_of_entries}). "
             f"Please specify a value greater than or equal zero.\n"
             "EXIT")
        exit(-1)

    def convert_number_of_entries_into_word(self):
        self.number_of_entries_as_word = num2words.num2words(self.number_of_entries)

    def print_success_message(self) -> None:
        if self.number_of_entries == 1:
            message_of_created_entries = "one entry"
        else:
            message_of_created_entries = f"{self.number_of_entries_as_word} entries"

        info(f"\nSuccesfully setup {message_of_created_entries}.\n"
             f"OK")


@click.command()
@click.option("-e", "--entries", "number_of_entries", help="Number of entries to create", type=int, default=4)
def main(number_of_entries: int) -> None:
    console_set_upper = SetupTestValuesForConsole()
    console_set_upper.setup(number_of_entries)


if __name__ == "__main__":  # pragma: no cover
    main()
