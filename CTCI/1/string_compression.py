from collections import Counter

def string_compression(s):
    current_count = 1
    result = ""
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            current_count += 1
        else:
            result += s[i] + str(current_count)
            current_count = 1
    result += s[-1] + str(current_count)
    if len(result) < len(s):
        return result
    return s


print(string_compression("aabbcccccaab"))
print(string_compression("abbb"))
print(string_compression("aabbb"))
