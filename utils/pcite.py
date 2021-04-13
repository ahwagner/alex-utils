import click
from datetime import date

@click.command()
@click.argument(
    'citations', type=click.INT
)
def cli(citations):
    """
    Print the projected number of citations by year-end given today's
    CITATIONS count.
    """
    delta = date.today() - date(year=date.today().year, month=1, day=1)
    c = int(round(citations / int(delta.days) * 365, 0))
    click.echo(f'{c} citations projected by end of year.')
