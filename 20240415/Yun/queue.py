class Queue:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.arr = [None] * capacity
        self.front_, self.rear_ = -1, -1

    def size(self):
        return self.rear_ - self.front_
    
    def empty(self):
        return not self.size()
    
    def full(self):
        return self.capacity - 1 <= self.rear_

    def __str__(self):
        return f"{self.arr}"
    
    def front(self):
        return self.arr[self.front_ + 1]

    def rear(self):
        return self.arr[self.rear_]

    def enqueue(self, data):
        if self.full():
            raise Exception("enqueue from full queue")
        
        self.rear_ += 1
        self.arr[self.rear_] = data
    
    def dequeue(self):
        if self.empty():
            raise Exception("dequeue from empty queue")
        
        i = self.front_ + 1
        ret = self.arr[i]
        while i < self.rear_:
            self.arr[i] = self.arr[i+1]
            i += 1
        
        self.arr[self.rear_] = None
        self.rear_ -= 1

        return ret
    
if __name__ == "__main__":
    SIZE = 5
    queue = Queue(SIZE)
    
    for data in range(10, 60, 10):
        queue.enqueue(data)
        print(f"queue = {queue}")
    print()

    print(f">> queue.dequeue() = {queue.dequeue()}")
    print(f"queue = {queue}")
    print(f">> queue.status:{queue.front_, queue.rear_}")
    print(f">> queue.dequeue() = {queue.dequeue()}")
    print(f"queue = {queue}")
    print(f">> queue.status:{queue.front_, queue.rear_}")
    print(f">> queue.dequeue() = {queue.dequeue()}")
    print(f">> queue.status:{queue.front_, queue.rear_}")
    print(f"queue = {queue}")
    print(f">> queue.dequeue() = {queue.dequeue()}")
    print(f">> queue.status:{queue.front_, queue.rear_}")
