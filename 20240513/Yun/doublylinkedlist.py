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


class ListLinkedDoubly:
    """Doubly Linked List"""
    def __init__(self):
        self.head = None

    def empty(self):
        return self.head is None
    
    def search(self, data):
        bgn = self.head
        while bgn and bgn != Node(data):
            bgn = bgn.rlink
        return bgn is not None

    def insert_head(self, data):
        new = Node(data)
        new.rlink = self.head
        if self.head:
            self.head.llink = new
        self.head = new

    def insert_tail(self, data):
        bgn = self.head
        while bgn and bgn.rlink:
            bgn = bgn.rlink
        if bgn is None:
            self.insert_head(data)
            return
        bgn.rlink = Node(data, bgn)

    def __str__(self):
        ret = []
        bgn = self.head
        while bgn:
            ret.append(bgn)
            bgn = bgn.rlink
        ret = ", ".join(map(str, ret))
        return f"[{ret}]"

    def insert(self, data, after):
        if self.empty():
            raise Exception("insert from empty linked list")
        
        bgn = self.head
        while bgn and bgn != Node(after):
            bgn = bgn.rlink

        if bgn is None:
            return
        
        if bgn.rlink is None:
            bgn.rlink = Node(data, bgn, None)
            return
        
        new = Node(data, bgn, bgn.rlink)
        bgn.rlink = new

    def delete(self, data):
        if self.empty():
            raise Exception("delete from empty linked list")
        
        bgn = self.head
        while bgn and bgn != Node(data):
            bgn = bgn.rlink

        if bgn is None:
            return
        
        if bgn is self.head and bgn.rlink is None:
            self.head = None
            return
        
        if bgn is self.head and bgn.rlink:
            self.head = bgn.rlink
            bgn.rlink.llink = None
            return
        
        if bgn.llink and bgn.rlink is None:
            bgn.llink.rlink = bgn.rlink
            return
        
        assert bgn.llink and bgn.rlink
        bgn.rlink.llink = bgn.llink
        bgn.llink.rlink = bgn.rlink



if __name__ == "__main__":
    llist = ListLinkedDoubly()
    print(f"list = {llist}")
    data = 10
    llist.insert_tail(data)
    print(f"list.insert_tail({data})")
    print(f"list = {llist}")
    data = 20
    llist.insert_head(data)
    print(f"list.insert_head({data})")
    print(f"list = {llist}")
    data = 30
    llist.insert_tail(data)
    print(f"list.insert_tail({data})")
    print(f"list = {llist}")
    data = 20
    llist.delete(data)
    print(f"list.delete({data})")
    print(f"list = {llist}")
    data, after = 20, 30
    llist.insert(data, after)
    print(f"list.insert({data}, {after})")
    print(f"list = {llist}")
    data, after = 40, 10
    llist.insert(data, after)
    print(f"list.insert({data}, {after})")
    print(f"list = {llist}")
    data, after = 50, 20
    llist.insert(data, after)
    print(f"list.insert({data}, {after})")
    print(f"list = {llist}")
    data, after = 60, 50
    llist.insert(data, after)
    print(f"list.insert({data}, {after})")
    print(f"list = {llist}")
    data = 10
    llist.delete(data)
    print(f"list.delete({data})")
    print(f"list = {llist}")
    data = 60
    print(f"list.search({data}) = {llist.search(data)}")
    llist.delete(data)
    print(f"list.delete({data})")
    print(f"list = {llist}")
    print(f"list.search({data}) = {llist.search(data)}")
