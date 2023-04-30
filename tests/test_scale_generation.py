from inside.sequence_generator import SequenceGenerator
from inside.notes import Note
import pytest


@pytest.mark.parametrize(
    "root,name,expected",
    [
        ("C", "major", ["C", "D", "E", "F", "G", "A", "B"]),
        ("A", "aeolian", ["A", "B", "C", "D", "E", "F", "G"]),
        ("F", "mixolydian", ["F", "G", "A", "Bb", "C", "D", "Eb"]),
    ],
)
def test_scale_generation(root, name, expected):
    scale_generated = SequenceGenerator.generate_scale(Note[root], name)
    scale_expected = [Note[n] for n in expected]

    assert all([e0 == e1 for e0, e1 in zip(scale_generated, scale_expected)])


@pytest.mark.parametrize(
    "root,name,inversion,expected",
    [
        ("C", "maj", 0, ["C", "E", "G"]),
        ("A", "min", 0, ["A", "C", "E"]),
        ("Bb", "aug", 0, ["Bb", "D", "Gb"]),
        ("C", "maj", 1, ["E", "G", "C"]),
        ("C", "maj", 2, ["G", "C", "E"]),
    ],
)
def test_triad_generation(root, name, inversion, expected):
    scale_generated = SequenceGenerator.generate_triad(Note[root], name, inversion)
    scale_expected = [Note[n] for n in expected]
    assert all([e0 == e1 for e0, e1 in zip(scale_generated, scale_expected)])


@pytest.mark.parametrize(
    "root,name,inversion,expected",
    [
        ("C", "maj", 0, ["C", "E", "G", "B"]),
        ("A", "min", 0, ["A", "C", "E", "G"]),
        ("Bb", "minmaj", 0, ["Bb", "Db", "F", "A"]),
        ("C", "maj", 1, ["E", "G", "B", "C"]),
        ("C", "maj", 3, ["B", "C", "E", "G"]),
    ],
)
def test_seventh_generation(root, name, inversion, expected):
    scale_generated = SequenceGenerator.generate_seventh(Note[root], name, inversion)
    scale_expected = [Note[n] for n in expected]
    assert all([e0 == e1 for e0, e1 in zip(scale_generated, scale_expected)])
