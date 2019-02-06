def linear_search(a, target):
    for i, v in enumerate(a):
        if v == target:
            return True, v, i
    return False

a = [1, 5, 6, 9]
print(linear_search(a, 2))
        