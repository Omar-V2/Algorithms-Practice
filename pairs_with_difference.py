
# [[1, 0], [0, -1], [-1, -2], [2, 1]]

def pairs_with_difference(arr, k):
    pairs = {}
    ans = []
    for n in arr:
        pairs[n+k] = n
    for n in arr:
        key = n + k
        if key in arr:
            ans.append([pairs[key], key])
    return ans


arr = [0, -1, -2, 2, 1]