class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child: Optional[TreeNode] = None
        self.right_child: Optional[TreeNode] = None

    def __repr__(self):
        return f"{self}"

    def __str__(self):
        return f"{self.data}"

class TreeBst:
    def __init__(self, root=None):
        self.root = root

    #using iterative
    def insert_iterative(self, data):
        new = TreeNode(data)
        root = self.root
        parent = None
        while root and data != root.data:
            parent = root
            root = root.left_child if data < root.data else root.right_child

        if not parent:
            self.root = new
            return
        
        if parent.data > new.data:
            parent.left_child = new
        else:
            parent.right_child = new

    def traverse_inorder(self):
        ret = []
        def inorder_recursive(root):
            if not root:
                return
            inorder_recursive(root.left_child)
            ret.append(root)
            inorder_recursive(root.right_child)

        inorder_recursive(self.root)
        return ret

if __name__ == "__main__":
    tree = TreeBst()
    elems = 30, 5, 40, 2, 80, 35
    for i in elems:
        tree.insert_iterative(i)

    actions = tree.traverse_inorder()
    print(actions)
