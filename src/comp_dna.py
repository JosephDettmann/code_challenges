def complementary_dna(dna):
    comp_dna = ""
    for char in dna:
        if char == "C":
            comp_dna = comp_dna + "G"
        elif char == "T":
            comp_dna = comp_dna + "A"
        elif char == "G":
            comp_dna = comp_dna + "C"
        elif char == "A":
            comp_dna = comp_dna + "T"
    return comp_dna


if __name__ == "__main__":
    print(complementary_dna("CGATCGATAGCTAGCTAGTCAGTC"))
    print(complementary_dna("CTGACTGACTGAAGTCAGTCAGTC"))
