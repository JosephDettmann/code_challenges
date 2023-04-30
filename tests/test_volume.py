from src.volume import volume


def test_volume():
    assert(volume(4, 2, 3) == 24)
    assert(volume(5, 5, 3) == 75)
    assert(volume(5, 3, 4) == 60)
    assert(volume(4, 3, 4) == 48)
    assert(volume(1, 3, 17) == 51)
