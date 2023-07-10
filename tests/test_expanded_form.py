from src.expanded_form import expanded_form


def test_expanded_form():
    assert expanded_form(70304) == "70000 + 300 + 4"
    assert expanded_form(12) == "10 + 2"
    assert expanded_form(42) == "40 + 2"
