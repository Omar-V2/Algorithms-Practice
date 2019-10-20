class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def __repr__(self):
        return repr(self.show_items())
    
    def enqueue(self, item):
        next_item = Node(item)
        if not self.front and not self.rear:
            self.front = self.rear = next_item
            return
        self.rear.next = next_item
        self.rear = next_item
    
    def dequeue(self):
        if not self.front:
            return
        self.front = self.front.next
    
    def show_items(self):
        items = []
        current = self.front
        while current:
            items.append(current.value)
            current = current.next
        return items

if __name__ == "__main__":
    ll_queue = Queue()
    ll_queue.enqueue(5)
    ll_queue.enqueue(3)
    ll_queue.enqueue(7)
    ll_queue.dequeue()
    ll_queue.enqueue(23)
    ll_queue.enqueue(28)
    ll_queue.enqueue(9)
    ll_queue.dequeue()
    ll_queue.dequeue()
    print(ll_queue)

        
        