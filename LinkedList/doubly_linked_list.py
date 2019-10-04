class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None
    
class DoublyLinkedList:
    def __init__(self, head):
        self.head = head
    
    def __repr__(self):
        return self.print_nodes()

    def insert_front(self, node):
        node.next = self.head
        self.head.previous = node
        self.head = node
    
    def insert_end(self, node):
        current = self.head
        while current.next:
            current = current.next
        current.next = node
        node.previous = current
    
    def insert_i(self, node, position):
        # 0 indexed, position 0 is the position of head
        if position == 0:
            self.insert_front(node)
            return
        current = self.head
        for _ in range(position):
            current = current.next
        previous = current.previous
        previous.next = node
        node.previous = previous
        node.next = current
        current.previous = node

    def delete_i(self, position):
        if position == 0:
            next_node = self.head.next
            next_node.previous = None
            self.head = next_node
            return
        current = self.head
        for _ in range(position):
            current = current.next
        previous_node = current.previous
        next_node = current.next
        if current.next:
            previous_node.next = next_node
            next_node.previous = previous_node
        else:
            previous_node.next = next_node

    def print_nodes(self):
        current = self.head
        nodes = ""
        while current.next:
            nodes += str(current.data) + "<->"
            current = current.next
        nodes += str(current.data) + "->Null"
        return nodes


if __name__ == "__main__":
    head = Node(5)
    my_ll = DoublyLinkedList(head)
    my_ll.insert_end(Node(43))
    print(my_ll)
    my_ll.insert_i(Node(4), 1)
    print(my_ll)
    my_ll.delete_i(2)
    print(my_ll)
