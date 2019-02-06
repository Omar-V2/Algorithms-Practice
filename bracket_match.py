def bracket_match(s):
    c = 0
    unmatched = 0
    for b in s:
        if b == "(":
            c += 1
        else:
            c -= 1
            if c < 0:
                unmatched += 1
                c += 1
    return unmatched + c

print(bracket_match("))(("))