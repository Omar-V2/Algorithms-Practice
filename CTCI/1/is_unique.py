def is_unique(s):
    seen = {}
    for char in s:
        if char in seen:
            return False
        else:
            seen[char] = 1
    return True

def is_unique_set(s):
    return len(set(s)) == len(s)


print(is_unique("ssa"))
print(is_unique_set("ssa"))