from linked_list import Node, LinkedList


def removeDups(head):
    count = {}
    current = head
    previous = None
    while current is not None:
        if current.value in count:
            previous.next = current.next
        else:
            count[current.value] = 1
            previous = current
        current = current.next

head = Node(2)
myLinkedList = LinkedList(head)
myLinkedList.add_end(5)
myLinkedList.add_end(4)
myLinkedList.add_end(2)
myLinkedList.add_end(5)
print(myLinkedList.show())
removeDups(head)
print(myLinkedList.show())