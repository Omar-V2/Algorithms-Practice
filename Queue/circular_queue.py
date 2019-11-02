class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * self.capacity
        self.front = -1
        self.rear = -1
    
    def __repr__(self):
        current_items = self.items[self.front:self.rear+1]
        return repr(current_items)

    def enqueue(self, item):
        if self.is_empty():
            self.front += 1
        elif self.is_full():
            print("Queue overflow")
            return
        self.rear = (self.rear + 1) % self.capacity
        self.items[self.rear] = item
    
    def dequeue(self):
        if self.is_empty():
            print("Queue underflow")
            return
        elif self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity

    def is_empty(self):
        return self.front == -1 and self.rear == -1
    
    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front


if __name__ == "__main__":
    c_queue = CircularQueue(5)
    c_queue.enqueue(5)
    c_queue.enqueue(5)
    c_queue.enqueue(4)
    c_queue.enqueue(3)
    c_queue.enqueue(2)
    c_queue.dequeue()
    c_queue.enqueue(7)
    print(c_queue)
    print(c_queue.items)
    