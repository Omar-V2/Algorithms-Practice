def merge_sort(a):
    if len(a) < 2:
        return  
    mid = len(a) // 2
    l = a[:mid]
    r = a[mid:]
    merge_sort(l)
    merge_sort(r)
    merge(l, r, a)

def merge(l, r, a):
    i = j = k = 0
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            a[k] = l[i]
            i += 1
            k += 1
        else:
            a[k] = r[j]
            j += 1
            k += 1
    while i < len(l):
        a[k] = l[i]
        i += 1
        k += 1
    while j < len(r):
        a[k] = r[j]
        j += 1
        k += 1

a = [2, 9, 7, 13, 21, 4, 16]
merge_sort(a)
print(a)
