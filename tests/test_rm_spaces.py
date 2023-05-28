from src.rm_spaces import rm_spaces


def test_rm_spaces():
    assert rm_spaces("What's up?") == "What'sup?"
    assert rm_spaces("Hey man.") == "Heyman."
    assert rm_spaces("You good?") == "Yougood?"
    assert rm_spaces("What are you doing?") == "Whatareyoudoing?"
