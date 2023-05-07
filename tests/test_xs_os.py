from src.xs_os import xs_os


def test_xs_os():
    assert xs_os("myxomas") == True
    assert xs_os("exonym") == True
    assert xs_os("xylophone") == False
    assert xs_os("pharynx") == False
    assert xs_os("buxomer") == True
    assert xs_os("exogamy") == True
