class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def __repr__(self):
        return f"{self}"

    def __str__(self):
        return f"{self.data}"


class TreeBst:
    def __init__(self, root=None):
        self.root = root

    def insert(self, data):
        """Using recursive insertion"""
        def insert_recursive(root, data):
            if not root:
                return TreeNode(data)
            if data < root.data:
                root.left_child = insert_recursive(root.left_child, data)
            elif data > root.data:
                root.right_child = insert_recursive(root.right_child, data)
            return root

        self.root = insert_recursive(self.root, data)

    def delete(self, data):
        """Using recursive deletion"""
        def delete_recursive(root, data):
            if not root:
                return root

            if data < root.data:
                root.left_child = delete_recursive(root.left_child, data)
            elif data > root.data:
                root.right_child = delete_recursive(root.right_child, data)
            else:
                # Node with only one child or no child
                if not root.left_child:
                    temp = root.right_child
                    root = None
                    return temp
                elif not root.right_child:
                    temp = root.left_child
                    root = None
                    return temp

                # Node with two children: Get the inorder successor
                # (smallest in the right subtree)
                temp = self.min_value_node(root.right_child)

                # Copy the inorder successor's content to this node
                root.data = temp.data

                # Delete the inorder successor
                root.right_child = delete_recursive(root.right_child, temp.data)

            return root

        self.root = delete_recursive(self.root, data)

    def min_value_node(self, node):
        current = node
        # loop down to find the leftmost leaf
        while current.left_child is not None:
            current = current.left_child
        return current

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
        tree.insert(i)
    actions = tree.traverse_inorder()
    print(actions)
