def only_digits(query):
    try:
        int(query)
    except ValueError:
        return False
    return True, int(query)


print(only_digits("12a3"))