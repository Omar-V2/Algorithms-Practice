from linked_list import Node, LinkedList


def kthToLast(head, k):
    size = 1
    current = head
    while current.next is not None:
        size += 1
        current = current.next
    current = head
    target = size - k
    steps = 1
    while steps <= target:
        steps += 1
        current = current.next
    return current.value

def kthToLastRunner(head, k):
    runner = head
    current = head
    for i in range(k):
        runner = runner.next
    while runner is not None:
        current = current.next
        runner = runner.next
    return current.value


head = Node(2)
myLinkedList = LinkedList(head)
myLinkedList.add_end(5)
myLinkedList.add_end(4)
myLinkedList.add_end(2)
myLinkedList.add_end(5)
print(myLinkedList.show())
print(kthToLast(head, 3))
print(kthToLastRunner(head, 3))