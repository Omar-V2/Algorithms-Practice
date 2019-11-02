def two_sum_alt(nums, target):
    lookup = {}
    pairs = []
    for num in nums:
        if num in lookup:
            pairs.append([lookup[num], num])
        else:
            diff = target - num
            lookup[diff] = num
    print(lookup)
    return pairs

print(two_sum_alt([1, 2, 4, 7, 5, -10], -5))