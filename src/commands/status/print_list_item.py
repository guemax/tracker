from src.console_logger.console_logger import info


def print_list_item(message: str) -> None:
    style = " - "
    info(style + message)
