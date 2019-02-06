from linked_list import LinkedList, Node

# HashMap with collision resoltution via chaining implemented through Linked Lists.
# Not many test cases so not sure if everything works 100%
class HashMap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * self.capacity
    
    def _compute_hash(self, key):
        if type(key) == str:
            ascii_total = 0
            for c in key:
                ascii_total += ord(c)
            index = ascii_total % self.capacity
        else:
            index = key % self.capacity
        return index
    
    def put(self, key, value):
        index = self._compute_hash(key)
        pair = [key, value]
        if not self.items[index]: # if slot is empty
            self.items[index] = LinkedList(head=Node([key, value]))
        else: # slot is occupied, first check if the present value is the same key
            current = self.items[index].head
            while current:
                pair = current.data
                if pair[0] == key:
                    pair[1] = value
                    return
                current = current.next
            current = self.items[index].head            
            while current.next:
                current = current.next
            current.next = Node([key, value])

    def get(self, key):
        index = self._compute_hash(key)
        if not self.items[index]:
            return False
        else:
            current = self.items[index].head
            while current:
                pair = current.data
                if pair[0] == key:
                    return pair
                current = current.next
        return False
            
    def delete(self, key):
        index = self._compute_hash(key)
        if not self.items[index]:
            return False
        else:
            current = self.items[index].head
            num_items = 0
            while current:
                num_items += 1
                current = current.next
            if num_items == 1: # if only one item is stored at this index then set this index back to None (empty it)
                self.items[index] = None
            else:
                current = self.items[index].head
                pair = current.data
                if pair[0] == key:
                    self.items[index].head = current.next
                else:
                    previous = None
                    while current:
                        pair = current.data
                        if pair[0] == key:
                            previous.next = current.next
                            return
                        previous = current
                        current = current.next






store = HashMap(10)
store.put("Omar", "07500513650")
store.put("Omar", 'test')
store.put("Omar", "test again")
store.put("O", 'hello')
store.put("Mohammed", 5)
print(store.get("O"))
print(store.get("Omar"))
print(store.get("Mohammed"))
store.delete("Mohammed")
# store.delete("Omar")
store.delete("O")
i = store.items
print(i)

