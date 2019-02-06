def bubble_sort(a):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                swapped = True
    return a

a = [5, 7, 2, 4]
print(bubble_sort(a))