from src.digits_sqd import digits_squared


def test_digits_squared():
    assert digits_squared(9119) == 811181
    assert digits_squared(0000) == 0000
    assert digits_squared(7778) == 49494964
