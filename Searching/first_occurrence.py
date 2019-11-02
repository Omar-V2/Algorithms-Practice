def first_occurrence(items, target):
    start = 0
    end = len(items) - 1
    while start <= end:
        mid = int((start + end) / 2)
        if mid == 0 and items[mid] == target:
            return mid
        if items[mid] == target and items[mid-1] != target:
            return mid
        if target < items[mid]:
            end = mid - 1
        elif target > items[mid]:
            start = mid + 1
        elif items[mid-1] == target:
            end = mid - 1
    return -1

def last_occurrence(items, target):
    start = 0
    end = len(items) - 1
    while start <= end:
        mid = int((start + end) / 2)
        if mid == len(items) - 1 and items[mid] == target:
            return mid
        if target == items[mid] and items[mid+1] != target:
            return mid
        if target > items[mid]:
            start = mid + 1
        if target < items[mid]:
            end = mid - 1
        if items[mid+1] == target:
            start = mid + 1

def first_occurrence_better(items, target):
    start = 0
    end = len(items) - 1
    result = -1
    while start <= end:
        mid = int((start + end) / 2)
        if target == items[mid]:
            result = mid
            end = mid - 1
        elif target < items[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return result

def last_occurrence_better(items, target):
    start = 0
    end = len(items) - 1
    result = -1
    while start <= end:
        mid = int((start + end) / 2)
        if target == items[mid]:
            result = mid
            start = mid + 1
        elif target > items[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return result

def count_occurrences(items, target):
    return (last_occurrence_better(items, target) - first_occurrence_better(items, target)) + 1

items = [2, 4, 10, 10, 10, 18, 20]
# items = [10, 10, 10, 10, 10, 18, 20]
# items = [2, 4, 5, 6, 7, 8, 10]
# print(first_occurrence(items, 10))
# print(last_occurrence(items, 10))
print(first_occurrence_better(items, 10))
print(last_occurrence_better(items, 10))
print(count_occurrences(items, 10))