def dna_to_rna(dna):
    return dna.replace("T", "U")


if __name__ == "__main__":
    print(dna_to_rna("TTTT"))
