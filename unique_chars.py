def unique_chars(s):
    checker = {}
    for i in s:
        if i in checker:
            return False
        else:
            checker[i] = 1
    return True

print(unique_chars("moOse"))
print(unique_chars("moose"))