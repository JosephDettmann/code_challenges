def beast_feast(beast, dish):
    return (
        beast[0].casefold() == dish[0].casefold()
        and dish[-1].casefold() == beast[-1].casefold()
    )


if __name__ == "__main__":
    print(beast_feast("Black Bear", "baklava"))
