##Ex1
SIZE = 10
list_ = list(range(1, SIZE + 1))

print(f"list = {list_}")
print()

print(" addr\tvalue")
for i in list_:
    print(f"{id(i):8}\t{i:5}")

##Ex2
list_ = [1, 3, 1, 2, 3, 6, 2, 2, 4, 4]
print(f"list = {list_}")
print()

print(" addr\tvalue")
for i in list_:
    print(f"{id(i):8}\t{i:5}")

##Ex3
class Array:
    def __init__(self, capacity=10, fill=None):
        self.arr = [fill] * capacity
    def get(self, index):
        return self.arr[index]
    def set(self, index, value):
        self.arr[index] = value
    def __str__(self):
        if not len(self.arr):
            return "[]"
        
        ret = "["
        for elem in self.arr:
            ret += f"{elem}, "
        ret += "\b\b]"
        return ret
SIZE = 5
arr = Array(SIZE)
print(arr)
arr.set(0, 10)
arr.set(2, 30)
arr.set(1, 40)
arr.set(3, 20)
arr.set(4, 50)
print(f"arr = {arr}")

for i in range(SIZE):
    arr.set(i, i * 100)
print(f"arr = {arr}")

##Ex4. Fixed-length Array
class Array:
    def __init__(self, capacity=10, fill=None):
        self.arr = [fill] * capacity
        self.cur = 0
    def get(self, index):
        return self.arr[index]
    def set(self, index, value):
        self.arr[index] = value
    def add(self, value):
        self.set(self.cur, value)
        self.cur += 1
    def __str__(self):
        if not len(self.arr):
            return "[]"
        
        ret = "["
        for elem in self.arr:
            ret += f"{elem}, "
        ret += "\b\b]"
        return ret

SIZE = 10
arr = Array(SIZE)
print(arr)

arr.add(1)
arr.add(2)
arr.add(3)
arr.add(4)
arr.add(5)
print(f"arr = {arr}")
for i in range(5, SIZE):
    arr.add(i * 10)
print(f"arr = {arr}")

##Ex5. variable-length Array
class Array:
    def __init__(self, capacity=10, fill=None):
        self.arr = [fill] * capacity
        self.fill = fill
        self.capacity = capacity
        self.cur = 0
    def get(self, index):
        return self.arr[index]
    def set(self, index, value):
        self.arr[index] = value
    def add(self, value):
        if self.cur == len(self.arr):
            self.arr += [self.fill] * self.capacity
        
        self.set(self.cur, value)
        self.cur += 1
    def __str__(self):
        if not len(self.arr):
            return "[]"
        
        ret = "["
        for elem in self.arr:
            ret += f"{elem}, "
        ret += "\b\b]"
        return ret

SIZE = 5
arr = Array(SIZE)
print(f"arr = {arr}")

for i in range(SIZE):
    arr.add(i)
print(f"arr = {arr}")
arr.add(5)
print(f"arr = {arr}")
arr.add(6)
print(f"arr = {arr}")

##Ex6. Insert
class Array:
    def __init__(self, capacity=10, fill=None):
        self.arr = [fill] * capacity
        self.fill = fill
        self.capacity = capacity
        self.cur = 0
    def get(self, index):
        return self.arr[index]
    def set(self, index, value):
        self.arr[index] = value
    def add(self, value):
        if self.cur == len(self.arr):
            self.arr += [self.fill] * self.capacity
        
        self.set(self.cur, value)
        self.cur += 1
    def insert(self, index, value):
        self.add(None)

        i = len(self.arr) -1
        while i >= index:
            self.arr[i] = self.arr[i-1]
            i -= 1
        self.arr[index] = value
    def __str__(self):
        if not len(self.arr):
            return "[]"
        
        ret = "["
        for elem in self.arr:
            ret += f"{elem}, "
        ret += "\b\b]"
        return ret

SIZE = 5
arr = Array(SIZE)
print(f"arr = {arr}")
for i in range(0, 3):
    arr.add(i)

print(f"arr = {arr}")
arr.insert(0, 100)
print(f"arr = {arr}")
arr.insert(3, 200)
print(f"arr = {arr}")
arr.insert(4, 700)
print(f"arr = {arr}")
arr.add(800)
print(f"arr = {arr}")
