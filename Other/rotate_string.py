def rotate_string(s1, s2):
    first = s2[0]
    n = s1.index(first)
    shifted = shift(s1, n)
    return shifted == s2

def shift(s, n):
    return s[n:] + s[:n]


s1 = "abcde"
s2 = "cdeab"

print(rotate_string(s1, s2))