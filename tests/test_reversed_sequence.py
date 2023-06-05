from src.reversed_sequence import reverse_sequence

from src.reversed_sequence import reverse_sequence


def test_reversed_sequence():
    assert reverse_sequence(3) == [3, 2, 1]
    assert reverse_sequence(6) == [6, 5, 4, 3, 2, 1]
    assert reverse_sequence(9) == [9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert reverse_sequence(12) == [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
