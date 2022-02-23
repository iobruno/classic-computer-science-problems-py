import click
from csp.commands import csp

@click.group()
def cli():
    pass


cli.add_command(csp)

if __name__ == '__main__':
    cli()
