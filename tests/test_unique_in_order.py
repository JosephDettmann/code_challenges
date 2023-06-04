from src.unique_in_order import unique_in_order

def test_unique_sequence():
    assert unique_in_order("AAAABBBCCDAABBB") == []
    assert unique_in_order([]) == []
    assert unique_in_order(()) == []
