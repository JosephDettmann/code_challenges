def xs_os(s):
    s = s.lower()
    return s.count("x") == s.count("o")


if __name__ == "__main__":
    print(xs_os("hell"))
