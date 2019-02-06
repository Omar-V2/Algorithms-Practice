from array_stack import Stack


class SetofStacks:
    def __init__(self, capacity):
        self.capacity = capacity
        self.set_of_stacks = []
        self.current = 0
    
    def push(self, x):
        if not self.set_of_stacks:
            self.set_of_stacks.append(Stack())
            s = self.set_of_stacks[0]
            s.push(x)
        else:
            if len(self.set_of_stacks[-1].items) == self.capacity:
                self.set_of_stacks.append(Stack())
            self.set_of_stacks[-1].push(x)
