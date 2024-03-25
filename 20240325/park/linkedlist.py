class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def insert(self, pos, data):
        if pos < 0:
            print("Invalid position")
            return
        new_node = Node(data)
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            prev_node = self.head
            for _ in range(pos - 1):
                if prev_node is None:
                    print("Invalid position")
                    return
                prev_node = prev_node.next
            new_node.next = prev_node.next
            prev_node.next = new_node

    def delete(self, pos):
        if pos < 0 or self.head is None:
            print("Invalid position or list is empty")
            return
        if pos == 0:
            deleted_item = self.head.data
            self.head = self.head.next
            return deleted_item
        prev_node = self.head
        for _ in range(pos - 1):
            if prev_node.next is None:
                print("Invalid position")
                return
            prev_node = prev_node.next
        if prev_node.next is None:
            print("Invalid position")
            return
        deleted_item = prev_node.next.data
        prev_node.next = prev_node.next.next
        return deleted_item

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


if __name__ == "__main__":
    L1 = LinkedList()
    L1.insert(0, "A")
    L1.insert(1, "B")
    L1.insert(2, "C")
    L1.insert(3, "D")
    L1.display()
