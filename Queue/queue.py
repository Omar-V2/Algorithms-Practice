class Queue:
    def __init__(self, capacity):
        self.front = -1
        self.rear = -1
        self.capacity = capacity
        self.items = [None]*self.capacity
    
    def __repr__(self):
        current_items = self.items[self.front:self.rear+1]
        return repr(current_items)
    
    def enqueue(self, item):
        if self.is_empty():
            self.front += 1
        elif self.is_full():
            print("Queue overflow")
            return
        self.rear += 1
        self.items[self.rear] = item
    
    def dequeue(self):
        if self.is_empty():
            print("Queue underflow")
            return
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front += 1
    
    def is_empty(self):
        return self.front == -1 and self.rear == -1

    def is_full(self):
        return self.rear == self.capacity - 1

if __name__ == "__main__":
    queue = Queue(5)
    queue.enqueue(5)
    queue.enqueue(5)
    queue.enqueue(4)
    queue.enqueue(3)
    queue.enqueue(2)
    queue.dequeue()
    queue.enqueue(7)
    print(queue)
    print(queue.items)