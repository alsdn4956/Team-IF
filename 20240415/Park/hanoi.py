def hanoi(n, fr, tmp, to):
    
    if (n==1):
        print("Disk %d : %s --> %s" % (n, fr, to))
    else:
        hanoi(n-1, fr, to, tmp)
        print("Disk %d : %s --> %s" % (n, fr, to))
        hanoi(n-1, tmp, fr, to)

hanoi(4, 'a', 'b', 'c')
