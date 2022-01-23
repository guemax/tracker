import click


@click.command()
@click.option("-d/-w", "--day/--week", help="Summary of days or weeks", default=True)
def summary(day: bool) -> None:
    """Show the summary of work hours of days or weeks"""
    click.echo(day)
