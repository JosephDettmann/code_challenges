from src.replace_letters import replace_letters


def test_replace_letters():
    assert replace_letters("hello") == "idoon"
    assert replace_letters("codewars") == "enedazuu"
