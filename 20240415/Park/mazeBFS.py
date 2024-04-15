from CircularQueue import CircularQueue

map =[
       ['1', '1', '1', '1', '1' ,'1'],
       ['e', '0', '1', '0', '0' ,'1'],
       ['1', '0', '0', '0', '1' ,'1'],
       ['1', '0', '1', '0', '1' ,'1'],
       ['1', '0', '1', '0', '0' ,'x'],
       ['1', '1', '1', '1', '1' ,'1']
]

SIZE = 6

def isvalidPos(r, c):

    if 0 <= r < SIZE and 0 <= c < SIZE:
        if map[r][c] == '0' or map[r][c] == 'x':
            return True
    
    return False

def BFS():
    Q = CircularQueue(50)
    Q.enqueue((1,0))
    print('BFS : ')

    while not Q.isEmpty():
        pos = Q.dequeue()
        print(pos, end=" -> ")
        (r,c) = pos

        if(map[r][c] =='x'):
            return True
        
        else:
            map[r][c] = '.'
            if isvalidPos(r-1,c): Q.enqueue((r-1,c))
            if isvalidPos(r+1,c): Q.enqueue((r+1,c))
            if isvalidPos(r,c-1): Q.enqueue((r,c-1))
            if isvalidPos(r,c+1): Q.enqueue((r,c+1))
        Q.display()  # 수정된 부분

    return False

if __name__ == "__main__":
    result = BFS()
    if result:
        print('성공')
    else:
        print("실패")
