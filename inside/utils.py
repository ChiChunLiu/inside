from inside.settings import Color
from typing import Optional
from inside.notes import Note

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


def pprint_notes(
    notes: list[Note], root: Optional[Note] = None, color: bool = True, orient: str = "flat"
) -> None:
    if color:
        outputs = [
            f"{Color.RED}{n.strfnote(orient)}{Color.DEFAULT}" if n == root else n.strfnote(orient)
            for n in notes
        ]
    else:
        outputs = [n.strfnote(orient) for n in notes]
    print(" ".join(outputs))
