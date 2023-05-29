def digits_squared(num):
    digits = str(num)
    sol = ""
    for digit in digits:
        sqr = int(digit) ** 2
        sol += str(sqr)
    return int(sol)


if __name__ == "__main__":
    print(digits_squared(9119))
