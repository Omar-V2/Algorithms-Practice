def selection_sort(a):
    sorted_length = 0
    while sorted_length < len(a):
        min_index = None
        for i in range(len(a[sorted_length:])):
            if min_index is None or a[i] < a[min_index]:
                min_index = i + sorted_length
        a[min_index], a[sorted_length] = a[sorted_length], a[min_index]
        sorted_length += 1
    return a

a = [5, 7, 2, 4]
print(selection_sort(a))