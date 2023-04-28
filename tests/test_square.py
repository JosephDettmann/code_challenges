from src.square import square


def test_square():
    assert(square(8) == 64)
    assert(square(9) == 81)
    assert(square(10) == 100)
    assert(square(11) == 121)
    assert(square(12) == 144)