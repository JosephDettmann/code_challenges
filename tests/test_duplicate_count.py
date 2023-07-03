from src.duplicate_count import duplicate_count


def test_duplicate_count():
    assert duplicate_count("") == 0
    assert duplicate_count("abcde") == 0
    assert duplicate_count("abcdeaB") == 2
    assert duplicate_count("Indivisibilities") == 2
    assert duplicate_count("aazzbbyyccxx") == 6
