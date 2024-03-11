count = 0

def hanoi(n, fr, tmp, to):
    global count
    count += 1
    
    if (n==1):
        print("%d : Disk %d : %s --> %s" % (count, n, fr, to))
    else:
        hanoi(n-1, fr, to, tmp)
        print("%d : Disk %d : %s --> %s" % (count, n, fr, to))
        hanoi(n-1, tmp, fr, to)

hanoi(4, 'a', 'b', 'c')
