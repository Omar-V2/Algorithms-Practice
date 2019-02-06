from array_stack import Stack

def sortStack(s):
    right = Stack()
    while not s.isEmpty():
        temp = s.pop()
        while not right.isEmpty() and right.top() > temp:
            s.push(right.pop())
        right.push(temp)
    while not right.isEmpty():
        s.push(right.pop())
    return s

a = [4, 2, 1, 5]
s = Stack()
[s.push(i) for i in a]
n = sortStack(s)
print(n.items)