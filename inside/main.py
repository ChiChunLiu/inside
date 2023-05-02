import click
from inside.sequence_generator import SequenceGenerator
from inside.utils import get_signature, stringify_notes_singleline, stringify_notes_multiline
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
    s = stringify_notes_singleline(notes, root=Note[root], color=True, orient=sig)
    print(s)


@click.command()
@click.option("--root", required=True, help="root note with alteration in flat. e.g. Db")
@click.option("--name", required=True, help="triad name. e.g aug")
@click.option("--inversion", default=0, help="degree of inversion", type=click.IntRange(0, 2))
@click.option("--descend", is_flag=True, help="descending ordered")
def triad(root, name, inversion, descend):
    notes = SequenceGenerator.generate_triad(Note[root], name, inversion)
    if descend:
        notes.reverse()
    s = stringify_notes_singleline(notes, root=Note[root], color=True, orient="flat")
    print(s)


@click.command()
@click.option("--root", required=True, help="root note with alteration in flat. e.g. Db")
@click.option("--name", required=True, help="seventh name. e.g. min7b5")
@click.option("--inversion", default=0, help="degree of inversion", type=click.IntRange(0, 3))
@click.option("--descend", is_flag=True, help="descending ordered")
def seventh(root, name, inversion, descend):
    notes = SequenceGenerator.generate_seventh(Note[root], name, inversion)
    if descend:
        notes.reverse()
    s = stringify_notes_singleline(notes, root=Note[root], color=True, orient="flat")
    print(s)


@click.command()
@click.option("--key", required=True, help="key center with alteration in flat. e.g. Db")
@click.option("--mode", required=True, help="major/natural_minor/melodic_minor/harmonic_minor")
@click.option("--progression", required=True, help="name of progression. e.g. diatonic or ii-v-i")
@click.option("--inversion", default=0, help="degree of inversion", type=click.IntRange(0, 3))
@click.option("--layout", default="h", help="(h)orizontal or (v)ertical")
def progression(key, mode, progression, inversion, layout):
    _progression = SequenceGenerator.generate_seventh_progression(
        key_center=Note[key], mode=mode, progression_name=progression, inversion=inversion
    )
    roots = SequenceGenerator.generate_scale(root=Note[key], name=mode)
    s = stringify_notes_multiline(
        _progression, layout=layout, roots=roots, color=True, orient="flat", ljust=2
    )
    print(s)


cli.add_command(scale)
cli.add_command(triad)
cli.add_command(seventh)
cli.add_command(progression)
