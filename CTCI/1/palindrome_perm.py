def palindrome_perm(s):
    counts = {}
    num_odd = 0
    for char in s:
        char = char.lower()
        if char in counts:
            counts[char] += 1
        else:
            if char != " ":
                counts[char] = 1
    print(counts)
    for count in counts.values():
        if count % 2 != 0:
            num_odd += 1
            if num_odd > 1:
                return False
    return True

print(palindrome_perm("Taco CaT"))