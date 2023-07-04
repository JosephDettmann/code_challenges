def is_pangram(string):
    string = string.casefold()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if string.count(char) < 1:
            return False
    return True


print(is_pangram("The quick brown fox jumps over the lazy dog"))
