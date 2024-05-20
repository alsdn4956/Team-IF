class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
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
    
class TreeBinary:
    def __init__(self, root):
        self.root = root
    def traverse_inorder(self):
        ret = []

        def postorder_recursive(root):
            if root is None:
                return
            
            postorder_recursive(root.left_child)
            postorder_recursive(root.right_child)
            ret.append(root)

        postorder_recursive(self.root)
        return ret
    
if __name__ == "__main__":
    sexpr = "( + ( * ( * ( / ( A B ) C ) D ) E ) )".split()
    root = TreeBinaryBuilder.build(sexpr)
    assert root
    tree = TreeBinary(root)
    actions = tree.traverse_inorder()
    print(actions)
