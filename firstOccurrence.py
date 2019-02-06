def firstOccurence(arr):
    start = 0
    end = len(arr)
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == 1 and arr[mid - 1] == 0:
            return mid
        elif arr[mid] == 0:
            pass