class Stack:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.arr = [None] * capacity
        self.top = -1
    def empty(self):
        return -1 == self.top
    def full(self):
        return self.capacity - 1 <= self.top
    def size(self):
        return self.top + 1
    def push(self, data):
        if self.full():
            raise IndexError("push from full stack")
        
        self.top += 1
        self.arr[self.top] = data
    def peek(self):
        if self.empty():
            raise IndexError("push from empty stack")

        return self.arr[self.top]
    def pop(self):
        if self.empty():
            raise IndexError("push from empty stack")

        ret = self.arr[self.top]
        self.arr[self.top] = None
        self.top -= 1
        return ret       

stack = Stack(5)
for i in range(5):
    stack.push(i)
# stack.push(5)

print(stack.arr)
