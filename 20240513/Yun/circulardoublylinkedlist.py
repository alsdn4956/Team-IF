class Node:
    def __init__(self, data=None, llink=None, rlink=None):
        self.data = data
        self.llink = llink
        self.rlink = rlink

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        
        return self.data == other.data
    
    def __str__(self):
        return f"{self.data}"


class ListLinkedDoublyCircular:
    """Circular Doubly Linked List"""

    def __init__(self):
        self.head = None

    def empty(self):
        return self.head is None
    
    def search(self, data):
        bgn = self.head
        if bgn is None:
            return False
        while bgn:
            if bgn.data == data:
                return True
            if bgn.rlink == self.head:
                return False
            bgn = bgn.rlink

    def insert_head(self, data):
        new = Node(data)
        if self.empty():
            self.head = new
            new.llink = new
            new.rlink = new
            return
        new.rlink = self.head
        new.llink = self.head.llink
        self.head.llink.rlink = new
        self.head.llink = new
        self.head = new

    def insert_tail(self, data):
        new = Node(data)
        if self.empty():
            self.head = new
            new.llink = new
            new.rlink = new
            return
        new.llink = self.head.llink
        new.rlink = self.head
        self.head.llink.rlink = new
        self.head.llink = new

    def insert(self, data, after):
        if self.empty():
            raise Exception("insert from empty linked list")
        
        bgn = self.head
        while bgn:
            if bgn.data == after:
                new = Node(data)
                new.rlink = bgn.rlink
                bgn.rlink.llink = new
                bgn.rlink = new
                new.llink = bgn
                if bgn == self.head.llink:
                    self.head.llink = new
                return
            if bgn.rlink == self.head:
                break
            bgn = bgn.rlink

        raise ValueError(f"Node with data '{after}' not found")

    def delete(self, data):
        if self.empty():
            raise Exception("delete from empty linked list")
        
        bgn = self.head
        while bgn:
            if bgn.data == data:
                if bgn == self.head:
                    if bgn.rlink == self.head:
                        self.head = None
                    else:
                        self.head = bgn.rlink
                        bgn.rlink.llink = self.head.llink
                        self.head.llink.rlink = bgn.rlink
                else:
                    bgn.llink.rlink = bgn.rlink
                    bgn.rlink.llink = bgn.llink
                return
            if bgn.rlink == self.head:
                break
            bgn = bgn.rlink

        raise ValueError(f"Node with data '{data}' not found")

    def __str__(self):
        ret = []
        bgn = self.head
        if bgn is None:
            return "[]"
        while bgn:
            ret.append(bgn)
            if bgn.rlink == self.head:
                break
            bgn = bgn.rlink
        return f"[{', '.join(map(str, ret))}]"


if __name__ == "__main__":
    llist = ListLinkedDoublyCircular ()
    print(f"list = {llist}")
    data = 10
    llist.insert_head(data)
    print(f"list.insert_head({data})")
    print(f"list = {llist}")
    data = 20
    llist.insert_head(data)
    print(f"list.insert_head({data})")
    print(f"list = {llist}")
    data = 30
    llist.insert_head(data)
    print(f"list.insert_head({data})")
    print(f"list = {llist}")
    data = 40
    llist.insert_tail(data)
    print(f"list.insert_tail({data})")
    print(f"list = {llist}")
    data = 50
    llist.insert_tail(data)
    print(f"list.insert_tail({data})")
    print(f"list = {llist}")
    data = 60
    llist.insert_head(data)
    print(f"list.insert_head({data})")
    print(f"list = {llist}")
    data, after = 100, 30
    llist.insert(data, after)
    print(f">> llist.insert({data}, {after})")
    print(f"llist = {llist}")
    data, after = 200, 60
    llist.insert(data, after)
    print(f">> llist.insert({data}, {after})")
    print(f"llist = {llist}")
    data, after = 300, 200
    llist.insert(data, after)
    print(f">> llist.insert({data}, {after})")
    print(f"llist = {llist}")
    data, after = 400, 50
    llist.insert(data, after)
    print(f">> llist.insert({data}, {after})")
    print(f"llist = {llist}")
    data = 30
    llist.delete(data)
    print(f"list.delete({data})")
    print(f"list = {llist}")
    data = 400
    llist.delete(data)
    print(f"list.delete({data})")
    print(f"list = {llist}")
    data = 70
    llist.insert_tail(data)
    print(f"list.insert_tail({data})")
    print(f"list = {llist}")
    data = 60
    llist.delete(data)
    print(f"list.delete({data})")
    print(f"list = {llist}")
    data = 70
    llist.delete(data)
    print(f"list.delete({data})")
    print(f"list = {llist}")
    data = 200
    llist.delete(data)
    print(f"list.delete({data})")
    print(f"list = {llist}")