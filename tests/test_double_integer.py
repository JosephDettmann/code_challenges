from src.double_integer import double_integer


def test_double_integer():
    assert(double_integer(5) == 10)
    assert(double_integer(3) == 6)
    assert(double_integer(7) == 14)