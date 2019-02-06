def checkPermutation(s1, s2):
    if len(s1) != len(s2):
        return False
    lookup = {}
    for char in s1:
        if char in lookup:
            lookup[char] += 1
        else:
            lookup[char] = 1
    for char in s2:
        if char in lookup:
            lookup[char] -= 1
        else:
            return False
    if sum(lookup.values()) == 0:
        return True 
    else:
        return False


def checkPermutation2(s1, s2):
    if len(s1) != len(s2):
        return False
    lookup = {}
    for char in s1:
        if char in lookup:
            lookup[char] += 1
        else:
            lookup[char] = 1
    for char in s2:
        if char in lookup:
            lookup[char] -= 1
            if lookup[char] < 0:
                return False
        else:
            return False
    return True

print(checkPermutation("moose", "esoom"))
print(checkPermutation2("moose", "esoom"))