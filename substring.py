s = "abcd"
for start in range(len(s)):
    for finish in range(start, len(s)):
        print(s[start:finish+1])