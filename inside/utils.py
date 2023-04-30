from inside.settings import Color
from typing import Optional
from inside.notes import Note


def pprint_notes(notes: list[Note], root: Optional[Note] = None, color: bool = True):
    if color:
        notes = [f"{Color.RED}{n}{Color.DEFAULT}" if n == root else f"{n}" for n in notes]
    else:
        notes = [f"{n}" for n in notes]
    notes = " ".join(notes)
    print(notes)
