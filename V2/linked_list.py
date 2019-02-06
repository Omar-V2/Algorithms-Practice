class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def add_end(self, value):
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(value)
    
    def add_start(self, value):
        new = Node(value)
        new.next = self.head
        self.head = new
    
    def add_nth(self, value, n):
        current = self.head
        new = Node(value)
        for i in range(n-1):
            previous = current
            current = current.next
        previous.next = new
        new.next = current
    
    def delete_nth(self, n):
        current = self.head
        for i in range(n-1):
            previous = current
            current = current.next
        previous.next = current.next
    
    def reverse(self):
        current = self.head
        previous = None
        while current is not None:
            next_node = current.next # the next node in the original list
            current.next = previous
            previous = current
            current = next_node
        self.head = previous
    
    def reverse_recursive(self, head): # revisit this later
        if head is None or head.next is None:
            self.head = head # when we reach the final element (excluding None), we make it the head
            return
        else:
            self.reverse_recursive(head.next)
            q = head.next
            q.next = head
            head.next = None


    def show(self):
        current = self.head
        list_str = "{}->".format(current.value)
        while current.next is not None:
            current = current.next
            list_str += "{}->".format(current.value)
        list_str += "Null"
        return list_str
    
    def __repr__(self):
        return self.show()
    
    def show_recursive(self, head):
        if head.next is None:   
            return
        else:
            print(head.value) # swap these to lines to reverse the order of printing
            self.show_recursive(head.next)


head = Node(1)
myLinkedList = LinkedList(head)
myLinkedList.add_end(2)
myLinkedList.add_end(3)
myLinkedList.add_end(4)
# myLinkedList.reverse()
# myLinkedList.reverse_recursive(head)
print(myLinkedList)
# print(myLinkedList.show())