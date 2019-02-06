def isPermutation(s1, s2):
    if len(s1) != len(s2):
        return False
    count = {}
    for char in s1:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    for char in s2:
        if char in count:
            count[char] -= 1
        else:
            return False
    if sum(count.values()) == 0:
        return True
    else:
        return False

print(isPermutation('dcw4f', 'dcw5f'))