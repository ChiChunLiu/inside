from .notes import Note
from .intervals import MAJOR_SCALE_INTERVALS, TRIAD_INTERVALS, SEVENTH_INTERVLAS, SCALE_OFFSETS
import itertools


class SequenceGenerator:
    num_notes_scale = 7
    num_notes_triad = 3
    num_notes_seventh = 4

    @staticmethod
    def _intervals_to_notes(start: Note, intervals: list[int]) -> list[Note]:
        accumulated_intervals = itertools.accumulate(intervals)
        return [Note((start + a) % 12) for a in accumulated_intervals]

    @classmethod
    def generate_scale(cls, root: Note, name: str) -> list[Note]:
        intervals = itertools.cycle(MAJOR_SCALE_INTERVALS)
        for _ in range(SCALE_OFFSETS[name]):
            next(intervals)
        intervals = [0] + [next(intervals) for _ in range(cls.num_notes_scale - 1)]
        return SequenceGenerator._intervals_to_notes(start=root, intervals=intervals)

    @classmethod
    def generate_triad(cls, root: Note, name: str, inversion: int = 0) -> list[Note]:
        intervals = [0] + list(TRIAD_INTERVALS[name])
        notes = itertools.cycle(SequenceGenerator._intervals_to_notes(start=root, intervals=intervals))
        for _ in range(inversion):
            next(notes)
        return [next(notes) for _ in range(cls.num_notes_triad)]

    @classmethod
    def generate_seventh(cls, root: Note, name: str, inversion: int = 0) -> list[Note]:
        intervals = [0] + list(SEVENTH_INTERVLAS[name])
        notes = itertools.cycle(SequenceGenerator._intervals_to_notes(start=root, intervals=intervals))
        for _ in range(inversion):
            next(notes)
        return [next(notes) for _ in range(cls.num_notes_seventh)]
