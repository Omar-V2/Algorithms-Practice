def search_rotated_array(nums, target):
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = int((start + end) / 2)
        if nums[mid] == target:
            return mid
        elif nums[mid] <= nums[end]:
            if target > nums[mid] and target <= nums[end]:
                start = mid + 1
            else:
                end = mid - 1
        elif nums[start] <= nums[mid]:
            if target >= nums[start] and target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
    return -1