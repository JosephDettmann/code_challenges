from src.plural import plural


def test_plural():
    assert plural(5) == True
    assert plural(1) == False
    assert plural(7) == True
    assert plural(26) == True
