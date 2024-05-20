M = 13
table = [0] * M

def hashFn(key):
    return key % M

def getLinear(v, i):
    return (v + i) % M

def insert(key):
    v = hashFn(key)
    i = 0

    while i < M:
        b = getLinear(v, i)

        if table[b] == 0:
            table[b] = key
            return
        else:
            i += 1

def display():
    print()
    print('Bucket   Key')
    print('==============')

    for i in range(M):
        print('HT[%2d] : %2d' % (i, table[i]))

if __name__ == '__main__':
    data = [45, 27, 88, 9, 71, 60, 46, 38, 24]
    for d in data:
        print('h(%2d)=%2d' %(d, hashFn(d)), end = ' ')
        insert(d)
        print(table)

    display()