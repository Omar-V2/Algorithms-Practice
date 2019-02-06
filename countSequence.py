def countSequence(a, w1, w2):
    counter = count(a)
    return counter.get((w1, w2), "Sequence not present in array")


def count(a):
    count = {}
    for i in range(len(a)-1):
        if (a[i], a[i+1]) in count:
            count[(a[i], a[i+1])] +=1
        else:
            count[(a[i], a[i+1])] = 1
    return count


a = ["this", "is", "my", "world", "this", "is", "my", "galaxy"]
print(countSequence(a, "this", "is"))