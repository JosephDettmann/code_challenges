from src.beast_feast import beast_feast


def test_best_feast():
    assert beast_feast("Tuna", "tapioca") == True
    assert beast_feast("Octopus", "olives") == True
    assert beast_feast("Muhammad ibn Musa al-Khwarizmi", "moderately difficult algebra")== False
