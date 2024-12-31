import click

from app.csp.commands import csp
from app.genetic_algorithms.commands import ga


@click.group()
def cli():
    pass


cli.add_command(csp)
cli.add_command(ga)
