import click
from datetime import date, timedelta

date_parse_strings = [
    '%Y-%m-%d',
    '%Y-%m',
    '%Y'
]


@click.command()
@click.argument(
    'start', type=click.DateTime(date_parse_strings), default=str(date.today())
)
@click.argument(
    'end', type=click.DateTime(date_parse_strings), default=str(date.today())
)
@click.option('-d', '--delta', type=click.INT)
def cli(start, end, delta):
    """
    Print the number of days from START date to END date. If DELTA is provided,
    print computed START date plus DELTA days (and ignore END date).
    """
    if delta is not None:
        end = start + timedelta(days=delta)
        click.echo(
            f'{delta} days from {start.date()}: {end.date()}.'
        )
    elif start == end and end.date() == date.today():
        click.echo(
            f'Today is {date.today()}.'
        )
    else:
        delta = end - start
        click.echo(
            f'Difference from {start.date()} to {end.date()}: {delta.days} days.'
        )
