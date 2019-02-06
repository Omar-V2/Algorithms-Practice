from linked_list import Node, LinkedList


def intersection(l1_head, l2_head):
    current1 = l1_head
    current2 = l2_head
    seen = {}
    while current1:
        seen[current1] = 1
        current1 = current1.next
    while current2:
        if current2 in seen:
            return current2.value
        current2 = current2.next
    return False

def intersection2(l1_head, l2_head):
    pA = l1_head
    pB = l2_head
    while pA != pB:
        if pA is None:
            pA = l2_head
        else:
            pA = pA.next
        if pB is None:
            pB = l1_head
        else:
            pB = pB.next
    return pA.value




    # l1_size = 0
    # l2_size = 0
    # l1_current = l1_head
    # l2_current = l2_head
    # while l1_current:
    #     l1_size += 1
    #     l1_current = l1_current.next
    # while l2_current:
    #     l2_size += 1
    #     l2_current = l2_current.next
    # l1_current = l1_head
    # l2_current = l2_head   
    # if l1_size > l2_size:
    #     pass

head1 = Node(1)
intersect = Node(2)
l1 = LinkedList(head1)
l1.head.next = intersect # 1-2-3
l1.add_end(3)
head2 = Node(5)
l2 = LinkedList(head2)
l2.add_end(intersect)
l2.add_end(3)
# l2.add_end(1)
# l2.add_end(6)
# l2.head.next.next.next.next = intersect
print(intersection(head1, head2))

