from linked_list import LinkedList, Node


def sumLists(l1, l2):
    current1 = l1.head
    current2 = l2.head
    carry = 0
    first_iteration = True
    while current1 and current2:
        first_sum = current1.value + current2.value
        first_sum += carry
        if first_sum > 10:
            carry = first_sum // 10
            rem = first_sum % 10
            if first_iteration:
                solution = LinkedList(head=Node(rem))
                first_iteration = False
            else:
                solution.add_end(rem)
        else:
            if first_iteration:
                solution = LinkedList(head=Node(first_sum))
                first_iteration = False
            else:
                solution.add_end(first_sum)
        current1 = current1.next
        current2 = current2.next
    if carry > 0:
        solution.add_end(carry)
    return solution

def sumLists2(l1, l2):
    c1 = l1.head
    c2 = l2.head
    carry = 0
    first_iteration = True
    while c1 or c2:
        val = carry
        if c1:
            val += c1.value
            c1 = c1.next
        if c2:
            val += c2.value
            c2 = c2.next
        carry = val // 10
        rem = val % 10
        if first_iteration:
            solution = LinkedList(Node(rem))
            first_iteration = False
        else:
            solution.add_end(rem)
    if carry > 0:
        solution.add_end(carry)
    return solution

l1 = LinkedList(head=Node(7))
l1.add_end(1)
l1.add_end(6)
l2 = LinkedList(head=Node(2))
l2.add_end(1)
# l2.add_end(9)

# s = sumLists(l1, l2)
s = sumLists2(l1, l2)
print(s.show())



def sumLists3(l1, l2):
    carry = 0
    c1 = l1.head
    c2 = l2.head
    first_iteration = True
    while c1 or c2:
        first_sum = carry
        if c1:
            first_sum += c1.value
            c1 = c1.next
        if c2:
            first_sum += c2.value
            c2 = c2.next
        carry = first_sum // 10
        rem = first_sum % 10
        if first_iteration:
            solution = LinkedList(Node(rem))
            first_iteration = False
        else:
            solution.add_end(rem)
    if carry > 0:
        solution.add_end(carry)
    return solution

        

s = sumLists3(l1, l2)
print(s.show())