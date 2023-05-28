from src.parsed_age import parsed_age


def test_parsed_age():
    assert parsed_age("8 years old") == 8
    assert parsed_age("2 years old") == 2
    assert parsed_age("9 years old") == 9
