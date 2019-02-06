import sys

def median_array(a1, a2):
    merged = []
    i = j = k = 0
    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            merged.append(a1[i])
            i += 1
            k += 1
        else:
            merged.append(a2[j])
            j += 1
            k += 1
    while i < len(a1):
        merged.append(a1[i])
        k += 1
        i += 1
    while j < len(a2):
        merged.append(a2[j])
        k += 1
        j += 1
    size = len(merged)    
    if size % 2 != 0:
        return merged[(size)//2]
    else:
        high = ((size-1) // 2) + 1
        low = (size-1) // 2
        print(high, low)
        return (merged[high] + merged[low]) / 2.0

def find_median(a):
    if len(a) % 2 == 0:
        first = len(a)
        second = len(a) - 1
        return (a[first] + a[second] / 2.0)
    else:
        return a[len(a) // 2]

def median(a1, a2):
    if len(a1) < 3:
        return (max(a1[0], a2[0]) + min(a1[1], a2[1])) / 2.0
    else:
        m1 = find_median(a1)
        m2 = find_median(a2)
        m1_idx = a1.index(m1)
        m2_idx = a2.index(m2)
        if m2 > m1:
            return median(a1[m1_idx:], a2[:m2_idx+1])
        else:
            return median(a1[:m1_idx+1], a2[m2_idx:])

def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    start = 0
    end = len(nums1)
    
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    while start <= end:
        part_x = (start + end) // 2
        total_elements = len(nums1) + len(nums2)
        part_y = ((total_elements + 1) // 2 ) - part_x
        low_x = -sys.maxsize if part_x == 0 else nums1[part_x - 1]
        high_x = sys.maxsize if part_x == len(nums1) else nums1[part_x]
        low_y = -sys.maxsize if part_y == 0 else nums2[part_y - 1]
        high_y = sys.maxsize if part_y == len(nums2) else nums2[part_y]
        if low_x <= high_y and low_y <= high_x:
            if total_elements % 2 == 0:
                return ((max(low_x, low_y) + min(high_x, high_y)) / 2.0)
            else:
                return max(low_x, low_y)
        elif low_x > high_y:
            end = part_x - 1
        else:
            start = part_x + 1
                    



a1 = [1,12,15,26, 38]
a2 = [2,13,17,30,45]
print(findMedianSortedArrays(a1, a2))
# print(median(a1, a2))
# print(median_array(a1, a2))
# print(find_median(a1), find_median(a2))