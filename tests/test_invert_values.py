from src.invert_values import invert_values


def test_invert_values():
    assert invert_values([1, -3, 5, -7, 9]) == [-1, 3, -5, 7, -9]
    assert invert_values([-2, -4, 6, 8, -10, -12]) == [2, 4, -6, -8, 10, 12]
    assert invert_values([1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]) == [
        -1,
        -2,
        -3,
        -5,
        -7,
        -11,
        -13,
        -17,
        -19,
        -23,
        -29,
        -31,
        -37,
    ]
    assert invert_values([5, 4, 3, 2, 1]) == [-5, -4, -3, -2, -1]
    assert invert_values([-16, 8, -4, 2, -1]) == [16, -8, 4, -2, 1]
