class Node:
    def __init__(self, data=None, link=None):
        self.data= data
        self.link = link

    # ohter 객체가 Node클래스의 인스턴스인지 확인
    # self.__class__ != other.__class__ 와 기능적으로 동일
    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        return self.data == other.data
    
    def __str__(self):
        return f"{self.data}"
    
class ListLinkedSignlyCircular:
    def __init__(self):
        self.tail = None
    
    def empty(self):
        return self.tail is None
    
    def search(self, data):
        if self.empty:
            return False
        
        # 리스트가 비어있는지 확인.
        # 비어있는 경우 AssertionError를 발생시켜 프로그램이 비정상적으로 종료되도록 함.
        # self.tail이 None인지 확인.    
        assert self.tail
        bgn = self.tail.link
        while bgn and bgn != Node(data):
            # 한 바퀴 돌아서 처음 노드로 돌아왔을 떄 종료하기 위함.
            # 모든 노드를 한 바퀴 돌아서 리스트의 끝에 도달했음을 의미함.
            if bgn.link is self.tail.link:
                break
            bgn = bgn.link
        else:
            return True
        return False
    
    def insert_head(self, data):
        new = Node(data)
        if self.empty():
            self.tail = new.link = new
            return
        assert self.tail
        new.link, self.tail.link = self.tail.link, new
        

    def insert_tail(self, data):
        if self.empty():
            self.insert_head(data)
            return
        
        assert self.tail
        new = Node(data, self.tail.link)
        self.tail.link = new
        self.tail = new

    def insert(self, data, after):
        if self.empty():
            raise Exception("insert from empty linked list")
        
        assert self.tail and self.tail.link
        bgn = self.tail.link
        while bgn != Node(after):
            if bgn.link is self.tail.link:
                return
            bgn = bgn.link
    
        if bgn is self.tail:
            self.insert_tail(data)  
            return

        new = Node(data, bgn.link)
        bgn.link  = new   

    def delete(self, data):
        if self.empty():
            raise Exception("delete from empty linked list")
        
        assert self.tail
        prev, bgn = self.tail, self.tail.link

        assert bgn, prev
        while bgn != Node(data):
            prev = bgn
            if bgn.link is self.tail.link:
                return
            bgn = bgn.link

        if bgn is self.tail:
            self.tail = prev
        
        prev.link = bgn.link

    def __str__(self):
        ret = []
        if self.empty():
            return f"{ret}"
        
        assert self.tail
        bgn = self.tail.link
        while bgn:
            ret.append(bgn)
            bgn = bgn.link
            if bgn is self.tail.link:
                break

        ret = ", ".join(map(str, ret))
        return f"[{ret}]"

if __name__ == "__main__":
    llist = ListLinkedSignlyCircular()
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
