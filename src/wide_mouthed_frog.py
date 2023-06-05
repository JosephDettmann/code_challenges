def mouth_size(animal):
    if animal.casefold() == "alligator":
        return "small"
    return "wide"


if __name__ == "__main__":
    print(mouth_size("AlLiGaToR"))
