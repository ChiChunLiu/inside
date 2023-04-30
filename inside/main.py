import click
from inside.sequence_generator import SequenceGenerator
from inside.utils import pprint_notes
from inside.notes import Note


@click.group()
def cli():
    pass


@click.command()
@click.option("--root", required=True, help="root note with alteratino in flat. e.g. Db")
@click.option("--name", required=True, help="scale name")
def scale(root, name):
    notes = SequenceGenerator.generate_scale(Note[root], name)
    pprint_notes(notes, color=True)


@click.command()
@click.option("--root", required=True, help="root note with alteratino in flat. e.g. Db")
@click.option("--name", required=True, help="triad name")
@click.option("--inversion", default=0, help="degree of inversion")
def triad(root, name, inversion):
    notes = SequenceGenerator.generate_triad(Note[root], name, inversion)
    pprint_notes(notes, color=True)


cli.add_command(scale)
cli.add_command(triad)
