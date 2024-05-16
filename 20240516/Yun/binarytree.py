class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
    def __str__(self):
        return f"{self.data}"

class TreeBinary:
    def __init__(self):
        self.root = None
    
    def build(self, sexpr):
        stack = []

        def add(node):
            return node if node.data != "#" else None

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
                self.root = root_
                return
            root = stack.pop()
            root_.data = root.data
            stack.append(root_)

        if stack:
            self.root = stack.pop()

if __name__ == "__main__":
    sexpr = "( 30 ( 5 ( 2 # ) 40 ( # 80 ) ) )".split()
    tree = TreeBinary()
    tree.build(sexpr)

    root = tree.root
    print(root)  
    print(root.left_child)  
    print(root.left_child.left_child)  
    print(root.left_child.right_child)  
    print(root.right_child)  
    print(root.right_child.left_child) 
    print(root.right_child.right_child)  
