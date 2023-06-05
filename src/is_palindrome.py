def is_palindrome(s):
    return s.casefold() == s[::-1].casefold()


if __name__ == "__main__":
    print(is_palindrome("anna"))
