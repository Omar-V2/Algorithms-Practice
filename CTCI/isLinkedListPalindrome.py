from linked_list import Node, LinkedList


def isPalindrome(head):
    stack = []
    current = head
    while current:
        stack.append(current.value)
        current = current.next
    current = head # reset head
    while current:
        node = stack.pop()
        if current.value != node:
            return False
        current = current.next
    return True

def isPalindrome2(head):
    current = head
    clone = head
    previous = None
    while clone:
        next_node = clone.next
        clone.next = previous
        previous = clone
        clone = next_node
    clone = previous
    while clone and current:
        if clone.value != current.value:
            return False
        clone = clone.next
        current = current.next
    return True



head = Node(1)
myLinkedList = LinkedList(head)
myLinkedList.add_end(2)
myLinkedList.add_end(2)
myLinkedList.add_end(1)
print(myLinkedList.show())
print(isPalindrome2(head))
# print(myLinkedList.show())

