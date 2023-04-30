import click
from inside.sequence_generator import SequenceGenerator
from inside.utils import pprint_notes, get_signature
from inside.notes import Note
from inside.intervals import SCALE_OFFSETS_HALF_STEP


@click.group()
def cli():
    pass


@click.command()
@click.option("--root", required=True, help="root note with alteration in flat. e.g. Db")
@click.option("--name", required=True, help="scale name")
@click.option("--descend", is_flag=True, help="descending ordered")
def scale(root, name, descend):
    notes = SequenceGenerator.generate_scale(Note[root], name)
    if descend:
        notes.reverse()
    key_center = (Note[root] - SCALE_OFFSETS_HALF_STEP[name] + 12) % 12
    sig = get_signature(key_center)
    pprint_notes(notes, root=Note[root], color=True, orient=sig)


@click.command()
@click.option("--root", required=True, help="root note with alteration in flat. e.g. Db")
@click.option("--name", required=True, help="triad name. e.g aug")
@click.option("--inversion", default=0, help="degree of inversion", type=click.IntRange(0, 2))
@click.option("--descend", is_flag=True, help="descending ordered")
def triad(root, name, inversion, descend):
    notes = SequenceGenerator.generate_triad(Note[root], name, inversion)
    if descend:
        notes.reverse()
    pprint_notes(notes, root=Note[root], color=True, orient="flat")


@click.command()
@click.option("--root", required=True, help="root note with alteration in flat. e.g. Db")
@click.option("--name", required=True, help="seventh name. e.g. min7b5")
@click.option("--inversion", default=0, help="degree of inversion", type=click.IntRange(0, 3))
@click.option("--descend", is_flag=True, help="descending ordered")
def seventh(root, name, inversion, descend):
    notes = SequenceGenerator.generate_seventh(Note[root], name, inversion)
    if descend:
        notes.reverse()
    pprint_notes(notes, root=Note[root], color=True, orient="flat")


cli.add_command(scale)
cli.add_command(triad)
cli.add_command(seventh)
