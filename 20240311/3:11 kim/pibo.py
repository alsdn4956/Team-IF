count = 0

def rfib(n):
    global count
    count += 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return rfib(n-2) + rfib(n-1)
    
def ifib(n): #손으로 해보고 이해하기
    if (n <2):
        return n
    
    pp = 0
    p = 1
    for i in range(2,n+1):
        current = p + pp
        pp = p
        p = current

    return current
    
print("rfib: %d" %(rfib(10)))
print("count %d" %count)
print("ifib: %d" %(ifib(10)))