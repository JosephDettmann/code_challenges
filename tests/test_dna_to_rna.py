from src.dna_to_rna import DNAtoRNA


def test_dna_to_rna():
    assert DNAtoRNA("ATAT") == "AUAU"
    assert DNAtoRNA("GCACGT") == "GCACGU"
