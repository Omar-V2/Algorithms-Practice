class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root
    
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(value, self.root)
    
    def count_equal_nodes(self, count):
        if not self.root:
            return 
        else:
            return self._count_equal_nodes(self.root, count)
    
    def search(self, value):
        if not self.root:
            return False
        else:
            return self._search(value, self.root)
    
    def find_max(self):
        if not self.root:
            return "This binary search tree is empty"
        else:
            return self._find_max(self.root)

    def find_min(self):
        if not self.root:
            return "This binary search tree is empty"
        else:
            return self._find_min(self.root)
    
    def find_height(self):
        if not self.root:
            return 0
        else:
            return self._find_height(self.root)
    
    def in_order(self):
        if not self.root:
            return 0
        else:
            return self._in_order(self.root)
    
    def post_order(self):
        if not self.root:
            return 0
        else:
            return self._post_order(self.root)
        
    def pre_order(self):
        if not self.root:
            return 0
        else:
            return self._pre_order(self.root)

    def isBst(self, current, store=[]):
        if not current:
            return
        else:
            self.isBst(current.left)
            store.append(current.value)
            self.isBst(current.right)
        return store
    
    def first_greater(self, value):
        if not self.root:
            return False
        else:
            return self._first_greater(value, self.root)
        
    def _insert(self, value, current):
        if value < current.value:
            if not current.left:
                current.left = Node(value)
            else:
                self._insert(value, current.left)
        elif value > current.value:
            if not current.right:
                current.right = Node(value)
            else:
                self._insert(value, current.right)
        else:
            print("Value already in tree")
    
    def _first_greater(self, value, current):
        if value < current.value:
            if not current.left:
                return current.value
            else:
                return self._first_greater(value, current.left)
        elif value >= current.value:
            if not current.right:
                return current.value
            else:
                return self._first_greater(value, current.right)
    
    def _count_equal_nodes(self, current, count):
        if not current:
            return
        else:
            if current.left and current.right:
                print(current.left.value + current.right.value)
                if (current.left.value + current.right.value) == current.value:
                    count += 1
            elif current.left and not current.right:
                print(current.left.value)
                if current.left.value == current.value:
                    count += 1
            elif current.right and not current.left:
                print(current.right.value)
                if current.right.value == current.value:
                    count += 1
            self._count_equal_nodes(current.left, count)
            self._count_equal_nodes(current.right, count)
        return count

    
    def _search(self, value, current):
        if value == current.value:
            return True
        elif value < current.value:
            if not current.left:
                return False
            else:
                return self._search(value, current.left)
        elif value > current.value:
            if not current.right:
                return False
            else:
                return self._search(value, current.right)
    
    def _find_max(self, current):
        #recursive
        # if not current.right:
        #     return current.value
        # else:
        #     return self._find_max(current.right)
        #iterative
        while current.right:
            current = current.right
        return current.value
    
    def _find_min(self, current):
        #recursive
        # if not current.left:
        #     return current.value
        # else:
        #     return self._find_min(current.left)
        #iterative
        while current.left:
            current = current.left
        return current.value
    
    def _find_height(self, current):
        if not current:
            return -1
        else:
            return max(self._find_height(current.left), self._find_height(current.right)) + 1
    
    def level_order(self):
        queue = []
        queue.append(self.root)
        while queue:
            visited = queue.pop(0)
            print(visited.value)
            if visited.left:
                queue.append(visited.left)
            if visited.right:
                queue.append(visited.right)

    def _in_order(self, current):
        if not current:
            return
        else:
            self._in_order(current.left)
            print(current.value)
            self._in_order(current.right)

    def _pre_order(self, current):
        if not current:
            return
        else:
            print(current.value)
            self._pre_order(current.left)
            self._pre_order(current.right)

    def _post_order(self, current):
        if not current:
            return
        else:
            self._post_order(current.left)
            self._post_order(current.right)
            print(current.value)

root = Node(8)
bst = BinarySearchTree(root=root)
nodes = [4, 10, 3, 5, 9, 12]
# nodes = [19, 7, 43, 3, 11, 23, 47, 2, 5, 17, 37, 53, 13, 29, 41, 31]
[bst.insert(i) for i in nodes]
# print(bst.root.right.value)
print(bst.count_equal_nodes(0))