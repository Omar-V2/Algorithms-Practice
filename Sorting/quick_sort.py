from random import randint

def quicksort(a, start, end):
    if start < end:
        p = random_partition(a, start, end)
        quicksort(a, start, p-1)
        quicksort(a, p+1, end)
    


def partition(a, start, end):
    pivot = a[end]
    pindex = 0
    for i in range(len(a)):
        if a[i] < pivot:
            a[i], a[pindex] = a[pindex], a[i]
            pindex += 1
    a[end], a[pindex] = a[pindex], a[end]
    return pindex

def random_partition(a, start, end):
    pivot = randint(start, end)
    pindex = 0
    a[end], a[pivot] = a[pivot], a[end]
    for i in range(len(a)):
        if a[i] < a[end]:
            a[i], a[pindex] = a[pindex], a[i]
            pindex += 1
    a[end], a[pindex] = a[pindex], a[end]
    return pindex



# b = [6, 8, 3, 2, 1]
# partition(b, 0, len(b)-1)
# print(b)
# random_partition(b, 0, len(b)-1)
# print(b)

a = [7,3,1,8,2,4]
quicksort(a, 0, len(a)-1)
print(a)