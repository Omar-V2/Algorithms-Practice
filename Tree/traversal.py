class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def __repr__(self):
        return repr(self.value)

class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root
    
    def insert(self, item):
        if not self.root:
            self.root = Node(item)
        else:
            return self._insert(self.root, item)
    
    def level_order(self):
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            print(current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

    def in_order(self, current):
        if not current:
            return
        self.in_order(current.left)
        print(current.value)
        self.in_order(current.right)
    
    def pre_order(self, current):
        if not current:
            return
        print(current.value)
        self.pre_order(current.left)
        self.pre_order(current.right)
        
    
    def post_order(self, current):
        if not current:
            return
        self.post_order(current.left)
        self.post_order(current.right)
        print(current.value)

    def _insert(self, current, item):
        if not current:
            return Node(item)
        if item > current.value:
            current.right = self._insert(current.right, item)
        else:
            current.left = self._insert(current.left, item)
        return current


if __name__ == "__main__":
    bst = BinarySearchTree()
    letters = ["F", "D", "J", "B", "E", "G", "K", "A", "C", "I", "H"]
    [bst.insert(letter) for letter in letters]
    # print(bst.level_order())
    print(bst.in_order(bst.root))
    # print(bst.post_order(bst.root))
    # print(bst.pre_order(bst.root))

        