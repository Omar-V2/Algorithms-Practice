class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def top(self):
        return self.items[-1]
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)


if __name__ == "__main__":

    mystack = Stack()
    mystack.push(5)
    mystack.push(4)
    mystack.push(3)
    print(mystack.top())
    print(mystack.items)
    mystack.pop()
    print(mystack.isEmpty())


    # reverse a string using a stack 
    some_str = "hello"
    reversed_str = ""
    str_stack = Stack()
    for char in some_str:
        str_stack.push(char)

    while not str_stack.isEmpty():
        reversed_str += str_stack.pop()
    print(some_str)
    print(reversed_str)