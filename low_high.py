def low_high(a):
    high = True
    end = len(a) - 1
    for i in range(len(a)-1):
        if high:
            if a[i] < a[i+1]:
                high = False
            else:
                while a[end] < a[i]:
                    end -= 1
                a[end], a[i+1], a[i+1], a[end]
                end = len(a) - 1
                high = False
        else:
            if a[i] > a[i+1]:
                high = True
            else:
                while a[end] > a[i]:
                    end -= 1
                a[end], a[i+1] = a[i+1], a[end]
                end = len(a) - 1
                high = True
    return a

def low_high2(a):
    for i in range(len(a)-1):
        if a[i] < a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
    return a

a = [2,3,6,7,1,8]
print(low_high(a))
print(low_high2(a))