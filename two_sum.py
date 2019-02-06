def twoSum(array, target):
    mydict = {}
    for i in array:
        if i in mydict:
            return i, mydict[i]
        else:
            mydict[target - i] = i

def twoSumNaive(array, target):
    for first in range(len(array)):
        for second in range(len(array)):
            if array[first] + array[second] == target:
                return [array[second], array[first]]

# 1, 2, 5, 7 t = 9

print(twoSum([1,2,5,7], 9))
print(twoSumNaive([1,2,5,7], 9))