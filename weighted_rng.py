from random import randint

def weighted_rng(numbers, weights):
    total_weight = sum(weights)
    rnd = randint(0, total_weight-1)
    for i in range(len(weights)):
        if rnd < weights[i]:
            return numbers[i]
        rnd -= weights[i]


def weighted_rng_binary_search(numbers, weights):
    prefix_sum = []
    running_sum = 0
    for w in weights:
        running_sum += w
        prefix_sum.append(running_sum)
    rnd = randint(1, prefix_sum[-1])
    start = 0
    end = len(prefix_sum) - 1
    while start <= end:
        mid = (start + end) // 2
        if prefix_sum[mid] == rnd:
            return numbers[mid]
        elif rnd < prefix_sum[mid]:
            if prefix_sum[mid-1] > rnd:
                end = mid - 1
            else:
                if prefix_sum[mid-1] == rnd:
                    return numbers[mid-1]
                return numbers[mid]
        else:
            start = mid + 1
        

class WeightedRNG:
    def __init__(self):
        self.items = {}
    
    def set(self, key, weight):
        self.items[key] = weight
        self.prefix_sum = []
        pairs = self.items.items()
        running_sum = 0
        for p in pairs:
            running_sum += p[1]
            self.prefix_sum.append([p[0], running_sum])
        
    def get(self):
        start = 0
        end = len(self.prefix_sum) - 1
        rnd = randint(1, self.prefix_sum[-1][1])
        while start <= end:
            mid = (start + end) // 2
            if self.prefix_sum[mid][1] == rnd:
                return self.prefix_sum[mid][0]
            elif rnd < self.prefix_sum[mid][1]:
                if rnd < self.prefix_sum[mid-1][1]:
                    end = mid - 1
                else:
                    if rnd == self.prefix_sum[mid-1][1]:
                        return self.prefix_sum[mid-1][0]
                    else:
                        return self.prefix_sum[mid][0]
            else:
                start = mid + 1
        




myRNG = WeightedRNG()
myRNG.set(1, 1)
myRNG.set(3, 4)
myRNG.set(4, 8)
outputs = [myRNG.get() for _ in range(100)]
counts = [outputs.count(i) for i in myRNG.items.keys()]
print(counts)


numbers = [10, 30, 20, 40]
weights = [2, 6, 2, 1]
# # [1, 7, 9, 10]

# output = [weighted_rng_binary_search(numbers, weights) for _ in range(10000)]
# # # print(output)
# ans = [output.count(i) for i in numbers]
# print([i*1.0/sum(ans) for i in ans])