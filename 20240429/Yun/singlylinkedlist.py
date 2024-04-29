class Node:
    def __init__(self, data=None, link=None):
        self.data = data
        self.link = link
    
    # 현재 객체와 other객체의 클래스를 직접 비교
    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return False
        return self.data == other.data
    
    def __str__(self):
        return f"{self.data}"

class ListLinkedSingly:
    """Singly Linked List"""
    def __init__(self):
        self.head = None
    
    def empty(self):
        return self.head is None
    
    # 주어진 데이터가 연결리스트 안에 존재하는지 확인하는데 사용
    def search(self, data):
        # 리스트 탐색을 위해 사용. bgn은 노드의 현재 위치를 의미. 처음부터 끝까지 탐색.
        bgn = self.head
        # 리스트의 끝까지 반복하거나 찾고자 하는 데이터가 발견될 때까지 반복
        while bgn and bgn != Node(data):
            bgn = bgn.link
        return bgn is not None
    
    def insert_head(self, data):
        # 새로운 노드를 생성. self.head를 링크로 가지도록.
        new = Node(data, self.head)
        # 리스트의 head를 새로운 노드로 업데이트
        self.head = new
    
    def insert_tail(self, data):
        bgn = self.head

        # 리스트에 노드가 있는 경우. 마지막 노드를 찾은 다음 새로운 노드를 마지막 노드의 다음에 추가.
        # bgn은 현재 노드를 의미. bgn.link는 현재 노드의 다음 노드를 의미.
        # bgn이 Noned인 경우 : 리스트의 끝에 도달했거나 리스트가 비어있는 경우.
        # bgn.link가 None인 경우 : bgn이 마지막 노드인 경우.
        # 위 두 경우에는 반복문이 종료.
        while bgn and bgn.link:
            bgn = bgn.link

        # 리스트가 비어있는 경우 insert_head 메서드 호출.
        if bgn is None:
            self.insert_head(data)
            return
        
        # 'bgn'이 마지막 노드를 가리키는 상태이므로 새로운 노드를 연결
        bgn.link = Node(data)

    def insert(self, data, after):
        if self.empty():
            raise Exception("insert from empty single linked list")
        
        bgn = self.head
        while bgn and bgn != Node(after):
            bgn = bgn.link
        
        if bgn is None: return

        new = Node(data)
        new.link, bgn.link = bgn.link, new

    def delete(self, data):
        if self.empty():
            raise Exception("delete from empty single linked list")
        
        # 삭제할 노드 bgn. 이전 노드 prev
        prev = bgn = self.head
        while bgn and bgn != Node(data):
            prev, bgn = bgn, bgn.link
        
        if bgn is None or prev is None: return

        #  삭제할 노드가 리스트의 첫 번째 노드인 경우.
        self.head = bgn.link if prev is bgn else self.head
        prev.link, bgn = bgn.link, None

    def __str__(self):
        ret = []
        bgn = self.head
        while bgn:
            ret.append(bgn)
            bgn = bgn.link
        
        ret = ", ".join(map(str, ret))
        return f"[{ret}]"
    
if __name__ == "__main__":
    llist = ListLinkedSingly()
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
    llist = ListLinkedSingly()
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
