import click


class ConsoleLogger:
    def __init__(self, level: str):
        self.levels = {"DEBUG": "white", "INFO": "white", "WARNING": "yellow", "ERROR": "red", "FATAL": "red"}
        self.level_color = self.levels[level]

    def print(self, message: str, error: bool = False):
        if error:
            click.echo(click.style(message, fg=self.level_color), err=True)
        else:
            click.echo(click.style(message, fg=self.level_color))
