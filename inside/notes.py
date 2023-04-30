from enum import IntEnum


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

    def strfnote(self, orient="flat"):
        if orient == "sharp" and self.name in FLAT_TO_SHARP:
            return FLAT_TO_SHARP[self.name]
        else:
            return self.name
