def count_sheep(sheep):
    x = 0
    for i in range(len(sheep)):
        if sheep[i] == True:
            x = x + 1
    return x


if __name__ == "__main__":
    print(count_sheep([True, False, True, True, True]))
