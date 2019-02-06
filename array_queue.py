class NaiveQueue:
    def __init__(self):
        self.items = []
    
    def Enqueue(self, x):
        self.items.append(x) # head is at index 0
        # self.items.insert(0, x) # head is at end of list
    
    def Dequeue(self):
        return self.items.pop(0) # head is at index 0
        # return self.items.pop() # head is at end of list
    
    def isEmpty(self):
        return self.items == []


class EfficientQueue:
    def __init__(self):
        self.items = []
        self.head = 0
        self.rear = 0
    
    def Enqueue(self):
        pass
    
    def Dequeue(self):
        pass


if __name__ == "__main__":
    myQueue = NaiveQueue()
    myQueue.Enqueue(2)
    myQueue.Enqueue(5)
    myQueue.Enqueue(3)
    print(myQueue.items)
    myQueue.Dequeue()
    print(myQueue.items)