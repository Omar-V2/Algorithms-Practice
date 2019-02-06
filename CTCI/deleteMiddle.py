from linked_list import Node, LinkedList


def deleteMiddle(node):
    node.value = node.next.value
    node.next = node.next.next
