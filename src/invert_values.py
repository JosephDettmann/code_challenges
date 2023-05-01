def invert_values(lst):
    return [-x for x in lst]

if __name__ == "__main__":
    print(invert_values([1, -2, 3, -4, 5]))