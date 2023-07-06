from src.skills_master import count_skills


def test_count_skills():
    assert count_skills([0, 0, 0, 1, 3, 3, 2], {1, 2}) == 3
    assert count_skills([0, 0, 0, 1, 3, 3, 2], set()) == 0
    assert count_skills([0, 0, 0, 1, 3, 3, 2], {6}) == 3
