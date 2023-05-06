from src.bool_to_str import bool_to_str


def test_bool_to_str():
    assert bool_to_str(True) == "True"
    assert bool_to_str(False) == "False"
