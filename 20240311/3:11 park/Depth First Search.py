class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def dfs_recursive(node):
    if node is not None:
        print(node.value)  # 현재 노드의 값을 출력
        dfs_recursive(node.left)  # 왼쪽 자식 노드를 방문
        dfs_recursive(node.right)  # 오른쪽 자식 노드를 방문

# 간단한 이진 트리 생성
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# 순환적 DFS 호출
print("순환적 DFS 결과:")
dfs_recursive(root)
