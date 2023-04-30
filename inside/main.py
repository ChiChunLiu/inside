import click
from inside.sequence_generator import SequenceGenerator
from inside.utils import pprint_notes
from inside.notes import Note


@click.group()
def cli():
    pass


@click.command()
@click.option("--root", required=True, help="root note with alteration in flat. e.g. Db")
@click.option("--name", required=True, help="scale name")
def scale(root, name):
    notes = SequenceGenerator.generate_scale(Note[root], name)
    pprint_notes(notes, color=True)


@click.command()
@click.option("--root", required=True, help="root note with alteration in flat. e.g. Db")
@click.option("--name", required=True, help="triad name. e.g aug")
@click.option("--inversion", default=0, help="degree of inversion", type=click.IntRange(0, 2))
def triad(root, name, inversion):
    notes = SequenceGenerator.generate_triad(Note[root], name, inversion)
    pprint_notes(notes, color=True)


@click.command()
@click.option("--root", required=True, help="root note with alteration in flat. e.g. Db")
@click.option("--name", required=True, help="seventh name. e.g. min7b5")
@click.option("--inversion", default=0, help="degree of inversion", type=click.IntRange(0, 3))
def seventh(root, name, inversion):
    notes = SequenceGenerator.generate_seventh(Note[root], name, inversion)
    pprint_notes(notes, color=True)


cli.add_command(scale)
cli.add_command(triad)
cli.add_command(seventh)
