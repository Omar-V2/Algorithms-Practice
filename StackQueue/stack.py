class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []
    
if __name__ == "__main__":
    stack = Stack()
    test_str = "Hello World"
    for char in test_str:
        stack.push(char)
    reversed_str = ""
    while not stack.is_empty():
        reversed_str += stack.pop()
    print(reversed_str)