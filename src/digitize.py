def digitize(n):
    string = str(n)
    lst = []
    for char in string:
        lst.append(int(char))
    lst.reverse()
    return lst


if __name__ == "__main__":
    print(digitize(54545))
