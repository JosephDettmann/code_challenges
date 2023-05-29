def remove_exclamation(s):
    if s.endswith("!"):
        return s[:-1]
    return s


if __name__ == "__main__":
    print(remove_exclamation("HI!"))
