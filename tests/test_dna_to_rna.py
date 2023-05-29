from src.dna_to_rna import dna_to_rna


def test_dna_to_rna():
    assert dna_to_rna("ATAT") == "AUAU"
    assert dna_to_rna("GCACGT") == "GCACGU"
