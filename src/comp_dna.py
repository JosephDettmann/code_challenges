def complementary_dna(dna):
    trans_map = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join([trans_map[x] for x in dna])


if __name__ == "__main__":
    print(complementary_dna("CGATCGATAGCTAGCTAGTCAGTC"))
    print(complementary_dna("CTGACTGACTGAAGTCAGTCAGTC"))
