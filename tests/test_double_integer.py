from src.double_integer import double_integer


def test_double_integer():
    assert(double_integer(3) == 6)
    assert(double_integer(6) == 12)
    assert(double_integer(9) == 18)
    assert(double_integer(12) == 24)
    assert(double_integer(16) == 32)
