def check_perm(s1, s2):
    if len(s1) != len(s2):
        return False
    counts = {}
    for char in s1:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    for char in s2:
        if char in counts:
            counts[char] -= 1
            if counts[char] < 0:
                return False
        else:
            return False
    return sum(counts.values()) == 0

print(check_perm("math", "hmats"))