def is_pangram(string):
    string = string.casefold()
    if (
        string.count("a") >= 1
        and string.count("b") >= 1
        and string.count("c") >= 1
        and string.count("d") >= 1
        and string.count("e") >= 1
        and string.count("f") >= 1
        and string.count("g") >= 1
        and string.count("h") >= 1
        and string.count("i") >= 1
        and string.count("j") >= 1
        and string.count("k") >= 1
        and string.count("l") >= 1
        and string.count("m") >= 1
        and string.count("n") >= 1
        and string.count("o") >= 1
        and string.count("p") >= 1
        and string.count("q") >= 1
        and string.count("r") >= 1
        and string.count("s") >= 1
        and string.count("t") >= 1
        and string.count("u") >= 1
        and string.count("v") >= 1
        and string.count("w") >= 1
        and string.count("x") >= 1
        and string.count("y") >= 1
        and string.count("z") >= 1
    ):
        return True
    return False


print(is_pangram("The quick brown fox jumps over the lazy dog"))
