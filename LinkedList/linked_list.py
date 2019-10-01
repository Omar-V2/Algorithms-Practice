class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, head):
        self.head = head
    
    def __repr__(self):
        return self.print_nodes()
    
    def insert_end(self, node):
        current = self.head
        while current.next:
            current = current.next
        current.next = node
    
    def insert_front(self, node):
        new_head = node
        new_head.next = self.head
        self.head = new_head

    def insert_i(self, node, position):
        # 0 indexed, position value of 0 is the head.
        current = self.head
        if position == 0:
            self.insert_front(node)
            return
        for _ in range(position):
            previous = current
            current = current.next
        previous.next = node
        node.next = current
    
    def delete_i(self, position):
        # 0 indexed, position value of 0 is the head.
        current = self.head
        if position == 0:
            self.head = current.next
            return
        for _ in range(position):
            previous = current
            current = current.next
        previous.next = current.next

    def print_nodes(self):
        current = self.head
        nodes = str(current.data) + "->"
        while current.next:
            current = current.next
            nodes += str(current.data) + "->"
        nodes += "Null"
        return nodes
    
    def size(self):
        length = 1
        current = self.head
        while current.next:
            length += 1
            current = current.next
        return length

    def reverse(self):
        current = self.head
        previous = None
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous


if __name__ == "__main__":
    head = Node(5)
    my_ll = LinkedList(head)
    my_ll.insert_end(Node(4))
    my_ll.insert_i(Node(3), 1)
    print(my_ll)
    my_ll.delete_i(0)
    print(my_ll)
    my_ll.insert_i(Node(7), 0)
    print(my_ll)
    my_ll.reverse()
    print(my_ll)