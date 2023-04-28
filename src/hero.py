def hero(bullets, dragons):
    if dragons * 2 <= bullets:
        return True
    else:
        return False


if __name__ == "__main__":
    print(hero(8, 4))
