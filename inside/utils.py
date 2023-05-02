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


def stringify_notes(
    notes: list[Note],
    root: Optional[Note] = None,
    color: bool = True,
    orient: str = "flat",
    ljust: Optional[int] = None,
) -> list[str]:
    outputs = [n.strfnote(color=(n == root) if color else False, orient=orient, ljust=ljust) for n in notes]

    return outputs


def stringify_notes_singleline(
    notes: list[Note],
    root: Optional[Note] = None,
    color: bool = True,
    orient: str = "flat",
    ljust: Optional[int] = None,
) -> str:
    output = stringify_notes(notes, root, color, orient, ljust)

    return " ".join(output)


T = TypeVar("T")


def transpose(mat: list[list[T]]) -> list[list[T]]:
    m = len(mat)
    n = len(mat[0])

    transposed = [[mat[0][0] for _ in range(m)] for _ in range(n)]
    for i in range(m):
        for j in range(n):
            transposed[j][i] = mat[i][j]

    return transposed


# TODO: refactor to avoid splitting
def stringify_notes_multiline(
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

    lines = [stringify_notes(notes, root, color, orient, ljust) for root, notes in root_notes_pairs]

    if layout == "v":
        lines = transpose(lines)
    lines = [" ".join(line) for line in lines]

    return "\n".join(lines)
