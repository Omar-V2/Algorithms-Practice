class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self, head):
        self.head = head
        self.items = []

    def push(self, item):
        item = Node(item)
        item.next = self.head
        self.head = item
    
    def pop(self):
        self.head = self.head.next
    
    def show(self):
        current = self.head
        arr = [current.data]
        while current.next is not None:
            current = current.next
            arr.append(current.data)
        return arr


head = Node(5)
mystack = Stack(head)
mystack.push(4)
mystack.push(3)
mystack.push(2)
mystack.pop()
print(mystack.show())
            