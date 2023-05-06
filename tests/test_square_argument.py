from src.square_argument import square_argument


def test_square_argument():
    assert square_argument(7) == 49
    assert square_argument(6) == 36
    assert square_argument(5) == 25
    assert square_argument(4) == 16
    assert square_argument(3) == 9
    assert square_argument(2) == 4