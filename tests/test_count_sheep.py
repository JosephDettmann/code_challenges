from src.count_sheep import count_sheep


def test_count_sheep():
    assert count_sheep([True, False, True, False, True, True, False, True]) == 5
    assert count_sheep(True, True, True, False, False, True, True, True, True) == 7
    assert count_sheep(True, True, True, False) == 3
    assert (
        count_sheep(
            True,
            False,
            False,
            False,
            True,
            False,
            True,
            False,
            True,
            True,
            False,
            False,
            True,
            True,
            False,
            False,
            False,
            True,
        )
        == 8
    )
    assert count_sheep(False, False, False, False, False) == 0
