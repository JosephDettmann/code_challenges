from src.even_odd import even_odd


def test_even_odd():
    assert even_odd(1) == False
    assert even_odd(2) == True
    assert even_odd(3) == False
    assert even_odd(4) == True
    assert even_odd(7) == False
    assert even_odd(13) == False
    assert even_odd(25) == False
    assert even_odd(34) == True
    assert even_odd(8) == True
