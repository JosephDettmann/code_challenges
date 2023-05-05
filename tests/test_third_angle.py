from src.third_angle import third_angle


def test_third_angle():
    assert third_angle(30, 30) == 120
    assert third_angle(50, 50) == 80
    assert third_angle(12, 12) == 156
    assert third_angle(70, 70) == 40
    assert third_angle(32, 32) == 116
