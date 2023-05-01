from enum import IntEnum
from typing import Optional
from .settings import Color

FLAT_TO_SHARP = {"Db": "C#", "Eb": "D#", "Gb": "F#", "Ab": "G#", "Bb": "A#"}


class Note(IntEnum):
    C = 0
    Db = 1
    D = 2
    Eb = 3
    E = 4
    F = 5
    Gb = 6
    G = 7
    Ab = 8
    A = 9
    Bb = 10
    B = 11

    def __str__(self):
        return self.name

    def strfnote(
        self,
        color: bool = True,
        orient: str = "flat",
        ljust: Optional[int] = None,
    ) -> str:
        if orient == "sharp" and self.name in FLAT_TO_SHARP:
            s = FLAT_TO_SHARP[self.name]
        else:
            s = self.name

        if ljust is not None:
            assert ljust >= 2
            s = s.ljust(ljust)
        if color:
            s = f"{Color.RED}{s}{Color.DEFAULT}"

        return s
