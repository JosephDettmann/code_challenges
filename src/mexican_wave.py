def wave(string):
    string = string.casefold()
    result = []
    for i, char in enumerate(string):
        if char == " ":
            continue
        start = string[:i]
        middle = char.upper()
        end = string[i + 1 :]
        result.append(start + middle + end)
    return result


if __name__ == "__main__":
    print(wave("hello"))
