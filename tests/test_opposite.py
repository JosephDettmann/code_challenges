from src.opposite import opposite


def test_opposite():
    assert opposite(123456) == -123456
    assert opposite(1) != -3
    assert opposite(-557) == 557
    assert opposite(-4637.56) == 4637.56
    assert opposite(-46.32) != 2343247852369
