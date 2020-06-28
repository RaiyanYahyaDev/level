"""
The root of the command hierarchy.
"""
import click
from level import create, add, state, up, send, log


@click.group()
@click.version_option()
def cli() -> None:
    """
    A new take on code management.
    """


cli.add_command(create.create)
cli.add_command(add.add)
cli.add_command(state.state)
cli.add_command(up.up)
cli.add_command(send.send)
cli.add_command(log.log)
