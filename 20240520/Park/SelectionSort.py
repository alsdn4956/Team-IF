def printStep(A, index):
    print('  Step %d : ' %index, end='')
    print(A)

def selectionSort(A):
   
    n = len(A)

    for i in range(n-1):
        least = i
        for j in range(i+1, n):
            if A[j] < A[least]:
                least = j
        A[i], A[least] = A[least], A[i]
        printStep(A, i+1)

def insertionSort(A):

    n = len(A)

    for i in range(1, n):
        key = A[i]
        j = i - 1
        
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key

        printStep(A, i)
        

if __name__ == "__main__":
    data = [5, 3, 8, 4, 9, 1, 6, 2, 7]

    L = list(data)
    print("Before : ", L)

    selectionSort(L)
    print("Selection : ", L)
    
    print()
    
    L = list(data)
    print("Before : ", L)

    insertionSort(L)
    print("Insertion : ", L)