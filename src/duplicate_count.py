def duplicate_count(string):
    char_count = {
        char.lower()
        for char in string
        if string.lower().count(char.lower()) > 1 and char.isalnum()
    }
    return len(char_count)
