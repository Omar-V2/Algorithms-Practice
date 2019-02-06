def insertion_sort(a):
    for i in range(1, len(a)):
        pos = i
        while a[pos] < a[pos-1] and pos > 0:
            a[pos], a[pos-1] = a[pos-1], a[pos]
            pos -= 1
    return a

def insertion_sort2(a):
    for i in range(1, len(a)):
        current = a[i]
        pos = i
        while pos > 0 and current < a[pos-1]:
            a[pos] = a[pos-1]
            pos -= 1
        a[pos] = current
    return a
a = [5, 7, 2 ,9, 4]
print(insertion_sort(a))