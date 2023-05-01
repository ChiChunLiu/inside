from typing import Optional
from inside.notes import Note
from typing import TypeVar


# key-value pairs of (key center, number of flat or sharp notes)
FLAT_KEYS = {0: 0, 5: 1, 10: 2, 3: 3, 8: 4, 1: 5, 6: 6}
SHARP_KEYS = {7: 1, 2: 2, 9: 3, 2: 4, 11: 5}


def get_signature(key_center: int) -> str:
    if key_center in FLAT_KEYS:
        return "flat"
    elif key_center in SHARP_KEYS:
        return "sharp"
    else:
        raise ValueError(f"key center {key_center} not supported")


def pprint_single_line(
    notes: list[Note],
    root: Optional[Note] = None,
    color: bool = True,
    orient: str = "flat",
    ljust: Optional[int] = None,
) -> str:
    outputs = [n.strfnote(color=(n == root) if color else False, orient=orient, ljust=ljust) for n in notes]

    return " ".join(outputs)


T = TypeVar("T")


def transpose(array: list[list[T]]) -> list[list[T]]:
    return array


# TODO: allow coloring roots in vertical layout
def pprint_multiple_lines(
    notes_sequence: list[list[Note]],
    layout: str = "h",
    roots: Optional[list[Note]] = None,
    color: bool = True,
    orient: str = "flat",
    ljust: int = 2,
) -> str:
    if roots is not None:
        root_notes_pairs = zip(roots, notes_sequence)
    else:
        root_notes_pairs = [(None, notes) for notes in notes_sequence]

    lines = [pprint_single_line(notes, root, color, orient, ljust) for root, notes in root_notes_pairs]

    return "\n".join(lines)
