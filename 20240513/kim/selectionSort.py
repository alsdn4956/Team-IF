def printStep(A, idx):
    print("     step %d:" %idx, end=" ")
    print(A)



def selectionSort(A): #선택 정렬
    n = len(A)

    for i in range(n-1):
        least = i #정렬될 숫자의 idx
        for j in range(i+1,n): # (1,9)
            if A[j] < A[least]: #정렬될 숫자의 idx보다 작으면 least자리가 j자리가 됨
                least = j
        
        A[i], A[least] = A[least], A[i] #least와 j 자리의 숫자 스왑
        printStep(A, i+1) #i+1 -> n-1이라서 



def insertionSort(A): #삽입 정렬
    n = len(A)

    for i in range(1,n): #(1,9)
        key = A[i] #정렬 될 idx의 숫자
        j = i - 1
        while j >= 0 and A[j] > key: #idx가 0 이상 & key보다 클 때 까지
            A[j + 1] = A[j] #두개의 자리 바꿈 
            j -= 1 #앞으로 한칸씩 땡김
        A[j + 1] = key 
        printStep(A, i)
        




if __name__ == "__main__":
    data = [5,3,8,4,9,1,6,2,7]

    L = list(data)
    print("Before :", L)
    selectionSort(L)
    print("Selection :", L)

    L = list(data)
    print("Before :", L)
    insertionSort(L)
    print("Insertion :", L)