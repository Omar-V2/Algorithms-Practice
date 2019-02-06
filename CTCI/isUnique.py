def isUnique(s):
    lookup = {}
    for char in s:
        if char in lookup:
            return False
        else:
            lookup[char] = 1
    return True

print(isUnique("helo"))