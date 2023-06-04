def unique_in_order(sequence):
    i = 0
    cur_char = ""
    result = []
    for char in sequence():
        if i == 0 or char != cur_char:
            result.append(char)
            cur_char == char
        else:
            continue
        i+=1



if __name__ == "__main__":
    print(unique_in_order("AABBAACCAADD"))