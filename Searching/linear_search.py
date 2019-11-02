def linear_search(array, target):
    for index, value in enumerate(array):
        if value == target:
            return index
    return False


print(linear_search([3, 4, 12, 23, 46], target=46))