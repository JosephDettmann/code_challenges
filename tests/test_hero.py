from src.hero import hero


def test_hero():
    assert hero(100, 50)
    assert hero(10, 5)
    assert hero(18, 9)
   