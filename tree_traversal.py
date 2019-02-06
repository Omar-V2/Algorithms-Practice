from array_queue import NaiveQueue as Queue

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self, root=None):
        self.root = root

    def levelorder(self):
        if self.root is None:
            return "This tree is empty"
        else:
            myQueue = Queue()
            myQueue.Enqueue(self.root)
            while not myQueue.isEmpty():
                visited = myQueue.Dequeue()
                print(visited.value)
                if visited.left is not None:
                    myQueue.Enqueue(visited.left)
                if visited.right is not None:
                    myQueue.Enqueue(visited.right)
    
    def pre_order(self, root):
        current = root
        if current is None:
            return
        else:
            print(current.value)
            self.pre_order(current.left)
            self.pre_order(current.right)
    
    def in_order(self, root):
        current = root
        if current is None:
            return
        else:
            self.in_order(current.left)
            print(current.value)
            self.in_order(current.right)

    def post_order(self, root):
        nodes = []
        current = root
        if current is None:
            return
        else:
            self.post_order(current.left)
            self.post_order(current.right)
            nodes.append(current.value)
        return nodes
    
    def is_bst(self, root):
        pass



root = Node('F')
mytree = Tree(root)
branch1 = mytree.root.left = Node('D')
branch2 = mytree.root.right = Node('J')
branch1.left = Node('B')
branch1.right = Node('E')
branch2.left = Node('G')
branch2.right = Node('K')
# print(mytree.levelorder())
# print(mytree.preorder(root))
# print(mytree.inorder(root))
print(mytree.post_order(root))

                