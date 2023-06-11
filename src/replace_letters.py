def replace_letters(word):
    word = word.casefold()
    dictionary = {
        "a": "z",
        "b": "e",
        "c": "e",
        "d": "e",
        "e": "d",
        "f": "i",
        "g": "i",
        "h": "i",
        "i": "h",
        "j": "o",
        "k": "o",
        "l": "o",
        "m": "o",
        "n": "o",
        "o": "n",
        "p": "u",
        "q": "u",
        "r": "u",
        "s": "u",
        "t": "u",
        "u": "t",
        "v": "a",
        "w": "a",
        "x": "a",
        "y": "a",
        "z": "a",
    }
    new_word = ""
    for char in word:
        new_word += dictionary.get(char)
    return new_word
