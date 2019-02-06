class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root
    
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)
    
    def search(self, value):
        if self.root is not None:
            return self._search(value, self.root)
        else:
            return False
        
    def find_max(self):
        if self.root is not None:
            return self._find_max(self.root)
        else:
            return "This binary search tree is empty"
    
    def find_min(self):
        if self.root is not None:
            return self._find_min(self.root)
        else:
            return "This binary search tree is empty"
    
    def find_height(self):
        if self.root is not None:
            return self._find_height(self.root)
        else:
            return 0

    def _insert(self, value, current):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert(value, current.left)
        elif value > current.value:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert(value, current.right)
        else:
            print("Value already in tree")
    
    def _search(self, value, current):
        if value == current.value:
            return True
        elif value < current.value:
            if current.left is None:
                return False
            else:
                return self._search(value, current.left)
        else:
            if current.right is None:
                return False
            else:
                return self._search(value, current.right)
    
    def _find_max(self, current):
        # iterative
        while current.right is not None:
            current = current.right
        return current.value
        # recursive 
        # if current.right is None:
        #     return current.value
        # else:
        #     return self._find_max(current.right)

    def _find_min(self, current):
        # iterative
        # while current.left is not None:
        #     current = current.left
        # return current.value
        # recursive
        if current.left is None:
            return current.value
        else:
            return self._find_min(current.left)
    
    def _find_height(self, current): # need to understand this better 
        if current is None:
            return 0
        else:
            return max(self._find_height(current.left), self._find_height(current.right)) + 1



    

root = Node(15)
bst = BinarySearchTree(root)
bst.insert(10)
bst.insert(40)
bst.insert(8)
bst.insert(20)
bst.insert(25)
bst.insert(17)
bst.insert(12)
print(bst.search(12))
print(bst.find_max())
print(bst.find_min())
print(bst.find_height())

