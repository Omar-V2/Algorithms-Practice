from linked_list import Node, LinkedList
# 2-3-7
# 3-11
# merge to become 2-3-3-7-11
l1 = LinkedList(Node(2))
l2 = LinkedList(Node(3))
l1.add_end(3)
l1.add_end(7)
l2.add_end(11)

def merge_sorted_linkedlists(l1, l2):
    c1 = l1.head
    c2 = l2.head
    ans = tail = Node(0)
    while c1 and c2:
        if c1.data < c2.data:
            print(c1.data)
            tail.next = c1
            c1 = c1.next
        else:
            print(c2.data)
            tail.next = c2
            c2 = c2.next
        tail = tail.next
    while c1:
        print(c1.data)
        tail.next = c1
        c1 = c1.next
    while c2:
        print(c2.data)
        tail.next = c2
        c2 = c2.next
    return ans

tail = merge_sorted_linkedlists(l1, l2)
tail = LinkedList(tail)
print(tail.show())