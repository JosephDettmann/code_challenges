from src.multiply import multiply


def test_multiply():
    assert multiply(5, 10) == 50
    assert multiply(2, 17) == 34
    assert multiply(3, 17) == 51
    assert multiply(4, 35) == 140
    assert multiply(40, 15) == 600
    assert multiply(2394872, 1) != -3284239
    assert multiply(1, 2) != 1
    assert multiply(28, 5) == 140
