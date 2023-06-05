from src.digitize import digitize


def test_digitize():
    assert digitize(5678) == [8, 7, 6, 5]
    assert digitize(321) == [1, 2, 3]
    assert digitize(12345) == [5, 4, 3, 2, 1]
