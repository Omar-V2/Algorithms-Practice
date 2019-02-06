from collections import Counter


def sort_chars_freq(string):
    ans = ""
    count = Counter(string)
    pairs = []
    for key in count:
        pairs.append((key, count[key]))
    pairs.sort(key=lambda x: x[1], reverse=True)
    print(pairs)
    for pair in pairs:
        ans += pair[0]*pair[1]
    print(ans)
    

print(sort_chars_freq('tree'))