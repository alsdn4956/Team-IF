class ArrayList:

    def __init__(self, capacity = 100):
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.size = 0

    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == self.capacity
    
    def insert(self, pos, e):
        if not self.isFull() and 0 <= pos <= self.size:
            for i in range(self.size, pos, -1):
                self.array[i] = self.array[i-1]
            self.array[pos] = e
            self.size += 1
        else: pass

    def delete(self, pos, e):
        if not self.isFull() and 0 <= pos < self.size:
            e = self.array[pos]
            for i in range(self.size, pos, size-1):
                self.array[i] = self.array[i+1]
            size -= 1
            return e
        else: pass

    def display(self):
        for i in range(self.size):
            print(self.array[i], end = ' ')
        print()

if __name__ == '__main__':
    L1 = ArrayList()
    L1.insert(0,'A')
    L1.insert(1,'B')
    L1.insert(2,'C')
    L1.insert(3,'D')
    L1.display()
