class Tree:
    def __init__(self):
        self.root = None

    def build(self, sexpr):
        stack = []

        def add(node):
            return node if node.data != "#" else None

        for tok in sexpr:
            if tok != ")":
                stack.append(self.TreeNode(tok))
            else:
                children = []
                while stack and stack[-1].data != "(":
                    children.append(stack.pop())
                if stack and stack[-1].data == "(":
                    stack.pop()
                if stack:
                    parent = stack.pop()
                    if children:
                        parent.left_child = children.pop()
                        current = parent.left_child
                        while children:
                            current.right_sibling = children.pop()
                            current = current.right_sibling
                    stack.append(parent)
                else:
                    if children:
                        self.root = children.pop()
                        current = self.root
                        while children:
                            current.right_sibling = children.pop()
                            current = current.right_sibling

    class TreeNode:
        def __init__(self, data):
            self.data = data
            self.left_child = None
            self.right_sibling = None

        def __str__(self):
            return f"{self.data}"

    
if __name__ == "__main__":
    expr = "( A ( B ( E ( K L ) F ) C ( G ) D ( H ( M ) I J ) ) )"
    tree = Tree()
    tree.build(expr.split())

    a = tree.root
    print(a)
    
    assert a
    b = a.left_child
    print(b)
    c = b.right_sibling
    print(c)
    d = c.right_sibling
    print(d)

    e = b.left_child
    print(e)
    f = e.right_sibling
    print(f)

    g = c.left_child
    print(g)

    h = d.left_child
    print(h)
    i = h.right_sibling
    print(i)
    j = i.right_sibling
    print(j)
    k = e.left_child
    print(k)
    l = k.right_sibling
    print(l)

    m = h.left_child
    print(m)
