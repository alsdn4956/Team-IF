#전역 변수 선언
capacity = 100 
array = [None] * 100
size = 0 


def isEmpty(): #공백 상태 검사
    return size == 0

def isFull(): #포화 상태 검사
    return size == capacity

def insert(pos, e): #삽입 연산  
    global size

    if not isFull() and 0 <= pos <= size:
        for i in range(size, pos, -1):
            array[i] = array[i-1] #오른쪽으로 이동
        array[pos] = e #pos에 e를 insert
        size += 1 #갯수 증가
    else:
        print("Overflow of invalid Position")

def delete(pos): #삭제 연산
    global size

    if not isEmpty() and 0 <= pos < size: #pos는 0부터, size는 갯수 
        e = array[pos] #pos에 해당하는 e 
        for i in range(pos, size - 1):
            array[i] = array[i+1] #왼쪽으로 이동
        size -= 1 #갯수 감소
        return e
    else:
        print("Underflow of Invaild Positon")

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
    insert(0,'A')
    insert(1,'B')
    insert(1,'C')
    display()

    delete(0)
    display()

    insert(4,'D')
    insert(3,'E')
    display()

    
    e = input('Input item to delete:')
    idx = findItem(e)
    if idx != -1:
        display(idx)
        display()
