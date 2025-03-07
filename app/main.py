from typer import Typer

from app.csp.commands import csp
from app.genetic_algorithms.commands import ga

cli = Typer(no_args_is_help=True)
cli.add_typer(csp)
cli.add_typer(ga)
