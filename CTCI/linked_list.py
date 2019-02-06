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
    
    def add_end_node(self, node):
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = node
    
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
    
    def print_reverse(self, current):
        if not current:
            return    
        self.print_reverse(current.next)
        print(current.value)

    def show(self):
        current = self.head
        list_str = "{}->".format(current.value)
        while current.next is not None:
            current = current.next
            list_str += "{}->".format(current.value)
        list_str += "Null"
        return list_str
    
    def show_recursive(self, head):
        if head.next is None:   
            return
        else:
            print(head.value) # swap these to lines to reverse the order of printing
            self.show_recursive(head.next)
    
    def removeDups(self):
        count = {}
        current = self.head
        previous = None
        while current is not None:
            if current.value in count:
                previous.next = current.next
            else:
                count[current.value] = 1
                previous = current
            current = current.next
    
    def partitionLinkedList(self, partition):
        current = self.head
        small = []
        big = []
        while current is not None:
            if current.value < partition:
                small.append(current.value)
            else:
                big.append(current.value)
            current = current.next
        self.head = Node(small[0])
        current = self.head
        for value in small[1:]:
            current.next = Node(value)
            current = current.next
        for value in big:
            current.next = Node(value)
            current = current.next
        

if __name__ == "__main__":
    head = Node(3)
    myLinkedList = LinkedList(head)
    nodes = [5, 5, 5, 10, 2, 1]
    [myLinkedList.add_end(i) for i in nodes]
    print(myLinkedList.show())
    myLinkedList.reverse_recursive(head)
    print(myLinkedList.show())
    # myLinkedList.removeDups()
    # print(myLinkedList.show())
    # myLinkedList.partitionLinkedList(5)
    # print(myLinkedList.show())