from src.real_love import real_love


def test_real_love():
    assert real_love(3, 22) == True
    assert real_love(13, 2542) == True
    assert real_love(1, 23) == False
    assert real_love(6, 11) == True
    assert real_love(17, 88) == True
