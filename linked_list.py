from array_stack import Stack


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, head):
        self.head = head
    
    def __repr__(self):
        return self.show_list()
    
    def add_end(self, data):
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(data) # add_end item to the end of the list - O(n)
    
    def add_start(self, data):
        item = Node(data)
        item.next = self.head # this is new head, so now make it point to old head
        self.head = item
    
    def add_nth(self, data, n):
        item = Node(data)
        current = self.head
        for i in range(n-1):
            previous = current
            current = current.next
        previous.next = item
        item.next = current
    
    def remove_nth(self, n):
        current = self.head
        previous = None
        for i in range(n-1):
            previous = current # 1-2-3-4 1,2
            current = current.next 
        previous.next = current.next

    def size(self):
        current = self.head
        count = 1
        while current.next is not None:
            count += 1
            current = current.next
        return count

    def show(self):
        mylist = [self.head.data]
        current = self.head
        while current.next is not None:
            current = current.next
            mylist.append(current.data)
        return mylist

    def show_list(self):
        current = self.head
        list_str = "{}->".format(current.data)
        while current.next is not None:
            current = current.next
            list_str += "{}->".format(current.data)
        list_str += "Null"
        return list_str      
    
    def reverse(self):
        current = self.head
        previous = None
        while current is not None:
            next_node = current.next
            current.next = previous # 1-2-3-4
            previous = current
            current = next_node
        self.head = previous
    
    def stack_reverse(self): # not working atm 
        stack = Stack()
        current = self.head
        while current is not None:
            stack.push(current)
            current = current.next
        temp = stack.top()
        self.head = temp
        stack.pop()
        for i in range(stack.size()):
            temp.next = stack.top()
            stack.pop()
            temp = temp.next
    
    def recursive_print(self, head):
        current = head
        if current is None:
            return
        print(current.data)
        self.recursive_print(current.next)
    
    def recursive_reverse(self):
        pass

if __name__ == "__main__":

    head = Node(1)
    mylinkedlist = LinkedList(head)
    mylinkedlist.add_end(2)
    mylinkedlist.add_end(3)
    mylinkedlist.add_end(5)
    mylinkedlist.add_start(9)
    print(mylinkedlist.show())
    # mylinkedlist.add_nth(4, 3)
    print(mylinkedlist.show())
    mylinkedlist.remove_nth(4)
    print(mylinkedlist.show())
    mylinkedlist.reverse()
    print(mylinkedlist.show())
    # print(mylinkedlist.recursive_print(mylinkedlist.head))