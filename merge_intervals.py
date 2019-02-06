def merge_intervals(intervals):
    stack = []
    intervals.sort(key=lambda x: x[0])
    for i in intervals:
        if not stack:
            stack.append(i)
        else:
            if stack[-1][1] >= i[0]:
                second = max(stack[-1][1], i[1])
                merged = (stack[-1][0], second)
                stack.pop()
                stack.append(merged)
            else:
                stack.append(i)
    return stack


def merge_intervals2(intervals):
    current = 0
    after = 1
    ans = []
    intervals.sort(key=lambda x: x[0]) # sort intervals by first index
    while after < len(intervals):
        c = intervals[current]
        a = intervals[after]
        if c[1] >= a[0]: # merge is possible
            second = max(c[1], a[1])
            merged = (c[0], second)
            ans.append(merged)
            intervals[current] = merged
            after += 1
        else:
            if intervals[current] not in ans:
                ans.append(intervals[current])
            current = after
            after += 1
    return ans




i = [(0,1), (3, 5), (4, 8), (10, 12), (9, 10)]
print(merge_intervals(i))
print(merge_intervals2(i))
