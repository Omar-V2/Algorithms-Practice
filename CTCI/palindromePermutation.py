def palindromePermutation(s):
    count = {}
    num_odd = 0
    for char in s:
        if char in count:
            count[char] += 1
        elif char != " ": # ignore whitespaces
            count[char] = 1
    for k in count:
        if count[k] % 2 != 0:
            num_odd += 1
    if num_odd > 1:
        return False
    return True

print(palindromePermutation("tact coa"))