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
    
    def __repr__(self):
        return repr(self._print_tree(self.root))
    
    def insert(self, item):
        if not self.root:
            self.root = Node(item)
        else:
            # self._insert_iterative(item, self.root)
            # self._insert_recursive(item, self.root)
            return self._insert_recursive_better(item, self.root)
    
    def search(self, item):
        if not self.root:
            return False
        else:
            # return self._search_iterative(item, self.root)
            # return self._search_recursive(item, self.root)
            return self._search_recursive_better(item, self.root)
    
    def level_order(self):
        queue = []
        current = self.root
        while current:
            print(current)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            current = queue.pop(0)

    
    def get_height(self):
        if not self.root:
            print("This tree is empty")
        else:
            return self._get_height(self.root)
    
    def get_min(self):
        if not self.root:
            print("This tree is empty, it has no minimum")
        else:
            return self._get_min_recursive(self.root)
    
    def get_max(self):
        if not self.root:
            print("This tree is empty, it has no maximum")
        else:
            return self._get_max_recursive(self.root)
    
    def _get_height(self, current):
        if not current:
            return -1
        return max(self._get_height(current.left), self._get_height(current.right)) + 1
    
    def _get_min_recursive(self, current):
        if not current.left:
            return current.value
        else:
            return self._get_min_recursive(current.left)
    
    def _get_min_iterative(self, current):
        while current.left:
            current = current.left
        return current.value
    
    def _get_max_recursive(self, current):
        if not current.right:
            return current.value
        else:
            return self._get_max_recursive(current.right)
    
    def _get_max_iterative(self, current):
        while current.right:
            current = current.right
        return current.value

    
    def _insert_recursive(self, item, current):
        if item > current.value:
            if not current.right:
                current.right = Node(item)
                return
            else:
                self._insert_recursive(item, current.right)
        elif item < current.value:
            if not current.left:
                current.left = Node(item)
                return
            else:
                self._insert_recursive(item, current.left)
        else:
            print(f'{item} is already present in the tree')
    
    def _insert_recursive_better(self, item, current):
        if not current:
            return Node(item)
        if item > current.value:
            current.right = self._insert_recursive_better(item, current.right)
        elif item < current.value:
            current.left = self._insert_recursive_better(item, current.left)
        else:
            print(f'{item} is already present in the tree')
        return current
    
    def _insert_iterative(self, item, current):
        while current:
            if item > current.value:
                if not current.right:
                    current.right = Node(item)
                    return
                else:
                    current = current.right
            elif item < current.value:
                if not current.left:
                    current.left = Node(item)
                    return
                else:
                    current = current.left
            else:
                print(f'{item} is already present in th tree')

    def _search_recursive(self, item, current):
        if item == current.value:
            return True
        if item > current.value:
            if not current.right:
                return False
            else:
                return self._search_recursive(item, current.right)
        else:
            if not current.left:
                return False
            else:
                return self._search_recursive(item, current.left)

    def _search_recursive_better(self, item, current):
        if not current:
            return False
        if item == current:
            return True
        if item > current.value:
            return self._search_recursive(item, current.right)
        elif item < current.value:
            return self._search_recursive_better(item, current.left)
        
    def _search_iterative(self, item, current):
        while current:
            if item == current.value:
                return True
            elif item > current.value:
                current = current.right
            else:
                current = current.left
        return False
    
    def _print_tree(self, root):
        if root:
            self._print_tree(root.left)
            print(root.value)
            self._print_tree(root.right)


if __name__ == "__main__":
    # root = Node(5)
    bst = BinarySearchTree()
    bst.insert(6)
    bst.insert(7)
    bst.insert(3)
    bst.insert(5)
    bst.insert(4)
    print(bst)
    print(bst.search(4))
    print(bst.get_min())
    print(bst.get_max())
    print("Height is")
    print(bst.get_height())

    


