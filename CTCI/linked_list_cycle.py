from linked_list import Node, LinkedList


def ll_cycle(head):
    seen = {}
    current = head
    while current.next is not None:
        if current in seen:
            return current.value
        seen[current] = 1
        current = current.next

def ll_cycle2(head):
    slow = head
    fast = head
    previous = None
    while slow:
        print(slow.value, fast.value)
        previous = slow
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return previous.value

    # return previous.value

    


head = Node('A')
cycle = Node('C')
myLinkedList = LinkedList(head)
myLinkedList.add_end('B')
myLinkedList.add_end_node(cycle)
myLinkedList.add_end('D')
myLinkedList.add_end('E')
myLinkedList.add_end_node(cycle)

# print(myLinkedList.show())


print(ll_cycle2(head))


