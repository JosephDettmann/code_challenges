from src.comp_dna import complementary_dna


def test_complementary_dna():
    assert complementary_dna("AAAA") == "TTTT"
    assert complementary_dna("TTTT") == "AAAA"
    assert complementary_dna("CCCC") == "GGGG"
    assert complementary_dna("GGGG") == "CCCC"
