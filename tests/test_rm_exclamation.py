from src.rm_exclamation import remove_exclamation


def test_rm_exclamation():
    assert remove_exclamation("Hi!!!") == "Hi!!"
    assert remove_exclamation("!!Hi!!") == "!!Hi!"
    assert remove_exclamation("!H!i!") == "!H!i"
