import click
from csp.commands import csp
from genetic_algorithms.commands import ga


@click.group()
def cli():
    pass

cli.add_command(csp)
cli.add_command(ga)

if __name__ == '__main__':
    cli()
