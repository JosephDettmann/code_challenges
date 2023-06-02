from src.final_grade import final_grade


def test_final_grade():
    assert final_grade(74, 19) == 100
    assert final_grade(93, 0) == 100
    assert final_grade(77, 7) == 90
    assert final_grade(60, 3) == 75
