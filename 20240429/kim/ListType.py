from ListNode import ListNode

class ListType:
    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self):
        return self.head == None
    
    def insertFirst(self):
        node = ListNode(data, self.head)
        self.head = node
        self.size += 1
    
    def getNode(self, pos):
        p = self.head

        for i in range(1, pos-1):
            p = p.next

        return p #pos 이전 노드의 주소 위치

    def insertPos(self, pos, data):
        if pos == 1:
            self.insertFirst(data)
        else:
            if (pos <= self.size + 1):
                p = self.getNode(pos)

                node = ListNode(data, p.next)
                p.next = node

            else:
                print("Invaild pos")

    def display(self):
        p = self.head

        while p != None:
            print("[%s] ->" %p.data, end=" ")
            p = p.next
        print("\b\b\b   ")

    #def deleteFirst(self):

    #def deletePos(self):


if __name__ == "__main__":
    L = ListType()
    
    L.insertFirst('a');L.insertFirst('b');L.display()
    L.insertPos('c')
    L.display()