def move_zeros(a):
    start = 0
    end = len(a) - 1
    while start < end:
        if a[start] == 0 and a[end] != 0:
            a[start], a[end] = a[end], a[start]
            start += 1
            end -= 1
        elif a[start] == 0 and a[end] == 0:
            end -= 1
        else:
            start += 1
    return a

def move_zeros2(a):
    first = 0
    second = 1
    while second < len(a):
        if a[first] == 0 and a[second] == 0:
            print("both are zeros")
            second += 1
        elif a[first] == 0 or a[second] == 0:
            print("only one zero")
            a[first], a[second] = a[second], a[first]
            first += 1
            second += 1
        else:
            print("both non zero")
            first += 1
            second += 1
    return a

def move_zeros3(a):
    start = 0 
    end = len(a) - 1
    while start < end:
        if a[start] != 0:
            start += 1
        else:
            a[start], a[end] = a[end], a[start]
            end -= 1
    return a


def words_and_numbers(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        if type(a[start]) == int or type(a[start]) == float:
            start += 1
        


a = [0, 1, 5, 0, 3, 0, 4, 1, 0]
b = [0,1,0,3,12]
# print(move_zeros(a))
print(move_zeros(b))
# print(move_zeros3(a))
# print(move_zeros2(b))