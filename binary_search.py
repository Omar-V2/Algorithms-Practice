def binary_search_iterative(a, target):
    size = len(a)
    start = 0
    end = size - 1
    while start <= end:
        mid = (start + end) // 2
        if target == a[mid]:
            return "{} exists at index {}".format(target, mid)
        elif target < a[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return False


def binary_search_recursive(a, target, start, end):
    mid = (start + end) // 2
    if start > end:
        return False
    if target == a[mid]:
        return "{} exists at index {}".format(target, mid)
    elif target < a[mid]:
        return binary_search_recursive(a, target, start, mid-1)
    else:
        return binary_search_recursive(a, target, mid+1, end)

def first_occurence(a, target):
    start = 0 
    end = len(a) - 1
    while start <= end:
        mid = (start + end) // 2
        if a[mid] > target:
            end = mid - 1
        elif a[mid] < target:
            start = mid + 1
        elif a[mid] == target and (mid == 0 or a[mid-1] < target):
            return mid
        else:
            end = mid - 1
    return False

def last_occurrence(a, target):
    start = 0
    end = size = len(a) - 1
    while start <= end:
        mid = (start + end) // 2
        if a[mid] < target:
            start = mid + 1
        elif a[mid] > target: # could actually combine this line 
            end = mid - 1
        elif a[mid] == target and (mid == size or a[mid+1] > target):
            return mid
        else:               # and this line into a single else statement, but this is more readable
            start = mid + 1
    return False

def count_occurrences(a, target):
    first_index = first_occurence(a, target)
    last_index = last_occurrence(a, target)
    if first_index and last_index:
        return (last_index - first_index) + 1
    return False

def num_rotations(a): # need to finish this function
    start = 0
    end = size = len(a) - 1
    mid = (start + end) // 2
    while start <= end:
        nxt = (mid + 1) % size
        prev = (mid - 1) % size
        if a[start] <= a[end]:
            return mid

def index_equals_value(a):
    start = 0
    end = len(a) - 1
    while start <= end:
        mid = (start + end) // 2
        if a[mid] == mid:
            return mid
        elif a[mid] > mid:
            end = mid - 1
        else:
            start = mid + 1
    return False

def search_sorted_rotated(a, target):
    start = 0
    end = len(a) - 1
    while start <= end:
        mid = (start + end) // 2
        if a[mid] == target:
            return mid
        elif a[mid] >= a[start]:
            if target < a[mid] and target >= a[start]:
                end = mid - 1
            else:
                start = mid + 1
        elif a[mid] <= a[end]:
            if target > a[mid] and target <= a[end]:
                start = mid + 1 
            else:
                start = mid - 1




a = [5, 6, 7, 10, 19, 24]
b = [0, 1, 1, 1, 2, 2, 2, 9]
c = [2, 4, 10, 10, 10, 18, 20]
d = [-10, -5, 0, 3, 7]
e = [9, 1, 6]
e = [4, 5, 6, 7, 0, 1, 2]

# print(binary_search_iterative(a, 26))
# print(binary_search_recursive(a, 10, 0, len(a)-1))
# print(first_occurence(b, 2))
# print(last_occurrence(b, 22))
# print(first_occurence(a, 5))
# print(last_occurrence(c, 20))
# print(count_occurrences(b, 2))
# print(index_equals_value(e))
# print(search_sorted_rotated(e, 1))
print([search_sorted_rotated(e, i) for i in e])
