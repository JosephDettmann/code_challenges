def DNAtoRNA(dna):
    return dna.replace("T", "U")


if __name__ == "__main__":
    print(DNAtoRNA("TTTT"))
