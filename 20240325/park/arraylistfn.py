capacity = 100
array = [None] * 100
size = 0


def isEmpty():
    return size == 0

def isFull():
    return size == capacity

def insert(pos, e):
    global size

    if not isFull() and 0 <= pos <= size:
        for i in range(size, pos, -1):
            array[i] = array[i-1]
        array[pos] = e
        size += 1
    else:
        print("Overflow of Invalid Position")

def delete(pos):
    global size
    if not isEmpty() and 0 <= pos < size:
        e = array[pos]
        for i in range(pos, size-1):
            array[i] = array[i+1]
        size -= 1
        return 0
    else:
        print('Underflow or Invalid Position')

def findItem(e):
    for i in range(size):
        if array[i] == e:
            return i
    return -1

def display():
    for i in range(size):
        print(array[i], end=' ')
    print()

if __name__ == '__main__':
    insert(0, 'A')
    insert(1, 'B')
    insert(2, 'C')
    display()
    delete(0)
    display()

    insert(4, 'D')
    insert(3,'E')
    display()

    e = input('input item to delete : ')
    idx = findItem(e)
    if idx != -1:
        delete(idx)
        display()
