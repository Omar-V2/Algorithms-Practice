from array_queue import NaiveQueue as Queue

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class Tree:
    def __init__(self, root):
        self.root = root
    
    def level_order(self):
        if self.root is None:
            return "Empty Tree"
        else:
            myQueue = Queue()
            myQueue.Enqueue(self.root)
            while not myQueue.isEmpty():
                visited = myQueue.Dequeue()
                print(visited.data)
                if visited.left is not None:
                    myQueue.Enqueue(visited.left)
                if visited.right is not None:
                    myQueue.Enqueue(visited.right)




child1 = Node(2)
child2 = Node(3)
leaf1 = Node(4)
leaf2 = Node(5)
root = Node(1, child1, child2)
myTree = Tree(root)
myTree.root.left.left = leaf1
myTree.root.right.right = leaf2


# print(myTree.root.data)
# print(myTree.root.left.data)
# print(myTree.root.right.data)
# print(myTree.root.left.left.data)
# print(myTree.root.right.right.data)

print(myTree.level_order())

