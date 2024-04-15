from arrayStack import ArrayStack

map =[
       ['1', '1', '1', '1', '1' ,'1'],
       ['e', '0', '0', '0', '0' ,'1'],
       ['1', '0', '1', '0', '1' ,'1'],
       ['1', '1', '1', '0', '0' ,'x'],
       ['1', '1', '1', '0', '1' ,'1'],
       ['1', '1', '1', '1', '1' ,'1']
]


SIZE = 6

def isvalidPos(r, c):

    if 0 <= r <SIZE and 0 <= c < SIZE:
        if map[r][c] == '0' or map[r][c] == 'x':
            return True
    
    return False

def DFS():
    print("DFS : ")
    S = ArrayStack(100)
    S.push((1,0))

    while not S.isEmpty():
        pos = S.pop()
        print(pos, end = " -> ")
        (r,c) = pos

        if (map[r][c] == 'x'):
            return True
        
        else:
            map[r][c] = '.'
            if isvalidPos(r-1, c): S.push((r-1,c))
            if isvalidPos(r+1, c): S.push((r+1,c))
            if isvalidPos(r, c-1): S.push((r,c-1))
            if isvalidPos(r, c+1): S.push((r,c+1))

        S.display()

    return False

if __name__ == "__main__":
    result = DFS()
    if result:
        print("Success")
    else:
        print("Fail")
