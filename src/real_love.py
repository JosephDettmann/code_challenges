def real_love(flwr1, flwr2):
    if flwr1 % 2 == 0 and flwr2 % 2 == 1:
        return True
    elif flwr1 % 2 == 1 and flwr2 % 2 == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    print(real_love(5, 7))
