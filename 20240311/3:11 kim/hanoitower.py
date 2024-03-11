def hanoitower(n, fr, tmp, to):
    if(n==1):
        print("Disk %d : %s ---> %s" %(n, fr, to))
    else:
        hanoitower(n-1, fr, to, tmp)
        print("Disk %d : %s ---> %s" %(n, fr, to))
        hanoitower(n-1, tmp, fr, to)

hanoitower(3, 'A', 'B', 'C')