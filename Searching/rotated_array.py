def rotated_sorted_array(A):
    size = len(A)
    start = 0
    end = size - 1
    left = lambda i: (i + (size - 1)) % size
    right = lambda i: (i + 1) % size
    while start <= end:
        mid = int((start + end) / 2)
        if A[start] <= A[end]:
            return start
        # if left and right elements are both greater, we must be on the minimum element
        if A[left(mid)] > A[mid] and A[right(mid)] > A[mid]:
            return mid
        if A[start] <= A[mid]:
            start = mid + 1
        elif A[mid] <= A[end]:
            end = mid - 1

# items = [8, 11, 12, 2, 3, 5]
# items = [2, 3, 5, 8, 11, 12]
# items = [11, 12, 2, 3, 5, 8]
items = [3, 5, 8, 11, 12, 2]
print(rotated_sorted_array(items))
    