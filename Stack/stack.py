class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def top(self):
        return self.items[-1]

    def is_empty(self):
        return self.items == []

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.head = None
        
    def push(self, item):
        if not self.head:
            self.head = Node(item)
        else:
            new_node = Node(item)
            new_node.next = self.head
            self.head = new_node
    
    def pop(self):
        if not self.head:
            return
        else:
            old_head = self.head
            self.head = self.head.next
            return old_head.data

    def is_empty(self):
        if not self.head:
            return True
        return False
    
    def show_items(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

if __name__ == "__main__":
    # stack = Stack()
    stack = StackLinkedList()
    test_str = "Hello World"
    for char in test_str:
        stack.push(char)
    reversed_str = ""
    while not stack.is_empty():
        reversed_str += stack.pop()
    print(reversed_str)
