class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root
    
    def insert(self, value, true_insert=True):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)
    
    def _insert(self, value, current):
        if value < current.value:
            if current.left is None:
                current.left = Node(value) # return the value of the node prior the where the inserted element would have gone
            else:
                self._insert(value, current.left)
        elif value > current.value:
            if current.right is None:
                    current.right = Node(value)
            else:
                self._insert(value, current.right)
    
    def search(self, value):
        if self.root is None:
            return False
        else:
            return self._search(value, self.root)
    
    def _search(self, value, current, diff=100): # still not working!
        if diff > abs(value-current.value):
            diff = abs(value-current.value)
            ans = current.value
            print(diff, ans)
        if value == current.value:
            return value
        elif value < current.value:
            if current.left is None:
                return ans
            else:
                return self._search(value, current.left)
        else:
            if current.right is None:
                return ans
            else:
                return self._search(value, current.right)


# root = Node(1)
# myBST = BinarySearchTree(root)
# myBST.insert(5)

def solution(stores, houses):
    root = Node(stores[0])
    storesBST = BinarySearchTree(root)
    closest = []
    for i in stores[1:]:
        storesBST.insert(i)
    for i in houses:
        closest.append(storesBST.search(i))
    return closest

stores = [1, 5, 20, 11, 16]
houses = [19] # doesn't work on this test case, can correct by keeping track of closest as we move through BST
print(solution(stores, houses)) 