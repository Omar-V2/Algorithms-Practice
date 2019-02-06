class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _add(self, node):
        p = self.tail.prev
        p.next = node
        node.prev = p
        node.next = self.tail
        self.tail.prev = node
    
    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
    
    def get(self, key):
        if key in self.items:
            n = self.items[key]
            self._remove(n)
            self._add(n)
            return n.value
        return -1

    def put(self, key, value):
        if key in self.items:
            self._remove(self.items[key])
        n = Node(key, value)
        self._add(n)
        self.items[key] = n
        if len(self.items) > self.capacity:
            n = self.head.next
            self._remove(n)
            del self.items[n.key]
