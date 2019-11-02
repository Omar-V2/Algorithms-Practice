def binary_search(items, target):
    start = 0
    end = len(items) - 1
    while start <= end:
        mid = int((start + end) / 2)
        if items[mid] == target:
            return mid
        if target > items[mid]:
            start = mid + 1
        elif target < items[mid]:
            end = mid - 1
    return -1

def binary_search_recursive(items, target, start, end):
    if start <= end:
        mid = int((start + end) / 2)
        if target == items[mid]:
            return mid
        if target < items[mid]:
            return binary_search_recursive(items, target, start, mid-1)
        elif target > items[mid]:
            return binary_search_recursive(items, target, mid+1, end)
    return -1


items = [2, 6, 13, 21, 36, 47, 63, 81, 97]

print(binary_search(items, 97))
print(binary_search_recursive(items, 97, 0, len(items)-1))
