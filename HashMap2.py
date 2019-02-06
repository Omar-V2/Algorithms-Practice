class HashMap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [[] for _ in range(self.capacity)]
    
    def load_factor(self):
        used_slots = [i for i in self.items if i]
        lf = len(used_slots)*1.0 / len(self.items)
        return lf

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
        if not self.items[index]:
            self.items[index].append([key, value])
        else:
            for pairs in self.items[index]:
                if pairs[0] == key:
                    pairs[1] = value
                    return
            self.items[index].append([key, value])

    def get(self, key):
        index = self._compute_hash(key)
        print(self.items[index])
        if not self.items[index]:
            return False
        else:
            for pair in self.items[index]:
                if pair[0] == key:
                    return pair
        return False
    
    def delete(self, key):
        index = self._compute_hash(key)
        if not self.items[index]:
            return False
        else:
            for i, pair in enumerate(self.items[index]):
                if pair[0] == key:
                    self.items[index].pop(i)
                    return

        
            
hm = HashMap(10)
hm.put("Omar", "hi")
hm.put("Omar", "test")
hm.put("Od", "test")
print(hm.get("Od"))
# print(hm.get("O"))
# hm.delete("Omar")
hm.delete("O")
print(hm.items)
# print(hm.load_factor())