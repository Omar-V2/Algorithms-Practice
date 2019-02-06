def stringCompression(s):
    streak = 1
    compressed = []
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            streak += 1
        else:
            compressed.append(s[i] + str(streak))
            streak = 1
    compressed.append(s[-1] + str(streak))
    if len(s) < len(''.join(compressed)):
        return s
    return ''.join(compressed)
            


print(stringCompression("aabccccaaaz"))