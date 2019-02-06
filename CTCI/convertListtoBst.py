class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
def convert_to_bst(a):
    start = 0
    end = len(a) - 1
    mid = (start + end) // 2
    left = a[:mid]
    right = a[mid+1:]
    root = current = Node(a[mid])
    for num in left:
        current.left = Node(num)
        current = current.left
    current = root
    for num in right:
        current.right = Node(num)
        current = current.right