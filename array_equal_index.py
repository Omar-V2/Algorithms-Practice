def index_array(arr):
    for index, value in enumerate(arr):
        if index == value:
            return index
    return -1

print(index_array([-8,0,1,3,5]))