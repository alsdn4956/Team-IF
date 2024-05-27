class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = self.right_child = None
    def __repr__(self):
        return f"{self}"
    def __str__(self):
        return f"{self.data}"


class TreeBinaryBuilder:
    @staticmethod
    def build(sexpr):
        stack = []
        add = lambda node: node if node.data != "#" else None
        
        root = None
        for tok in sexpr:
            if tok != ")":
                stack.append(TreeNode(tok))
                continue
            root_ = None
            while stack[-1].data != "(":
                node = stack.pop()
                if root_ is None:
                    root_ = node
                    continue
                right, root_ = root_, TreeNode(None)
                root_.left_child, root_.right_child = add(node), add(right)
            stack.pop()
            
            if not stack:
                return root_
            
            assert root_
            root = stack.pop()
            root_.data = root.data
            stack.append(root_)
        return root
    
class TreeBst:
    def __init__(self, root):
        self.root = root
    # def search(self, data):
    #     def search_recursive(root):
    #         if root is None:
    #             return None
            
    #         if data == root.data:
    #             return root
            
    #         root = (
    #         search_recursive(root.left_child)
    #         if data < root.data
    #         else search_recursive(root.right_child)
    #         )
    #         return root
        
    #     return search_recursive(self.root)

    # using iterative
    def search(self, data):
        root = self.root
        while root and data != root.data:
            root = root.left_child if data < root.data else root.right_child
        return root

    
if __name__ == "__main__":
    sexpr = "( 30 ( 5 ( 2 # ) 40 ) )".split()
    sexpr = [int(i) if i.isnumeric() else i for i in sexpr]

    root = TreeBinaryBuilder.build(sexpr)
    assert root

    tree = TreeBst(root)

    found = tree.search(5)
    print(found)
    found = tree.search(2)
    print(found)
    found = tree.search(40)
    print(found)
    found = tree.search(30)
    print(found)
    found = tree.search(35)
    print(found)
