def three_sum(a, t):
    a.sort()
    for num in a:
        target = t - num
        i = 0
        j = len(a) - 1
        while i <= j:
            if a[i] + a[j] == target:
                return num, a[i], a[j]
            elif a[i] + a[j] > target:
                j -= 1
            elif a[i] + a[j] < target:
                i += 1
    return False


print(three_sum([2,3,4], 10))
