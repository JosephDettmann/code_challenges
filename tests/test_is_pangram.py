from src.is_pangram import is_pangram


def test_is_pangram():
    assert is_pangram("The quick brown fox jumps over the lazy dog") == True
