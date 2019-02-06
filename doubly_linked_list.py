class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self, head):
        self.head = head

    def add_start(self, data):
        item = Node(data)
        self.head.previous = item
        item.next = self.head
        self.head = item
    
    def add_end(self, data):
        item = Node(data)
        current = self.head
        while current.next is not None:
            current = current.next
        item.previous = current
        current.next = item
        
    def show(self):
        current = self.head
        mylist = "{}->".format(current.data)
        while current.next is not None:
            current = current.next
            mylist += "{}->".format(current.data)
        return mylist
    
    def reverse_print(self):
        current = self.head
        while current.next is not None:
            current = current.next
        mylist = "{}->".format(current.data)
        while current.previous is not None:
            current = current.previous
            mylist += "{}->".format(current.data)
        return mylist


head = Node(1)
mylinkedlist = DoublyLinkedList(head)
mylinkedlist.add_start(3)
mylinkedlist.add_start(4)
mylinkedlist.add_end(5)
print(mylinkedlist.show())
print(mylinkedlist.reverse_print())
