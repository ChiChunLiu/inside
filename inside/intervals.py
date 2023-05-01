MAJOR_SCALE_INTERVALS = (2, 2, 1, 2, 2, 2, 1)
TRIAD_INTERVALS = {
    "maj": (4, 3),
    "min": (3, 4),
    "dim": (3, 3),
    "aug": (4, 4),
}
SEVENTH_INTERVLAS = {
    "maj": (4, 3, 4),
    "min": (3, 4, 3),
    "dim": (3, 3, 3),
    "minmaj": (3, 4, 4),
    "min7b5": (3, 3, 4),
    "dom": (4, 3, 3),
    "maj7#5": (4, 4, 3),
}

SCALE_OFFSETS = {
    "major": 0,
    "minor": 5,
    "ionian": 0,
    "dorian": 1,
    "phrygian": 2,
    "lydian": 3,
    "mixolydian": 4,
    "aeolian": 5,
    "locrian": 6,
}


SCALE_OFFSETS_HALF_STEP = {
    "major": 0,
    "minor": 9,
    "ionian": 0,
    "dorian": 2,
    "phrygian": 4,
    "lydian": 5,
    "mixolydian": 7,
    "aeolian": 9,
    "locrian": 11,
}

SEVENTH_PROGRESSIONS = {
    "major": ("maj", "min", "min", "maj", "dom", "min7b5", "min"),
    "natural_minor": ("min", "min7b5", "maj", "min", "min", "major", "dom"),
    "harmonic_minor": ("minmaj", "min7b5", "maj7#5", "min", "dom", "maj", "dim"),
    "melodic_minor": ("minmaj", "min", "maj7#5", "dom", "dom", "min75b", "min7b5"),
}
